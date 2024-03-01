#!/bin/bash

# Loop through all folders
for folder in distance_*; do
    echo "Processing files in folder: $folder"
    
    # Construct the HDF5 file name based on the folder name
    input_h5="$folder/d_$(basename "$folder" | cut -d'_' -f2).hdf5"
    input_h5_name="$(basename "$input_h5")"
    
    echo "Found HDF5 file: $input_h5"
    echo "Found HDF5 file name : $input_h5_name"

    # Generate SLURM script
    slurm_script="$folder/run.slurm"
    slurm_script_name=run.slurm
    cp simple.slurm "$slurm_script"
    echo "srun python -m hymd ../options.toml $input_h5_name -p ../topol.toml" >> "$slurm_script"
    echo "exit 0" >> "$slurm_script"

    # Submit SLURM job
    cd "$folder"
     ls -a $slurm_script_name
    #sbatch "$slurm_script_name"
    cd ..
    
    echo "Submitted SLURM job for file: $input_h5"

    #sleep 5
done


