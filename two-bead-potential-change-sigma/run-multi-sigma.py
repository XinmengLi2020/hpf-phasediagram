# This is a python script that prepares a series of simulations
# The looping variable is h, the width of grids in the hybrid particle-field simulations

import os
import numpy as np


# sytem info
box_size = 10.0
template_folder = 'simulation-template'
modi_filename = 'options.toml'

# Define the range of h, step is 0.02 when h < 0.1 and 0.05 when h > 0.1
h_min = 0.02
h_max = 0.5
h_array = np.arange(h_min, 0.1, 0.02)
h_array = np.append(h_array, np.arange(0.1, h_max, 0.05))
h_array = np.append(h_array, h_max)
# print(h_array)

# loop over h
for h in h_array:
    # no.grid
    n = int(box_size / h)
    print('h =', h, 'n =', n)

    # create folder: copy from the base folder
    # h two digits after the decimal point
    dir_name = f"h-{h:.2f}"

    # prepare step
    PREPARE = False
    if PREPARE:
        os.system(f'cp -r {template_folder} ' + dir_name)

        # change the input file in the new folder
        # replace the 1000 by n in the line "mesh_size = [100, 100, 100]"
        # read the file
        modi_file = os.path.join(dir_name, modi_filename)
        with open(modi_file, 'r') as file:
            lines = file.readlines()
        # Iterate over the lines and replace the value if found
        for i, line in enumerate(lines):
            if "mesh_size = [100, 100, 100]" in line:
                lines[i] = line.replace("100", str(n))

        # Write the modified contents back to the file
        with open(modi_file, 'w') as file:
            file.writelines(lines)
