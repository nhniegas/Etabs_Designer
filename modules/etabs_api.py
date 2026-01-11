import os
import comtypes
import comtypes.client
import pandas as pd


class ETABSConnector:
    def __init__(self):
        # Initialize ETABS API connection variables
        self.etabs_object = None
        self.sap_model = None
        self.program_path = ""
        self.model_path = ""
        self.model_name = ""
        self.is_connected = False

        # Design parameters for concrete design
        self.load_combinations = []
        self.concrete_design_code = "ACI 318-14"

    def connect(self):
        self.program_path = (
            r"C:\Program Files\Computers and Structures\ETABS 22\ETABS.exe"
        )
        self.model_path = (
            r"C:\Users\Acer\Desktop\Etabs_Sample_API_Test\Etabs_Sample_API_Test.EDB"
        )

        # Create the ETABS API Helper Object
        try:
            helper = comtypes.client.CreateObject("ETABSv1.Helper")
            helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)

            # Create a new instance of ETABS
            self.etabs_object = helper.CreateObject(self.program_path)

            # Create SapModel Object
            self.sap_model = self.etabs_object.SapModel
            self.sap_model.InitializeNewModel

            # Set connection to true
            self.is_connected = True

        except Exception as e:
            print(f"Error connecting to ETABS: {e}")
            self.is_connected = False
            return False

    def open_model(self, model_path: str):
        # Check ETABS API Connection
        if not self.is_connected:
            print("Not connected to ETABS. Call connect() first.")
            return False

        # Verify model path exists
        if not os.path.exists(model_path):
            print(f"Model file not found: {model_path}")
            return False

        self.etabs_object.ApplicationStart()

        try:
            # Open the model
            self.sap_model.File.OpenFile(model_path)
            print(f"Model opened successfully: {model_path}")
            return True

        except Exception as e:
            print(f"Error opening model: {e}")
            return False

    def run_analysis(self):
        # Check ETABS API Connection
        if not self.is_connected or not self.model_path:
            print("No model loaded. Open a model first.")
            return False

        try:
            # Save the model before analysis``
            self.sap_model.File.Save(self.model_path)

            # Run the analysis
            run_info = self.sap_model.Analyze.RunAnalysis()
            if run_info == 0:
                print("Analysis completed successfully")
                return True
            else:
                print(f"Analysis failed with code: {run_info}")
                return False

        except Exception as e:
            print(f"Error running analysis: {e}")
            return False

    def run_concrete_design(self):
        # Check ETABS API Connection
        if not self.is_connected or not self.model_path:
            print("No model loaded. Open a model first.")
            return False

        try:
            # Set design code (example: ACI 318-14)
            self.sap_model.DesignConcrete.SetCode(self.concrete_design_code)

            # Run concrete design
            run_info = self.sap_model.DesignConcrete.StartDesign()
            if run_info == 0:
                print("Concrete design completed successfully")
                return True
            else:
                print(f"Concrete design failed with code: {run_info}")
                return False

        except Exception as e:
            print(f"Error running concrete design: {e}")
            return False

    def get_concrete_data(self):
        # Check ETABS API Connection
        if not self.is_connected or not self.model_path:
            return {}

        # Set table name
        table_name = "Material Properties - Concrete Data"

        try:
            # Get all raw data
            concrete_data = self.sap_model.DatabaseTables.GetTableForDisplayArray(
                table_name, [], "", 0
            )

            # Check if retrieval was successful
            if concrete_data[5] == 0:
                print("Concrete Frame Data Retrieved Successfully")

                # Store data in a pandas dataframe
                headers = concrete_data[2]
                table_data = concrete_data[4]
                num_columns = len(headers)
                row_list = []
                for i in range(0, len(table_data), num_columns):
                    row = table_data[i : i + num_columns]
                    row_list.append(row)
                concrete_dataframe = pd.DataFrame(row_list, columns=headers)
                return concrete_dataframe

            else:
                print(
                    f"Failed to retrieve Concrete Frame Data with code: {concrete_data[6]}"
                )

        except Exception as e:
            return {"error": str(e)}

    def get_rebar_data(self):
        # Check ETABS API Connection
        if not self.is_connected or not self.model_path:
            return {}

        # Set table name
        table_name = "Material Properties - Rebar Data"

        try:
            # Get all raw data
            rebar_data = self.sap_model.DatabaseTables.GetTableForDisplayArray(
                table_name, [], "", 0
            )

            # Check if retrieval was successful
            if rebar_data[5] == 0:
                print("Rebar Data Retrieved Successfully")

                # Store data in a pandas dataframe
                headers = rebar_data[2]
                table_data = rebar_data[4]
                num_columns = len(headers)
                row_list = []
                for i in range(0, len(table_data), num_columns):
                    row = table_data[i : i + num_columns]
                    row_list.append(row)
                rebar_dataframe = pd.DataFrame(row_list, columns=headers)
                print(rebar_dataframe)
                return rebar_dataframe

            else:
                print(f"Failed to retrieve Rebar Data with code: {rebar_data[6]}")

        except Exception as e:
            return {"error": str(e)}

    def get_frame_section_rectangular(self):
        # Check ETABS API Connection
        if not self.is_connected or not self.model_path:
            return {}

        # Set table name

        table_name = "Frame Section Property Definitions - Concrete Rectangular"

        try:
            # Get all raw data
            frame_section_summary = (
                self.sap_model.DatabaseTables.GetTableForDisplayArray(
                    table_name, [], "", 0
                )
            )

            # Check if retrieval was successful
            if frame_section_summary[5] == 0:
                print("Frame Section Retrieved Successfully")

                # Store data in a pandas dataframe
                headers = frame_section_summary[2]
                table_data = frame_section_summary[4]
                num_columns = len(headers)
                row_list = []
                for i in range(0, len(table_data), num_columns):
                    row = table_data[i : i + num_columns]
                    row_list.append(row)
                frame_section_dataframe = pd.DataFrame(row_list, columns=headers)
                return frame_section_dataframe

            else:
                print(
                    f"Failed to retrieve Frame Section with code: {frame_section_summary[6]}"
                )

        except Exception as e:
            return {"error": str(e)}

    def get_frame_section_circular(self):
        # Check ETABS API Connection
        if not self.is_connected or not self.model_path:
            return {}

        # Set table name

        table_name = "Frame Section Property Definitions - Concrete Circle"

        try:
            # Get all raw data
            frame_section_summary = (
                self.sap_model.DatabaseTables.GetTableForDisplayArray(
                    table_name, [], "", 0
                )
            )

            # Check if retrieval was successful
            if frame_section_summary[5] == 0:
                print("Frame Section Retrieved Successfully")

                # Store data in a pandas dataframe
                headers = frame_section_summary[2]
                table_data = frame_section_summary[4]
                num_columns = len(headers)
                row_list = []
                for i in range(0, len(table_data), num_columns):
                    row = table_data[i : i + num_columns]
                    row_list.append(row)
                frame_section_dataframe = pd.DataFrame(row_list, columns=headers)
                return frame_section_dataframe

            else:
                print(
                    f"Failed to retrieve Frame Section with code: {frame_section_summary[6]}"
                )

        except Exception as e:
            return {"error": str(e)}

    def get_concrete_beam_flexure_envelope(self):
        # Check ETABS API Connection
        if not self.is_connected or not self.model_path:
            return {}

        # Set table name

        table_name = f"Concrete Beam Flexure Envelope - {self.concrete_design_code}"

        try:
            # Get all raw data
            beam_envelope_summary = (
                self.sap_model.DatabaseTables.GetTableForDisplayArray(
                    table_name, [], "", 0
                )
            )

            # Check if retrieval was successful
            if beam_envelope_summary[5] == 0:
                print("Concrete Beam Flexure Envelope Retrieved Successfully")

                # Store data in a pandas dataframe
                headers = beam_envelope_summary[2]
                table_data = beam_envelope_summary[4]
                num_columns = len(headers)
                row_list = []
                for i in range(0, len(table_data), num_columns):
                    row = table_data[i : i + num_columns]
                    row_list.append(row)
                beam_flexure_dataframe = pd.DataFrame(row_list, columns=headers)
                return beam_flexure_dataframe

            else:
                print(
                    f"Failed to retrieve Concrete Beam Flexure Envelope with code: {beam_envelope_summary[6]}"
                )

        except Exception as e:
            return {"error": str(e)}

    def get_concrete_beam_shear_envelope(self):
        # Check ETABS API Connection
        if not self.is_connected or not self.model_path:
            return {}

        # Set table name

        table_name = f"Concrete Beam Shear Envelope - {self.concrete_design_code}"

        try:
            # Get all raw data
            beam_envelope_summary = (
                self.sap_model.DatabaseTables.GetTableForDisplayArray(
                    table_name, [], "", 0
                )
            )

            # Check if retrieval was successful
            if beam_envelope_summary[5] == 0:
                print("Concrete Beam Shear Envelope Retrieved Successfully")

                # Store data in a pandas dataframe
                headers = beam_envelope_summary[2]
                table_data = beam_envelope_summary[4]
                num_columns = len(headers)
                row_list = []
                for i in range(0, len(table_data), num_columns):
                    row = table_data[i : i + num_columns]
                    row_list.append(row)
                beam_shear_dataframe = pd.DataFrame(row_list, columns=headers)
                return beam_shear_dataframe

            else:
                print(
                    f"Failed to retrieve Concrete Beam Shear Envelope with code: {beam_envelope_summary[6]}"
                )

        except Exception as e:
            return {"error": str(e)}

    def close_model(self):
        try:
            self.sap_model.File.Save(self.model_path)
            print("Model saved successfully.")
            self.etabs_object.ApplicationExit(False)
            print("ETABS application closed successfully.")

            self.sap_model = None
            self.etabs_object = None
        except Exception as e:
            print(f"Error closing model: {e}")
            return False


if __name__ == "__main__":
    test_etabs = ETABSConnector()
    test_etabs.connect()
    test_etabs.open_model(test_etabs.model_path)
    test_etabs.run_analysis()
    test_etabs.run_concrete_design()
    concrete_data = test_etabs.get_concrete_data()
    print(concrete_data)
