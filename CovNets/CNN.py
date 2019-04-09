import tensorflow as tf


class CNN:

    def __init__(self, x_train, y_train, x_test, y_test):
        """

        :param categories:
        :param train_data_dir:
        :param test_data_dir:
        """

        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test

    @staticmethod
    def create_model(input_shape, final_activation, layer_activation, conv_layers, dense_layers, no_of_filters,
                     filter_size, pool_size, final_dense_neurons, kernel_initializer):
        model = tf.keras.Sequential()

        activations_dict = {"RELU": tf.nn.relu,
                            "LEAKY_RELU": tf.nn.leaky_relu,
                            "TANH": tf.nn.tanh,
                            "SOFTMAX": tf.nn.softmax}

        initializer_dict = {"ZEROS": tf.keras.initializers.Zeros,
                            "UNIFORM": tf.keras.initializers.uniform,
                            "RAND_NORM": tf.keras.initializers.random_normal,
                            "RAND_UNIF": tf.keras.initializers.random_uniform}

        for i in range(conv_layers):
            model.add(tf.keras.layers.Conv2D(no_of_filters[i], (filter_size[i], filter_size[i]), input_shape=input_shape,
                                             activation=activations_dict[layer_activation]))
            model.add(tf.keras.layers.MaxPooling2D(pool_size=(pool_size[i], pool_size[i])))
            model.add(tf.keras.layers.Dropout(0.2))

        model.add(tf.keras.layers.Flatten())  # this converts our 3D feature maps to 1D feature vectors

        hidden_units = 64

        for i in range(dense_layers):
            model.add(tf.keras.layers.Dense(hidden_units, kernel_initializer=initializer_dict[kernel_initializer]))
            model.add(tf.keras.layers.BatchNormalization(axis=1))
            model.add(tf.keras.layers.Activation(activations_dict[final_activation]))

        model.add(tf.keras.layers.Dense(final_dense_neurons))
        model.add(tf.keras.layers.Activation(activations_dict[final_activation]))

        return model

    @staticmethod
    def compile_model(model, loss, optimizer, metrics, alpha):
        # metrics_dict = {'mae': tf.keras.metrics.mean_absolute_error,
        #                 'mse': tf.keras.metrics.mean_squared_error,
        #                 'mape': tf.keras.metrics.mean_absolute_percentage_error,
        #                 'ba': tf.keras.metrics.binary_accuracy,
        #                 'ca': tf.keras.metrics.categorical_accuracy,
        #                 'tkca': tf.keras.metrics.top_k_categorical_accuracy,
        #                 'cosine': tf.keras.metrics.cosine_proximity}

        optimizer_dict = {"ADAM": tf.train.AdamOptimizer(learning_rate=alpha),
                          "RMSPROP": tf.train.RMSPropOptimizer(learning_rate=alpha)}

        # loss values function
        lossfunction_dict = {"CAT_CROSSENTROPY": tf.keras.losses.categorical_crossentropy,
                             "KULLBACK_LEIBLER": tf.keras.losses.kullback_leibler_divergence}

        model.compile(loss=lossfunction_dict[loss], optimizer=optimizer_dict[optimizer], metrics=metrics)

        return model

    @staticmethod
    def fit_model(model, train_data, train_labels, batch_size, epochs, verbose, validation_data):
        history = model.fit(train_data, train_labels, batch_size=batch_size, epochs=epochs, verbose=verbose,
                            validation_data=validation_data)

        return history

    @staticmethod
    def evaluate_model(model, test_data, test_labels):
        scores = model.evaluate(test_data, test_labels)

        return scores

    @staticmethod
    def predict_using_model(model, test_data, test_labels):
        ypred = model.predict(x=test_data, verbose=1)

        return ypred
