#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --mem=56000
#SBATCH --time=6-00:00:00
 
module load caffe
hostname

mkdir /local/tmp/jem_color/

cp /home/tntech.edu/jemoran42/Caffe/Cars/color/* /local/tmp/jem_color/
cp /home/tntech.edu/jemoran42/Caffe/Cars/color/Caffe_Output/mobilenet.caffemodel /local/tmp/jem_color/

cd /local/tmp/jem_color/

START=$(date +%s.%N)

echo 'Training'

caffe train --solver=mobilenet_solver.prototxt --weights=mobilenet.caffemodel

echo 'Done'

END=$(date +%s.%N)

DIFF=$(echo "$END - $START" | bc)
echo $DIFF

cp *.caffemodel /home/tntech.edu/jemoran42/Caffe/Cars/color/Caffe_Output/

cd ..
rm -rf jem_color
