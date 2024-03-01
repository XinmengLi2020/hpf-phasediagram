import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# parse simulation data
data_file = './simulation/field_E_values.txt'
with open(data_file, 'r') as file:
    data = file.read()
# Split the data into lines
lines = data.split('\n')
# Parse each line to separate the distance and value
parsed_data = [(float(line.split()[0]), float(line.split()[1]))
               for line in lines if line]
# Print the parsed data
r_sim = []
e_sim = []
for distance, value in parsed_data:
    r_sim.append(distance)
    e_sim.append(value)


data_file = './simulation-2-150grids/field_E_values.txt'
with open(data_file, 'r') as file:
    data = file.read()
# Split the data into lines
lines = data.split('\n')
# Parse each line to separate the distance and value
parsed_data = [(float(line.split()[0]), float(line.split()[1]))
               for line in lines if line]
# Print the parsed data
r_sim2 = []
e_sim2 = []
for distance, value in parsed_data:
    r_sim2.append(distance)
    e_sim2.append(value)


data_file = './simulation-3-172grids/field_E_values.txt'
with open(data_file, 'r') as file:
    data = file.read()
# Split the data into lines
lines = data.split('\n')
# Parse each line to separate the distance and value
parsed_data = [(float(line.split()[0]), float(line.split()[1]))
               for line in lines if line]
# Print the parsed data
r_sim3 = []
e_sim3 = []
for distance, value in parsed_data:
    r_sim3.append(distance)
    e_sim3.append(value)


# Lennard-Jones potential for Argon
def lj_potential(r, epsilon, sigma):
    return 4 * epsilon * ((sigma / r) ** 12 - (sigma / r) ** 6)

# Two-Gaussian model


def two_gaussian(r, a_G1, a_G2, sigma_G1, sigma_G2):
    return -a_G1 * np.exp(-(r / sigma_G1) ** 2) - a_G2 * np.exp(-(r / sigma_G2) ** 2)


# Parameters for Argon LJ potential
sigma_Ar = 0.3405  # nm
epsilon_Ar = 0.996  # kJ/mol

# Generate data for LJ potential
r_Ar = np.linspace(0.3, 1.0, 50)
V_Ar = lj_potential(r_Ar, epsilon_Ar, sigma_Ar)

# Fit the LJ potential with the two-Gaussian model
popt, pcov = curve_fit(two_gaussian, r_Ar, V_Ar,
                       p0=(-29.288, 8.291, 0.208, 0.304), maxfev=5000)

# Plot the data and the fitted curve
plt.figure(figsize=(8, 6))
plt.plot(r_Ar, V_Ar, 'r-', label='LJ Potential for Argon')
plt.plot(r_Ar, two_gaussian(r_Ar, *popt), 'b--',
         label='Fitted Two-Gaussian Model')
plt.plot(r_Ar, two_gaussian(r_Ar, -29.288, 8.291, 0.208, 0.304),
         'g-', label='Fitted Two-Gaussian Model*', linewidth=2)


plt.plot(r_sim, e_sim, 'g-x', label='two-bead in simulation: h=0.1')
plt.plot(r_sim2, e_sim2, 'y-+', label='two-bead in simulation2: h=0.067')
plt.plot(r_sim3, e_sim3, 'm-1', label='two-bead in simulation3: h=0.058')


plt.title('Fitting Lennard-Jones Potential with Two-Gaussian Model')
plt.ylabel('Potential Energy (kJ/mol)')
plt.legend()


# Add labels for fitted parameters
plt.text(0.8, 4.5, rf'$a_{{G1}} = {popt[0]:.3f}$', fontsize=12, color='blue')
plt.text(0.8, 4, rf'$a_{{G2}} = {popt[1]:.3f}$', fontsize=12, color='blue')
plt.text(
    0.8, 3.5, rf'$\sigma_{{G1}} = {popt[2]:.3f}$', fontsize=12, color='blue')
plt.text(
    0.8, 3, rf'$\sigma_{{G2}} = {popt[3]:.3f}$', fontsize=12, color='blue')


# Add labels for fitted parameters
popt0 = (-29.288, 8.291, 0.208, 0.304)
plt.text(0.5, 4.5, rf'$a_{{G1}} = {popt0[0]:.3f}$', fontsize=12, color='green')
plt.text(0.5, 4, rf'$a_{{G2}} = {popt0[1]:.3f}$', fontsize=12, color='green')
plt.text(
    0.5, 3.5, rf'$\sigma_{{G1}} = {popt0[2]:.3f}$', fontsize=12, color='green')
plt.text(
    0.5, 3, rf'$\sigma_{{G2}} = {popt0[3]:.3f}$', fontsize=12, color='green')


plt.text(
    0.32, 9, r'$V_G^G(r) = -a_{G1} e^{-(r/\sigma_{G1})^2} - a_{G2} e^{-(r/\sigma_{G2})^2}$', fontsize=12, color='black')


# Modify x-axis labels to include reduced units in another row
plt.xticks(np.arange(0.3, 1.1, 0.1), [
           f"{d:.1f}\n{d/0.3405:.2f}" for d in np.arange(0.3, 1.1, 0.1)])
plt.xlabel('Distance (nm) / Reduced Distance')

plt.grid(True)
plt.savefig('fit_with_simulation.pdf')

# Print the fitted parameters
print("Fitted Parameters:")
print("a_G1 =", popt[0])
print("a_G2 =", popt[1])
print("sigma_G1 =", popt[2])
print("sigma_G2 =", popt[3])
