from random import shuffle
import glob
import cv2
shuffle_data = True  # shuffle the addresses before saving
hdf5_path = '/path_to_files/train.h5'  # address to where you want to save the hdf5 file
car_train_path = '/path_to_renamed_car_images/*.jpg'
hdf5_test_path = '/path_to_files/test.h5'

# read addresses and labels from the 'train' folder
addrs = glob.glob(car_train_path)

i= -1
labels = []
for addr in addrs:
	i = i + 1
	labels.append(i)
	if 'Coupe' in addr:
		labels[i] = 0  # 0 = Coupe, 1=Convertible, 2 = Sedan, 3 = Van, 4 = SUV, 5 = Truck, 6 = Wagon, 7 = Hatchback.
	elif 'Convertible' in addr:
		labels[i] = 1
	elif 'Sedan' in addr:
		labels[i] = 2
	elif 'Van' in addr:
		labels[i] = 3
	elif 'SUV' in addr:
		labels[i] = 4
	elif 'Truck' in addr:
		labels[i] = 5
	elif 'Wagon' in addr:
		labels[i] = 6
	elif 'Hatchback' in addr:
		labels[i] = 7
	else:
		labels[i] = 10
		print 'Error at ' + i + 'Failed to label'
		print addr
		exit()


# to shuffle data
if shuffle_data:
    c = list(zip(addrs, labels))
    shuffle(c)
    addrs, labels = zip(*c)
    
train_addrs = addrs[0:int(0.8*len(addrs))]
train_labels = labels[0:int(0.8*len(addrs))]
test_addrs = addrs[int(0.8*len(addrs)):int(len(addrs))]
test_labels = labels[int(0.8*len(addrs)):int(len(addrs))]


import numpy as np
import h5py

data_order = 'tf'  # 'th' for Theano, 'tf' for Tensorflow

SIZE = 224
train_shape = (len(train_addrs), 3, SIZE, SIZE)


# open a hdf5 file and create earrays
hdf5_file = h5py.File(hdf5_path, mode='w')

hdf5_file.create_dataset("data", train_shape, np.int8)

# hdf5_file.create_dataset("train_mean", train_shape[1:], np.float32)

hdf5_file.create_dataset("label", (len(train_addrs),), np.int8)
hdf5_file["label"][...] = train_labels

# a numpy array to save the mean of the images
mean = np.zeros(train_shape[1:], np.float32)

# loop over train addresses
for i in range(len(train_addrs)):
    # print how many images are saved every 1000 images
    if i % 1000 == 0 and i > 1:
        print 'Train data: {}/{}'.format(i, len(train_addrs))

    # read an image and resize to (SIZE, SIZE)
    # cv2 load images as BGR, convert it to RGB
    addr = train_addrs[i]
    img = cv2.imread(addr)
    img = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_CUBIC)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # add any image pre-processing here

    img = np.rollaxis(img, 2)

    # save the image and calculate the mean so far
    hdf5_file["data"][i, ...] = img[None]
    mean += img / float(len(train_labels))


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
    if i % 1000 == 0 and i > 1:
        print 'Test data: {}/{}'.format(i, len(test_addrs))

    # read an image and resize to (SIZE, SIZE)
    # cv2 load images as BGR, convert it to RGB
    addr = test_addrs[i]
    img = cv2.imread(addr)
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
