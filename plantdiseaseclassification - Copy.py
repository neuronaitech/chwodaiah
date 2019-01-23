# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:14:39 2018

@author: Asus
"""
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils
import numpy as np
import os
from PIL import Image
from sklearn.utils import shuffle
#import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
img_rows, img_cols = 200, 200

path1 = r'F:\study materials\test\0'    
path2 = r'F:\study materials'  
listing = os.listdir(path1) 
num_samples=np.size(listing)
print(num_samples)

for file in listing:
    im = Image.open(path1 + '\\' + file)   
    img = im.resize((img_rows,img_cols))
    gray = img.convert('L')
    gray.save(path2 +'\\' +  file, "JPEG")

imlist = os.listdir(path1)

im1 = np.array(Image.open(r'F:\study materials' + '\\'+ imlist[0])) # open one image to get size
m,n = im1.shape[0:2] # get the size of the images
imnbr = len(imlist) # get the number of images

# create matrix to store all flattened images
immatrix = np.array([np.array(Image.open(r'F:\study materials'+ '\\' + im2)).flatten()
              for im2 in imlist],'f')
                
label=np.ones((num_samples,),dtype = int)
label[0:403]=0
label[403:904]=1
label[904:1314]=2
label[1313:1908]=3
label[1908:]=4

data,Label = shuffle(immatrix,label, random_state=2)
train_data = [data,Label]
print (train_data[0].shape)
print (train_data[1].shape)
#batch_size to train
batch_size =64
# number of output classes
nb_classes = 5
# number of epochs to train
nb_epoch = 10
# number of convolutional filters to use
nb_filters = 3
# size of pooling area for max pooling
nb_pool = 1
# convolution kernel size
nb_conv = 1

(X, y) = (train_data[0],train_data[1])
# STEP 1: split X and y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
X_train = X_train.reshape(X_train.shape[0],1 , img_rows, img_cols)
X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train /= 255
X_test /= 255
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)


###########################
model = Sequential()
model.add(Convolution2D(32,1,input_shape=(1, img_rows, img_cols)))
convout1 = Activation('relu')
model.add(convout1)
model.add(Dropout(0.05))
model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
model.add(Dropout(0.05))
model.add(Flatten())
model.add(Dense(50))
model.add(Activation('relu'))
model.add(Dropout(0.05))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])
print (model.summary()) 
hist = model.fit(X_train, Y_train, batch_size=batch_size, epochs=nb_epoch,
              verbose=1, validation_data=(X_test, Y_test))

from keras.preprocessing import image
test_image = image.load_img('F:\\study materials\\test\\0\\1aef6002-435e-42c1-ac33-47b5a07e88b3.JPG')
test_image=test_image.resize((img_rows,img_cols))
test_image= test_image.convert('L')
test_image.show()
test_img =np.array(test_image).reshape(1,1,200,200)
pred_result = model.predict(test_img)
print(pred_result)

test_score = model.evaluate(X_test, Y_test,  verbose=0)
#print("score:",test_score)
#print('Test score:', test_score[0])
print('Test accuracy:', test_score[1])
train_score = model.evaluate(X_train, Y_train,  verbose=0)
#print("score:",train_score)
#print('Train score:', train_score[0])
print('Train accuracy:', train_score[1])

final_res=any(i > 0.3 for i in pred_result[0])
if final_res == True:
     print("THE IMAGE HAVE DISEASE")
else:
     print("THE IMAGE DONT HAVE DISEASE")