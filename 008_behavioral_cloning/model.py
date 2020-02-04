from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Conv2D, Dropout, Cropping2D, Dropout


def network_1(loss='mse', optimizer='adam'):
  model = Sequential()
  model.add(
    Cropping2D(cropping=((60, 30), (0, 0)),
               input_shape=(160, 320, 3),
               data_format="channels_last"))
  #model.add(Cropping2D(cropping = ((70, 25), (0, 0)), input_shape = (160, 320, 3)))
  model.add(Lambda(lambda x: (x / 127.5) - 1., input_shape=(70, 160, 3)))
  model.add(Conv2D(filters=24, kernel_size=5, strides=(2, 2),
                   activation='relu'))
  model.add(Conv2D(filters=36, kernel_size=5, strides=(2, 2),
                   activation='relu'))
  model.add(Conv2D(filters=48, kernel_size=5, strides=(2, 2),
                   activation='relu'))
  model.add(Conv2D(filters=64, kernel_size=3, strides=(1, 1),
                   activation='relu'))
  model.add(Conv2D(filters=64, kernel_size=3, strides=(1, 1),
                   activation='relu'))
  model.add(Flatten())
  model.add(Dense(100, activation='relu'))
  model.add(Dense(50, activation='relu'))
  model.add(Dense(10, activation='relu'))
  model.add(Dense(1))
  model.compile(loss=loss, optimizer=optimizer)

  return model


def network(loss='mse', optimizer='adam'):
  model = Sequential()
  model.add(
    Cropping2D(cropping=((60, 30), (0, 0)),
               input_shape=(160, 320, 3),
               data_format="channels_last"))
  #model.add(Cropping2D(cropping = ((70, 25), (0, 0)), input_shape = (160, 320, 3)))
  model.add(Lambda(lambda x: (x / 127.5) - 1., input_shape=(70, 160, 3)))
  model.add(Conv2D(filters=24, kernel_size=5, strides=(2, 2),
                   activation='relu'))
  model.add(Conv2D(filters=36, kernel_size=5, strides=(2, 2),
                   activation='relu'))
  model.add(Conv2D(filters=48, kernel_size=5, strides=(2, 2),
                   activation='relu'))
  model.add(Conv2D(filters=64, kernel_size=3, strides=(1, 1),
                   activation='relu'))
  model.add(Conv2D(filters=64, kernel_size=3, strides=(1, 1),
                   activation='relu'))
  model.add(Flatten())
  model.add(Dense(100, activation='relu'))
  model.add(Dropout(.5))
  model.add(Dense(50, activation='relu'))
  model.add(Dense(10, activation='relu'))
  model.add(Dropout(.5))
  model.add(Dense(1))
  model.compile(loss=loss, optimizer=optimizer)
  model.summary()
  return model
