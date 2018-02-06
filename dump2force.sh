#!/bin/bash
#PBS -l select=1:ncpus=16:mpiprocs=16:mem=8gb

# Edit your Walltime hours
#PBS -l walltime=12:00:00
#PBS -k oe

# Edit your email address or delete these two lines
#PBS -N D2F_4-6.3_on_8-11_mm
#PBS -M deside.chibwe@uon.edu.au
#PBS -m bae

# Edit where my simulation is and the name of the file
SIMDIR="/home/c3217954/PhD_Work/FT_Charging_System/Coke_Discharge/Binary/4-6.3_on_8-11_mm/post"

source /etc/profile.d/modules.sh  
module load python/3.5.3

export OMP_NUM_THREADS=$NCPUS

cd $SIMDIR

for file in `ls *.forcechains`

do 

basename=`echo $file | sed 's/\.[^.]*$//'`
extname=`echo $file | sed 's/[^0-9]*\([0-9]*\)\.\(.*\)/\2\1/'`

echo "Processing file: "$basename

python $HOME/convert.py $basename.forcechains >  $extname.vtk

done

exit 0
