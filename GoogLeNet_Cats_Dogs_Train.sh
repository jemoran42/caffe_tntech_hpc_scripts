#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=56000


module load caffe
hostname

echo 'Training'
caffe train --solver=/home/tntech.edu/yourusername/Caffe/caffe/models/bvlc_googlenet/quick_solver.prototxt --weights=/home/tntech.edu/yourusername/Caffe/caffe/models/bvlc_googlenet/bvlc_googlenet.caffemodel -gpu=0

echo 'Done'
