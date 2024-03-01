import os
import numpy as np
import matplotlib.pyplot as plt


box_size = 10.0


def two_gaussian(r, a_G1, a_G2, sigma_G1, sigma_G2):
    return -a_G1 * np.exp(-(r / sigma_G1) ** 2) - a_G2 * np.exp(-(r / sigma_G2) ** 2)


r_Ar = np.linspace(0.3, 1.0, 50)
plt.figure(figsize=(10, 8))
plt.plot(r_Ar, two_gaussian(r_Ar, -29.288, 8.291, 0.208, 0.304),
         'g-', label='Fitted Two-Gaussian Model*', linewidth=3)


# Define the range of h, step is 0.02 when h < 0.1 and 0.05 when h > 0.1
h_min = 0.02
h_max = 0.5
h_array = np.arange(h_min, 0.1, 0.02)
h_array = np.append(h_array, np.arange(0.1, h_max, 0.05))
h_array = np.append(h_array, h_max)
# print(h_array)

# The looping variable is h, the width of grids in the hybrid particle-field simulations
# loop over h
for h in h_array[:5]:
    # no.grid
    n = int(box_size / h)
    print('h =', round(h, 2), 'n =', n)

    # create folder: copy from the base folder
    # h two digits after the decimal point
    dir_name = f"h-{h:.2f}"

    # read the data file
    data_file = f'./{dir_name}/field_E_values.txt'
    r_sim = []
    e_sim = []
    with open(data_file, 'r') as file:
        data = file.read()
        # Split the data into lines
        lines = data.split('\n')
        # Parse each line to separate the distance and value
        parsed_data = [(float(line.split()[0]), float(line.split()[1]))
                       for line in lines if line]
        # Print the parsed data

        for distance, value in parsed_data:
            r_sim.append(distance)
            e_sim.append(value)

        plt.plot(r_sim, e_sim, '-o', label=f'two-bead simulation: h={h:.2f}')


plt.title('Two-Gaussian Potential with varing h')
plt.ylabel('Potential Energy (kJ/mol)')
plt.legend()


# Modify x-axis labels to include reduced units in another row
plt.xticks(np.arange(0.3, 1.1, 0.1), [
           f"{d:.1f}\n{d/0.3405:.2f}" for d in np.arange(0.3, 1.1, 0.1)])
plt.xlabel('Distance (nm) / Reduced Distance')

plt.grid(True)
plt.savefig('change-grid-width.pdf')
