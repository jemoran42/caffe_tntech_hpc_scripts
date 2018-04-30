#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --mem=56000
#SBATCH --time=30-00:00:00
 

TOTAL_START=$(date +%s.%N)

module load caffe
hostname

DIR=/local/tmp/all_nets/
ORIGIN_DIR=/home/tntech.edu/yourusername/path_to_dir/All_Networks/

mkdir $DIR

cp -r $ORIGIN_DIR/* $DIR

cd $DIR/GoogleNet/Color

START=$(date +%s.%N)

echo 'Training'

caffe train --solver=quick_solver.prototxt --weights=$DIR/GoogleNet/Original/bvlc_googlenet.caffemodel

echo 'Done'

END=$(date +%s.%N)

DIFF=$(echo "$END - $START" | bc)
echo $DIFF

cp *.caffemodel $ORIGIN_DIR/GoogleNet/Color/




cd $DIR/GoogleNet/Make/

START=$(date +%s.%N)

echo 'Training'

caffe train --solver=quick_solver.prototxt --weights=$DIR/GoogleNet/Original/bvlc_googlenet.caffemodel

echo 'Done'

END=$(date +%s.%N)

DIFF=$(echo "$END - $START" | bc)
echo $DIFF

cp *.caffemodel $ORIGIN_DIR/GoogleNet/Make/




cd $DIR/GoogleNet/Type

START=$(date +%s.%N)

echo 'Training'

caffe train --solver=quick_solver.prototxt --weights=$DIR/GoogleNet/Original/bvlc_googlenet.caffemodel

echo 'Done'

END=$(date +%s.%N)

DIFF=$(echo "$END - $START" | bc)
echo $DIFF

cp *.caffemodel $ORIGIN_DIR/GoogleNet/Type/




cd $DIR/SqueezeNet/Color

START=$(date +%s.%N)

echo 'Training'

caffe train --solver=solver.prototxt --weights=$DIR/SqueezeNet/Original_v1.1/squeezenet_v1.1.caffemodel

echo 'Done'

END=$(date +%s.%N)

DIFF=$(echo "$END - $START" | bc)
echo $DIFF

cp *.caffemodel $ORIGIN_DIR/SqueezeNet/Color/



cd $DIR/SqueezeNet/Make

START=$(date +%s.%N)

echo 'Training'

caffe train --solver=solver.prototxt --weights=$DIR/SqueezeNet/Original_v1.1/squeezenet_v1.1.caffemodel

echo 'Done'

END=$(date +%s.%N)

DIFF=$(echo "$END - $START" | bc)
echo $DIFF

cp *.caffemodel $ORIGIN_DIR/SqueezeNet/Make/




cd $DIR/SqueezeNet/Type

START=$(date +%s.%N)

echo 'Training'

caffe train --solver=solver.prototxt --weights=$DIR/SqueezeNet/Original_v1.1/squeezenet_v1.1.caffemodel

echo 'Done'

END=$(date +%s.%N)

DIFF=$(echo "$END - $START" | bc)
echo $DIFF

cp *.caffemodel $ORIGIN_DIR/SqueezeNet/Type/





cd $DIR/MobileNet/Color

START=$(date +%s.%N)

echo 'Training'

caffe train --solver=solver.prototxt --weights=$DIR/MobileNet/Original_v1/mobilenet.caffemodel

echo 'Done'

END=$(date +%s.%N)

DIFF=$(echo "$END - $START" | bc)
echo $DIFF

cp *.caffemodel $ORIGIN_DIR/MobileNet/Color/




cd $DIR/MobileNet/Make

START=$(date +%s.%N)

echo 'Training'

caffe train --solver=solver.prototxt --weights=$DIR/MobileNet/Original_v1/mobilenet.caffemodel

echo 'Done'

END=$(date +%s.%N)

DIFF=$(echo "$END - $START" | bc)
echo $DIFF

cp *.caffemodel $ORIGIN_DIR/MobileNet/Make/




cd $DIR/MobileNet/Type

START=$(date +%s.%N)

echo 'Training'

caffe train --solver=solver.prototxt --weights=$DIR/MobileNet/Original_v1/mobilenet.caffemodel

echo 'Done'

END=$(date +%s.%N)

DIFF=$(echo "$END - $START" | bc)
echo $DIFF

cp *.caffemodel $ORIGIN_DIR/MobileNet/Type/



cd $DIR
cd ..
rm -rf $DIR


TOTAL_END=$(date +%s.%N)

TOTAL_DIFF=$(echo "$TOTAL_END - $TOTAL_START" | bc)
echo $TOTAL_DIFF
