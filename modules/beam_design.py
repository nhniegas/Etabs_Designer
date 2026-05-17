import numpy as np
from concreteproperties.material import Concrete, SteelBar
import concreteproperties.stress_strain_profile as ssp
import sectionproperties.pre.library.primitive_sections as sp_ps
from concreteproperties.pre import add_bar_rectangular_array
from concreteproperties.concrete_section import ConcreteSection
from typing import Any


class ConcreteDesign:
    def __init__(self):
        self.des_param: dict[str, Any] = {
            "design_code": "ACI 318-14",
            "flexure_reduction_factor": None,
            "shear_reduction_factor": None,
            "alpha_factor": None,  # For rectangular stress block
            "beta_factor": None,  # For rectangular stress block
            "lw_factor": None,
        }

        self.mat_prop: dict[str, Any] = {
            "concrete": None,
            "main_bar": None,
            "secondary_bar": None,
        }

        self.beam_geom: dict[str, Any] = {
            "depth": None,
            "width": None,
            "main_bar_diameter": None,
            "secondary_bar_diameter": None,
            "web_bar_diameter": None,
            "concrete_cover": None,
        }

        self.seis_param: dict[str, Any] = {
            "rho_max": False,
            "half_moment": False,
            "fourth_moment": False,
            "probable_shear": False,
            "gravity_load_moment": None,
        }

        self.bending_cap: dict[str, Any] = {
            "Positive_moment": False,
            "Negative_moment": False,
        }

    def set_design_param(
        self,
        design_code: str,
        flexure_reduction_factor: float,
        shear_reduction_factor: float,
        alpha_factor: float,
        beta_factor: float,
    ):
        self.des_param["design_code"] = design_code
        self.des_param["flexure_reduction_factor"] = flexure_reduction_factor
        self.des_param["shear_reduction_factor"] = shear_reduction_factor
        self.des_param["alpha_factor"] = alpha_factor
        self.des_param["beta_factor"] = beta_factor

    def set_mat_prop(self, alpha, f_c: float, f_y: float, f_yt: float):
        E_c = 4700 * np.sqrt(f_c)
        Beta = 0.85 if f_c <= 28 else max(0.85 - 0.05 * ((f_c - 28) / 7), 0.65)
        self.mat_prop["alpha_factor"] = alpha
        self.mat_prop["beta_factor"] = Beta

        self.mat_prop["concrete"] = Concrete(
            name=f"{f_c} MPa Concrete",
            density=2.4e-6,
            stress_strain_profile=ssp.ConcreteLinear(elastic_modulus=E_c),
            ultimate_stress_strain_profile=ssp.RectangularStressBlock(
                compressive_strength=f_c,
                alpha=0.85,
                gamma=Beta,
                ultimate_strain=0.003,
            ),
            flexural_tensile_strength=4.2,
            colour="lightgrey",
        )

        self.mat_prop["main_bar"] = SteelBar(
            name=f"{f_y} MPa Main Rebar",
            density=7.85e-6,
            stress_strain_profile=ssp.SteelElasticPlastic(
                yield_strength=f_y,
                elastic_modulus=200e3,
                fracture_strain=0.05,
            ),
            colour="grey",
        )

        self.mat_prop["secondary_bar"] = SteelBar(
            name=f"{f_yt} MPa Secondary Rebar",
            density=7.85e-6,
            stress_strain_profile=ssp.SteelElasticPlastic(
                yield_strength=f_yt,
                elastic_modulus=200e3,
                fracture_strain=0.05,
            ),
            colour="grey",
        )

    def set_beam_geom(
        self,
        depth: float,
        width: float,
        main_bar_diameter: float,
        secondary_bar_diameter: float,
        web_bar_diameter: float,
        concrete_cover: float,
    ):
        self.beam_geom["depth"] = depth
        self.beam_geom["width"] = width
        self.beam_geom["main_bar_diameter"] = main_bar_diameter
        self.beam_geom["secondary_bar_diameter"] = secondary_bar_diameter
        self.beam_geom["web_bar_diameter"] = web_bar_diameter
        self.beam_geom["concrete_cover"] = concrete_cover

    def set_seis_param(
        self,
        rho_max: bool,
        half_moment: bool,
        fourth_moment: bool,
        probable_shear: bool,
        gravity_load_moment: float,
    ):
        self.seis_param["rho_max"] = rho_max
        self.seis_param["half_moment"] = half_moment
        self.seis_param["fourth_moment"] = fourth_moment
        self.seis_param["probable_shear"] = probable_shear
        self.seis_param["gravity_load_moment"] = gravity_load_moment

    def min_reinf(self):
        return (
            0.25
            * np.sqrt(
                self.mat_prop["concrete"].stress_strain_profile.compressive_strength
            )
            / self.mat_prop["main_bar"].stress_strain_profile.yield_strength
        )

    def max_reinf_bar_per_layer(self):
        s_min = min(25, self.beam_geom["secondary_bar_diameter"])
        max_bars = int(
            self.beam_geom["width"]
            - 2 * self.beam_geom["concrete_cover"]
            - 2 * self.beam_geom["secondary_bar_diameter"]
        ) / (s_min + self.beam_geom["main_bar_diameter"])

        return int(max_bars)

    def beam_reinf(self, n_main_reinf_top: int, n_main_reinf_bot: int):
        beam = sp_ps.rectangular_section(
            d=self.beam_geom["depth"],
            b=self.beam_geom["width"],
            material=self.mat_prop["concrete"],
        )

        rho_max_check = []

        if self.seis_param["rho_max"]:
            rho_top = (
                np.pi
                * self.beam_geom["main_bar_diameter"] ** 2
                / 4
                * n_main_reinf_top
                / (self.beam_geom["width"] * self.beam_geom["depth"])
            )
            rho_bottom = (
                np.pi
                * self.beam_geom["main_bar_diameter"] ** 2
                / 4
                * n_main_reinf_bot
                / (self.beam_geom["width"] * self.beam_geom["depth"])
            )
            if rho_top > 0.025:
                rho_max_check.append(f"Top ratio ({rho_top:.3%}) > {0.025:.1%}")
            if rho_bottom > 0.025:
                rho_max_check.append(f"Bottom ratio ({rho_bottom:.3%}) > {0.025:.1%}")

        bars_per_layer_top = []
        bars_per_layer_bottom = []

        while n_main_reinf_top > 0:
            if n_main_reinf_top > self.max_reinf_bar_per_layer():
                bars_per_layer_top.append(self.max_reinf_bar_per_layer())
                n_main_reinf_top = n_main_reinf_top - self.max_reinf_bar_per_layer()
            else:
                if n_main_reinf_top == 1:
                    n_main_reinf_top += 1
                bars_per_layer_top.append(n_main_reinf_top)
                n_main_reinf_top = 0

        while n_main_reinf_bot > 0:
            if n_main_reinf_bot > self.max_reinf_bar_per_layer():
                bars_per_layer_bottom.append(self.max_reinf_bar_per_layer())
                n_main_reinf_bot = n_main_reinf_bot - self.max_reinf_bar_per_layer()
            else:
                if n_main_reinf_bot == 1:
                    n_main_reinf_bot += 1
                bars_per_layer_bottom.append(n_main_reinf_bot)
                n_main_reinf_bot = 0

        max_bar_per_layer_check = []

        if len(bars_per_layer_top) > 3:
            max_bar_per_layer_check.append(
                "Top reinforcement exceeds 3 layers. Increase beam width or bar diameter."
            )
        if len(bars_per_layer_bottom) > 3:
            max_bar_per_layer_check.append(
                "Bottom reinforcement exceeds 3 layers. Increase beam width or bar diameter."
            )

        for i in range(len(bars_per_layer_top)):
            beam = add_bar_rectangular_array(
                geometry=beam,
                area=(np.pi / 4) * (self.beam_geom["main_bar_diameter"] ** 2),
                material=self.mat_prop["main_bar"],
                n_x=bars_per_layer_top[i],
                x_s=(
                    self.beam_geom["width"]
                    - 2 * self.beam_geom["concrete_cover"]
                    - 2 * self.beam_geom["secondary_bar_diameter"]
                    - self.beam_geom["main_bar_diameter"]
                )
                / bars_per_layer_top[i],
                anchor=(
                    self.beam_geom["concrete_cover"]
                    + self.beam_geom["secondary_bar_diameter"]
                    + self.beam_geom["main_bar_diameter"] / 2,
                    self.beam_geom["depth"]
                    - self.beam_geom["concrete_cover"]
                    - self.beam_geom["secondary_bar_diameter"]
                    - self.beam_geom["main_bar_diameter"] / 2
                    - i * (self.beam_geom["main_bar_diameter"] + 25),
                ),
            )

        for i in range(len(bars_per_layer_bottom)):
            beam = add_bar_rectangular_array(
                geometry=beam,
                area=(np.pi / 4) * (self.beam_geom["main_bar_diameter"] ** 2),
                material=self.mat_prop["main_bar"],
                n_x=bars_per_layer_bottom[i],
                x_s=(
                    self.beam_geom["width"]
                    - 2 * self.beam_geom["concrete_cover"]
                    - 2 * self.beam_geom["secondary_bar_diameter"]
                    - self.beam_geom["main_bar_diameter"]
                )
                / bars_per_layer_bottom[i],
                anchor=(
                    self.beam_geom["concrete_cover"]
                    + self.beam_geom["secondary_bar_diameter"]
                    + self.beam_geom["main_bar_diameter"] / 2,
                    self.beam_geom["concrete_cover"]
                    + self.beam_geom["secondary_bar_diameter"]
                    + self.beam_geom["main_bar_diameter"] / 2
                    + i * (self.beam_geom["main_bar_diameter"] + 25),
                ),
            )

        return max_bar_per_layer_check, rho_max_check, beam

    def ult_bend_cap(self, beam):
        beam_conrete_section = ConcreteSection(beam)
        sag_res = beam_conrete_section.ultimate_bending_capacity()
        hog_res = beam_conrete_section.ultimate_bending_capacity(theta=np.pi)

        self.bending_cap["Positive_moment"] = (
            self.des_param["flexure_reduction_factor"] * sag_res
        )
        self.bending_cap["Negative_moment"] = (
            self.des_param["flexure_reduction_factor"] * hog_res
        )

    def conc_shear_cap(self):
        V_c = (
            0.17
            * self.mat_prop["lw_factor"]
            * np.sqrt(
                self.mat_prop["concrete"].stress_strain_profile.compressive_strength
            )
            * self.beam_geom["width"]
            * self.beam_geom["depth"]
        )

        return V_c

    def shear_reinf(self):
        pass
