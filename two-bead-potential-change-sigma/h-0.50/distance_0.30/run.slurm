#!/bin/bash
#SBATCH --account=nn4654k
#SBATCH --job-name=HhPF-2particles
#SBATCH --time=0-1:0:0
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=64
#SBATCH --cpus-per-task=1
#SBATCH --qos=devel

## Recommended safety settings:
set -o errexit # Make bash exit on any error
set -o nounset # Treat unset variables as errors

# Load modules
module --quiet purge
module load HDF5/1.14.0-gompi-2022b
module load Python/3.10.8-GCCcore-12.2.0

# Load environment
source /cluster/projects/nn4654k/cascella_group/new_mgcm/venv/hymd-lj-branch/bin/activate
module list

###################
# cp -r *.toml $input_h5 $SCRATCH
# cd $SCRATCH
# cleanup cp -r $SCRATCH $SLURM_SUBMIT_DIR

#srun python -m hymd ../options.toml $input_h5 -p ../topol.toml
#exit 0




srun python -m hymd ../options.toml d_0.30.hdf5 -p ../topol.toml
exit 0
