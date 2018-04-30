from random import shuffle
import glob
import cv2
shuffle_data = True  # shuffle the addresses before saving
hdf5_train1_path = '/home/tntech.edu/jemoran42/Caffe/All_Networks/Datasets/make/train1.h5'  # address to where you want to save the hdf5 file
hdf5_train2_path = '/home/tntech.edu/jemoran42/Caffe/All_Networks/Datasets/make/train2.h5'  # address to where you want to save the hdf5 file
car_train_path = '/home/tntech.edu/jemoran42/Caffe/Cars/Make_of_Cars/*.jpg'
hdf5_test_path = '/home/tntech.edu/jemoran42/Caffe/All_Networks/Datasets/make/test.h5'

# read addresses and labels from the 'train' folder
addrs = glob.glob(car_train_path)

i= -1
labels = []
for addr in addrs:
	i = i + 1
	labels.append(i)
	if 'Audi' in addr:
		labels[i] = 0
	elif 'BMW' in addr:
		labels[i] = 1
	elif 'Buick' in addr:
		labels[i] = 2
	elif 'Chevrolet' in addr:
		labels[i] = 3
	elif 'Dodge' in addr:
		labels[i] = 4
	elif 'Ford' in addr:
		labels[i] = 5
	elif 'GMC' in addr:
		labels[i] = 6
	elif 'Honda' in addr:
		labels[i] = 7
	elif 'Infiniti' in addr:
		labels[i] = 8
	elif 'Jeep' in addr:
		labels[i] = 9
	elif 'Kia' in addr:
		labels[i] = 10
	elif 'Lexus' in addr:
		labels[i] = 11
	elif 'Lincoln' in addr:
		labels[i] = 12
	elif 'Mazda' in addr:
		labels[i] = 13
	elif 'Mercedes-benz' in addr:
		labels[i] = 14
	elif 'Nissan' in addr:
		labels[i] = 15
	elif 'Porsche' in addr:
		labels[i] = 16
	elif 'Toyota' in addr:
		labels[i] = 17
	elif 'Volkswagen' in addr:
		labels[i] = 18
	elif 'Volvo' in addr:
		labels[i] = 19
	


# to shuffle data
if shuffle_data:
    c = list(zip(addrs, labels))
    shuffle(c)
    addrs, labels = zip(*c)
    
train1_addrs = addrs[0:int(0.5*len(addrs))]
train1_labels = labels[0:int(0.5*len(addrs))]
train2_addrs = addrs[int(0.5*len(addrs)):int(0.9*len(addrs))]
train2_labels = labels[int(0.5*len(addrs)):int(0.9*len(addrs))]
test_addrs = addrs[int(0.9*len(addrs)):int(len(addrs))]
test_labels = labels[int(0.9*len(addrs)):int(len(addrs))]


import numpy as np
import h5py

data_order = 'tf'  # 'th' for Theano, 'tf' for Tensorflow

SIZE = 224
train_shape = (len(train1_addrs), 3, SIZE, SIZE)


# open a hdf5 file and create earrays
hdf5_file = h5py.File(hdf5_train1_path, mode='w')

hdf5_file.create_dataset("data", train_shape, np.int8)

# hdf5_file.create_dataset("train_mean", train_shape[1:], np.float32)

hdf5_file.create_dataset("label", (len(train1_addrs),), np.int8)
hdf5_file["label"][...] = train1_labels

# a numpy array to save the mean of the images
mean = np.zeros(train_shape[1:], np.float32)

# loop over train addresses
for i in range(len(train1_addrs)):
    # print how many images are saved every 1000 images
    if i % 1000 == 0 and i > 1:
        print 'Train1 data: {}/{}'.format(i, len(train1_addrs))

    # read an image and resize to (SIZE, SIZE)
    # cv2 load images as BGR, convert it to RGB
    addr = train1_addrs[i]
    # print addr
    img = cv2.imread(addr)
    if img is not None:	
		img = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_CUBIC)
		# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

		# add any image pre-processing here

		img = np.rollaxis(img, 2)

		# save the image and calculate the mean so far
		hdf5_file["data"][i, ...] = img[None]
		mean += img / float(len(train1_labels))


# save the mean and close the hdf5 file
# hdf5_file["train_mean"][...] = mean
hdf5_file.close()

train_shape = (len(train2_addrs), 3, SIZE, SIZE)

# open a hdf5 file and create earrays
hdf5_file = h5py.File(hdf5_train2_path, mode='w')

hdf5_file.create_dataset("data", train_shape, np.int8)

# hdf5_file.create_dataset("train_mean", train_shape[1:], np.float32)

hdf5_file.create_dataset("label", (len(train2_addrs),), np.int8)
hdf5_file["label"][...] = train2_labels

# a numpy array to save the mean of the images
mean = np.zeros(train_shape[1:], np.float32)

# loop over train addresses
for i in range(len(train2_addrs)):
    # print how many images are saved every 1000 images
    if i % 1000 == 0 and i > 1:
        print 'Train2 data: {}/{}'.format(i, len(train2_addrs))

    # read an image and resize to (SIZE, SIZE)
    # cv2 load images as BGR, convert it to RGB
    addr = train2_addrs[i]
    img = cv2.imread(addr)
    if img is not None:	
		img = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_CUBIC)
		# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

		# add any image pre-processing here

		img = np.rollaxis(img, 2)

		# save the image and calculate the mean so far
		hdf5_file["data"][i, ...] = img[None]
		mean += img / float(len(train2_labels))


# save the mean and close the hdf5 file
# hdf5_file["train_mean"][...] = mean
hdf5_file.close()


test_shape = (len(test_addrs), 3, SIZE, SIZE)


# open a hdf5 file and create earrays
hdf5_file = h5py.File(hdf5_test_path, mode='w')

hdf5_file.create_dataset("data", test_shape, np.int8)

# hdf5_file.create_dataset("train_mean", train_shape[1:], np.float32)

hdf5_file.create_dataset("label", (len(test_addrs),), np.int8)
hdf5_file["label"][...] = test_labels

# a numpy array to save the mean of the images
mean = np.zeros(test_shape[1:], np.float32)

# loop over train addresses
for i in range(len(test_addrs)):
    # print how many images are saved every 1000 images
    if i % 100 == 0 and i > 1:
        print 'Test data: {}/{}'.format(i, len(test_addrs))

    # read an image and resize to (SIZE, SIZE)
    # cv2 load images as BGR, convert it to RGB
    addr = test_addrs[i]
    img = cv2.imread(addr)
    if img is not None:
		img = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_CUBIC)
		# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

		# add any image pre-processing here

		img = np.rollaxis(img, 2)

		# save the image and calculate the mean so far
		hdf5_file["data"][i, ...] = img[None]
		mean += img / float(len(test_labels))


# save the mean and close the hdf5 file
# hdf5_file["train_mean"][...] = mean
hdf5_file.close()