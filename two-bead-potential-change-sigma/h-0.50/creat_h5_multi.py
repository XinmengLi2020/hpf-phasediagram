import h5py
import numpy as np
import os


def setup_system(box_size, particles_distance, out_path):
    """Setup a simple system of independent particles with no bonds

    Parameters
    ----------
    box_size : list of float
        Simulation box size in nm.
    particles_distance : float
        Distance between the two particles in the simulation box.
    out_path : str
        Path of the created structure file.
    """
    box_size = np.asarray(box_size, dtype=np.float32)
    n_particles = 2

    with h5py.File(out_path, "w") as out_file:
        out_file.attrs["box"] = box_size
        out_file.attrs["n_molecules"] = n_particles

        position_dataset = out_file.create_dataset(
            "coordinates",
            (
                1,
                n_particles,
                box_size.size,
            ),
            dtype="float32",
        )
        velocities_dataset = out_file.create_dataset(
            "velocities",
            (
                1,
                n_particles,
                box_size.size,
            ),
            dtype="float32",
        )
        types_dataset = out_file.create_dataset(
            "types",
            (n_particles,),
            dtype="i",
        )
        names_dataset = out_file.create_dataset(
            "names",
            (n_particles,),
            dtype="S5",
        )
        indices_dataset = out_file.create_dataset(
            "indices",
            (n_particles,),
            dtype="i",
        )

        types_dataset[...] = 0
        names_dataset[...] = np.string_("H")
        indices_dataset[...] = np.arange(n_particles)
        position_dataset[0, 0, :] = np.zeros(3)
        position_dataset[0, 1, :] = np.array([particles_distance, 0.0, 0.0])
        velocities_dataset[0, :, :] = np.zeros((n_particles, 3))


# Loop through each distance value and generate the corresponding input file
# distances = np.arange(0.33, 1.0, 0.02)

d_min = 0.30
d_middle = 0.5
d_max = 1.0
d_array = np.arange(d_min, d_middle, 0.01)
d_array = np.append(d_array, np.arange(d_middle, d_max, 0.03))
# d_array = np.append(d_array, d_max)


for i, distance in enumerate(d_array):
    folder_name = f"distance_{distance:.2f}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    out_path = os.path.join(folder_name, f"d_{distance:.2f}.hdf5")
    setup_system([10.0, 10.0, 10.0], distance, out_path)
    print(f"Input file generated for distance {distance:.2f} nm: {out_path}")
