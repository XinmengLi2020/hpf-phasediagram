import os
import numpy as np


# distance array
d_min = 0.30
d_middle = 0.5
d_max = 1.0
d_array = np.arange(d_min, d_middle, 0.01)
d_array = np.append(d_array, np.arange(d_middle, d_max, 0.03))


# Directory where folders containing sim.log files are located
base_directory = './'

# Output file to save collected field E values
output_file = 'field_E_values.txt'

with open(output_file, 'w') as out_file:
    # Loop through each distance folder
    for distance in [f'distance_{d:.2f}' for d in d_array]:
        folder_path = os.path.join(base_directory, distance)
        log_file = os.path.join(folder_path, 'sim.log')

        # Check if the log file exists
        if os.path.exists(log_file):
            with open(log_file, 'r') as log:
                lines = log.readlines()
                for i, line in enumerate(lines):
                    if line.startswith('         step         time         temp        tot E        kin E        pot E      field E '):
                        field_E_line = lines[i+1]
                        field_E_value = float(field_E_line.split()[6])
                        # Write the field E value to the output file
                        d = distance.split('_')[1]
                        out_file.write(f'{d}  {field_E_value}\n')
                        print(f'Field E value for {distance}: {field_E_value}')
                        break
        else:
            print(f'Log file not found in {folder_path}')
