import cv2                 
import numpy as np         
import os                  
from random import shuffle 
from tqdm import tqdm
from tensorflow.python.framework import ops
# Visualize training history
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt






TRAIN_DIR = 'C:\\Users\\sredd\\OneDrive\\Desktop\\covid\\train'
TEST_DIR = 'C:\\Users\\sredd\\OneDrive\\Desktop\\covid\\test'

IMG_SIZE = 50
LR = 1e-3
MODEL_NAME = 'healthyvsunhealthynew-{}-{}.model'.format(LR, '2conv-basic')

##
##if K.image_data_format() == 'channels_first':
##    shape = (3, IMG_SIZE, IMG_SIZE)
##else:
##    shape = (IMG_SIZE, IMG_SIZE, 3)
##
##    
def label_img(img):
    word_label = img[0]
    print(word_label)
  
    if word_label == 'c':
        print('COVID')
        return [1,0,0]   
    elif word_label == 'p':
        print(' Viral Pneumonia')
        return [0,1,0]
    elif word_label == 'n':
        print('Normal ')
        return [0,0,1]
##    elif word_label == 'n':
##        print('0.0.Normal')
##        return [0,0,0,1]
##    elif word_label == 'm':
##        print('leafmold')
##        return [0,0,0,0,1,0]
##    elif word_label == 'x':
##        print('leafmold')
##        return [0,0,0,0,0,1]    

def create_train_data():
    training_data = []
    for img in tqdm(os.listdir(TRAIN_DIR)):
        label = label_img(img)
        print('##############')
        print(label)
        path = os.path.join(TRAIN_DIR,img)
        img = cv2.imread(path,cv2.IMREAD_COLOR)
        img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
        #img = cv2.resize(img,None,fx=0.5,fy=0.5)
        training_data.append([np.array(img),np.array(label)])
    shuffle(training_data)
    np.save('train_data.npy', training_data)
    return training_data

def process_test_data():
    testing_data = []
    for img in tqdm(os.listdir(TEST_DIR)):
        path = os.path.join(TEST_DIR,img)
        img_num = img.split('.')[0]
        img = cv2.imread(path,cv2.IMREAD_COLOR)
        img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
        testing_data.append([np.array(img), img_num])
        
    shuffle(testing_data)
    np.save('test_data.npy', testing_data)
    return testing_data

train_data = create_train_data()
# If you have already created the dataset:
#train_data = np.load('train_data.npy')


import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import tensorflow as tf
from tensorflow.python.framework import ops
#tf.reset_default_graph()
ops.reset_default_graph()

convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 3], name='input')

convnet = conv_2d(convnet, 32, 3, activation='relu')
convnet = max_pool_2d(convnet, 3)

convnet = conv_2d(convnet, 64, 3, activation='relu')
convnet = max_pool_2d(convnet, 3)

convnet = conv_2d(convnet, 128, 3, activation='relu')
convnet = max_pool_2d(convnet, 3)

convnet = conv_2d(convnet, 32, 3, activation='relu')
convnet = max_pool_2d(convnet, 3)

convnet = conv_2d(convnet, 64, 3, activation='relu')
convnet = max_pool_2d(convnet, 3)

convnet = fully_connected(convnet, 1024, activation='relu')
convnet = dropout(convnet, 0.8)

convnet = fully_connected(convnet, 3, activation='softmax')
convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

model = tflearn.DNN(convnet, tensorboard_dir='log')

if os.path.exists('{}.meta'.format(MODEL_NAME)):
    model.load(MODEL_NAME)
    print('model loaded!')

train = train_data[:-200]
test = train_data[-200:]

X = np.array([i[0] for i in train]).reshape(-1,IMG_SIZE,IMG_SIZE,3)
Y = [i[1] for i in train]
print(X.shape)
test_x = np.array([i[0] for i in test]).reshape(-1,IMG_SIZE,IMG_SIZE,3)
test_y = [i[1] for i in test]
print(test_x.shape)

history=model.fit({'input': X}, {'targets': Y},n_epoch=100, validation_set=({'input': test_x}, {'targets': test_y}),snapshot_step=30, show_metric=True, run_id=MODEL_NAME)
###graph
##loss_train = history.history['loss']
##loss_val = history.history['val_loss']
##epochs = range(1,35)
##plt.plot(epochs, loss_train, 'g', label='Training loss')
##plt.plot(epochs, loss_val, 'b', label='validation loss')
##plt.title('Training and Validation loss')
##plt.xlabel('Epochs')
##plt.ylabel('Loss')
##plt.legend()
##plt.show()
##
##
##history.history.keys()
### summarize history for accuracy
##plt.plot(history.history['accuracy'])
##plt.plot(history.history['val_accuracy'])
##plt.title('model accuracy')
##plt.ylabel('accuracy')
##plt.xlabel('epoch')
##plt.legend(['train', 'test'], loc='upper left')
##plt.show()
### summarize history for loss
##plt.plot(history.history['loss'])
##plt.plot(history.history['val_loss'])
##plt.title('model loss')
##plt.ylabel('loss')
##plt.xlabel('epoch')
##plt.legend(['train', 'test'], loc='upper left')
##plt.show()

model.save(MODEL_NAME)










        
