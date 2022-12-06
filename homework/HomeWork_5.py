import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys
from keras.preprocessing import image
#data 전처리
from keras.preprocessing.image import ImageDataGenerator
import google.colab.drive as drive

from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

#heatmap
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#get data
Train_URL='./drive/MyDrive/2022_2nd_semister/AI_programming/DATA/HW_5/train'
Test_URL='./drive/MyDrive/2022_2nd_semister/AI_programming/DATA/HW_5/test'
drive.mount('/content/drive')

#data scaling
#flip to avoid overfitting
train_data_generator=ImageDataGenerator(rescale=1./255,horizontal_flip=True,vertical_flip=True)
test_data_generator=ImageDataGenerator(rescale=1./255)

#trainset, testset input
#colorization - gray
train_generator=train_data_generator.flow_from_directory(Train_URL,target_size=(256,256),
                                                         batch_size=1,class_mode='categorical'
                                                         ,color_mode='grayscale',shuffle=True,)
test_generator=test_data_generator.flow_from_directory(Test_URL,target_size=(256,256),batch_size=1,class_mode='categorical',shuffle=True,color_mode='grayscale')


#input check
train_generator.next()
print(test_generator.class_indices)

#trainning model
model = Sequential()
model.add(Conv2D(32, kernel_size = (9, 9), input_shape = (256, 256, 1), activation = 'relu',padding="same"))
model.add(Conv2D(64, (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(256, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(3, activation = 'softmax'))
model.summary()
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
modelpath='./drive/MyDrive/2022_2nd_semister/AI_programming/DATA/HW_5_test'
checkpointer = ModelCheckpoint(filepath = modelpath, monitor = 'accuracy', verbose = 1, save_best_only = True)
early_stopping_callback = EarlyStopping(monitor = 'accuracy', patience = 35)
#patience값이 낮으면 학습이 안돼서 큰 값으로 설정
#과적합 방지를 위해서 tool flip과 shuffle을 사용했습니다

history=model.fit(train_generator,epochs=20000,steps_per_epoch=100,
                  shuffle=True,batch_size=100,callbacks = [early_stopping_callback, checkpointer])

y_predict=np.argmax(model.predict(test_generator),axis=-1)

# get lables
real_labels = []
for i in range(114):  #num of test
  x,y=next(test_generator)
  real_labels.append(np.argmax(y,axis=-1))

real_labels=np.array(real_labels)
real_labels=real_labels.reshape(-1)
print(real_labels)
print(y_predict)


confusion_matrix=metrics.confusion_matrix(real_labels,y_predict)
df=pd.DataFrame(confusion_matrix,['adidas','converse','nike'],['adidas','converse','nike'])
colormap = plt.cm.gist_heat
plt.figure(figsize = (10, 10))



# heatmap plotting
sns.heatmap(df, cmap = colormap, annot = True)
plt.show()

