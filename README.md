#  Single Plant Resolution Irrigation - A data management and visualization tool
##### Last edited by: M. Jenkins
##### Date: 06.30.18

## Overview
A command line executable pipeline for data harvesting and analysis. Allows nearly seamless interfacing between modern operating systems and Campbell Scientific loggers.  Resulting data is immediately available in a highly customizable format (numpy arrays) and visualized using the robust matplotlib Python library.

### Workflow:
1) Connect and collect '.dat' data files from a Campbell Scientific datalogger. Expect this to take 10 minutes to 1 hour.

##### Next few steps take less than 5 minutes, always.
- Move '.dat' data files into '/dat_to_csv.py/files_to_convert/' or copy filepath to clipboard
- Use command line executable 'dat_to_csv.py', following prompts accordingly to convert '.dat' file to '.csv' file
- Use 'SVRI_data_machine.ipynb' to visualize data


### Data example:
![alt text][logo]

[logo]: https://github.com/mattjenkins3/SinglePlant_Irrigation_DataTool/blob/master/images/06.15-28.18_battV.png "main panel temp over time"
