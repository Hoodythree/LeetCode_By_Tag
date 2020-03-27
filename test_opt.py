import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2
from PIL import Image
import os
from keras.utils import to_categorical


height = 30
width = 30
channels = 3
classes = 43
n_inputs = height * width*channels
# 数据预处理
# 转化为numpy array
def get_data():
    data=[]
    labels=[]

    for i in range(classes) :
        path = 'project/input/Train/{0}/'.format(i)
        print(path)
        Class=os.listdir(path)
        for a in Class:
            try:
                image=cv2.imread(path+a)
                image_from_array = Image.fromarray(image, 'RGB')
                size_image = image_from_array.resize((height, width))
                data.append(np.array(size_image))
                labels.append(i)
            except AttributeError:
                print(" ")

    Cells=np.array(data)
    labels=np.array(labels)

    #Randomize the order of the input images
    s=np.arange(Cells.shape[0])
    np.random.seed(43)
    np.random.shuffle(s)
    Cells=Cells[s]
    labels=labels[s]

    #Spliting the images into train and validation sets
    (X_train,X_val)=Cells[(int)(0.2*len(labels)):],Cells[:(int)(0.2*len(labels))]
    X_train = X_train.astype('float32')/255 
    X_val = X_val.astype('float32')/255
    (y_train,y_val)=labels[(int)(0.2*len(labels)):],labels[:(int)(0.2*len(labels))]

    #Using one hote encoding for the train and validation labels
    y_train = to_categorical(y_train, 43)
    y_val = to_categorical(y_val, 43)


    #Predicting with the test data
    y_test=pd.read_csv("project/input/Test.csv")
    labels=y_test['Path'].as_matrix()
    y_test=y_test['ClassId'].values

    data2=[]

    for f in labels:
        image=cv2.imread('project/input/test/'+f.replace('Test/', ''))
        image_from_array = Image.fromarray(image, 'RGB')
        size_image = image_from_array.resize((height, width))
        data2.append(np.array(size_image))

    X_test=np.array(data2)
    X_test = X_test.astype('float32')/255 
# pred = model.predict_classes(X_test)
    return X_train, y_train, X_test, y_test



from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout, Activation

# model = Sequential()
# model.add(Conv2D(filters=32, kernel_size=(5,5), activation='relu', input_shape=X_train.shape[1:]))
# model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
# model.add(MaxPool2D(pool_size=(2, 2)))
# model.add(Dropout(rate=0.25))
# model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
# model.add(MaxPool2D(pool_size=(2, 2)))
# model.add(Dropout(rate=0.25))
# model.add(Flatten())
# model.add(Dense(256, activation='relu'))
# model.add(Dropout(rate=0.5))
# model.add(Dense(43, activation='softmax'))

model = Sequential()
model.add(Dense(512, input_shape=X_train.shape[1:]))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(43))
model.add(Activation('softmax'))



#Compilation of the model
model.compile(
    loss='categorical_crossentropy', 
    optimizer='adam', 
    metrics=['accuracy']
)


#using ten epochs for the training and saving the accuracy for each epoch
epochs = 20
history = model.fit(X_train, y_train, batch_size=32, epochs=epochs,
validation_data=(X_val, y_val))




#Display of the accuracy and the loss values
# import matplotlib.pyplot as plt

# plt.figure(0)
# plt.plot(history.history['acc'], label='training accuracy')
# plt.plot(history.history['val_acc'], label='val accuracy')
# plt.title('Accuracy')
# plt.xlabel('epochs')
# plt.ylabel('accuracy')
# plt.legend()
# plt.savefig('test.png')

# plt.figure(1)
# plt.plot(history.history['loss'], label='training loss')
# plt.plot(history.history['val_loss'], label='val loss')
# plt.title('Loss')
# plt.xlabel('epochs')
# plt.ylabel('loss')
# plt.legend()
