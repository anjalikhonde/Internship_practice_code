import tensorflow as tf

import numpy as np

#----------------------------------------------
#training data
#----------------------------------------------

#study houre,attendance,assignment,internal marks

x=np.array([
    [2,60,40,35],
    [3,65,45,40],
    [4,70,55,50],
    [5,75,60,60],
    [6,80,70,65],
    [7,85,80,75],
    [8,90,85,80],
    [9,95,90,90]
],dtype=float)

#result 
#0=fail
#1=pass

y=np.array([
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1
])

#----------------------------------------------
#normalize data
#----------------------------------------------

x=x/np.max(x,axis=0)

#----------------------------------------------
#build ann model
#-----------------------------------------------

model=tf.keras.Sequential()

model.add(tf.keras.layers.Dense(8,activation='relu',input_shape=(4,)))

model.add(tf.keras.layers.Dense(4,activation='relu'))

model.add(tf.keras.layers.Dense(1,activation='sigmoid'))

#--------------------------------------------------
#compile model
#--------------------------------------------------

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

#--------------------------------------------------
#train model
#--------------------------------------------------

model.fit(x,y,epochs=100,verbose=1)

#test new student

study=float(input("Enter study hours:"))
attendance=float(input("Enter attendance:"))
assignment=float(input("enter assignment marks:"))
internal=float(input("enter internal marks:"))

new_student=np.array([[study,attendance,assignment,internal]])

new_student=new_student/np.max(x,axis=0)

prediction=model.predict(new_student)

print("prediction:",prediction)

if prediction>0.5:
    print("Student will pass")
else:
    print("Student will fail")