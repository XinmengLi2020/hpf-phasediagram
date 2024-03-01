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
distances = np.arange(0.3, 1.0, 0.02)
for i, distance in enumerate(distances):
    folder_name = f"distance_{distance:.2f}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    out_path = os.path.join(folder_name, f"d_{distance:.2f}.hdf5")
    setup_system([10.0, 10.0, 10.0], distance, out_path)
    print(f"Input file generated for distance {distance:.1f} nm: {out_path}")

