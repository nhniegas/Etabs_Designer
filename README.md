# Etabs_Designer
### Software extension for ETABS specialized for extended design routine in structural analysis and design. Below are the key components/features that the program whants to attain:

### A. Security Feature
    * A user input form that requires specific username and password
    * For temporary development stage, there is only one single permissible login credentials 
### B. Session State Management
    * Same as conventional desktop application where there is New, Open, Save, and Save As menu components
    * Incorparates the concept of caching for storage management of previous session states 
### C. Direct Data Extraction from Etabs
    * Ask the user to link the specific etabs file where design routine is intended
    * Automatically triggers the "Etabs Model Run Analysis" state if not yet performed
    * Real-time extraction of runtime data for both analysis and design specific to the Etabs Design Module
    * Requires the use of comtypes library for direct communication from Etabs API to Python Script
### D. Etabs Designer Modules
    * Concrete Beam/Girder Designer
        * Interactive editing feature and real-time reflection of design results 
    * Concrete Column Designer
        *  Interactive editing feature and real-time reflection of design results 
