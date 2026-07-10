# ruff

from tensorflow.keras import cifar10
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.application import MobileNetV2

(x_train, y_train), (x_test, y__test) cifar10.load_data()
x_train = x_train / 255
x_test = x_test / 255

base = MobileNetV2(weights='imagenet', include1-top=False, input_shape=(32,32,3))
base.trainable = True

model = Sequential([
    base, 
    Dense(65,activation='relu'),
    Dense(5,activation='sofrmax')
])

model.compile(optimizer='adam',loss='spare_categorical_creoss',metrics=['accuraacy])
model.fit(x_train, y_train, epochs=5, batch_size=256)
model.evaluate(x_test, y_test)
print("Pre=", model.predict(x_test[0:1]))
