import os
import shutil

user_path = '/home/tntech.edu/yourusername/path_to_dir/'
path = user_path + 'color'
train_path = user_path + 'color_train/'
test_path = user_path + 'color_test/'
index = 0

files = os.listdir(path)
for file in files:
	images = os.listdir(os.path.join(path, file))
	index = 0
	for image in images:
		if index < 2000:
			shutil.copy2(os.path.join(os.path.join(path,file),image), train_path+str(file)+str(index)+'.jpg')
			print str(image) + ' to ' + str(file) + str(index) + '.jpg'
		else:
			shutil.copy2(os.path.join(os.path.join(path,file),image), test_path+str(file)+str(index)+'.jpg')
			print str(image) + ' to ' + str(file) + str(index) + '.jpg'			
		index += 1
