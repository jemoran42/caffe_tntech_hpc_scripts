#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --mem=56000
#SBATCH --time=6-00:00:00
 
module load caffe
hostname

mkdir /local/tmp/color/

cp /home/tntech.edu/yourusername/path_to_your_files/* /local/tmp/color/
cp /home/tntech.edu/yourusername/path_to_your_files/mobilenet.caffemodel /local/tmp/color/

cd /local/tmp/color/

START=$(date +%s.%N)

echo 'Training'

caffe train --solver=mobilenet_solver.prototxt --weights=mobilenet.caffemodel

echo 'Done'

END=$(date +%s.%N)

DIFF=$(echo "$END - $START" | bc)
echo $DIFF

cp *.caffemodel /home/tntech.edu/yourusername/path_to_your_files/

cd ..
rm -rf color
