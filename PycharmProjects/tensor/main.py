# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tensorflow as tf
import tf.contrib.keras


def mypredict():
    model = keras.Sequential ([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')

    xs = np.array([-1.0, 0.0, 2.0, 3.0, 4.0], dtype=float)
    ys = np.array([-3.0, -1.0, 2.0, 3.0, 4.0], dtype=float)

    model.fit(xs, ys, epochs=500)
    print (model.predict([10.0]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mypredict()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
