from CNN import CNN
from metrics import *
from data_import import *
from processing import *
from augmentation import *

# 10 classes in our case for 10 leaves
categories = ['acer_campestre', 'acer_palmatum', 'acer_saccharum']  # 'castanea_dentata', 'eucommia_ulmoides',
# 'ginkgo_biloba', 'gleditsia_triacanthos', 'liquidambar_styraciflua', 'salix_babylonica',
# 'ulmus_americana']

## DEBUG code: trying to run on ASL sign language for testing purpose
# alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Img_Size = [100, 100]  # [width, height]


def main():
    """
    This is the wrapper function which calls and generates data from other classes and helper functions
    :return: does specifically return anything.
    """

    # get current and data directories (train and test)
    di = DataImport(__file__)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(current_dir)

    os.chdir("../data/dataset/images")
    # os.chdir("../../Research/ASL-Sign-Language-Classification/data")
    parent_path = os.getcwd()
    print(parent_path)

    os.chdir("temp")
    temp_path = os.getcwd()
    print(temp_path)

    os.chdir("../processed")
    data_path = os.getcwd()
    train_data_dir = data_path + "/training_data"
    test_data_dir = data_path + "/test_data"

    os.chdir("../../../..")
    plot_path = os.getcwd() + "/plots/PART G-changing_initialization"
    # train_data_dir = data_path + "/asl_alphabet_train"
    # test_data_dir = data_path + "/asl_alphabet_test"
    print(train_data_dir, test_data_dir, plot_path)

    # create an object of dataImport and use it to create training and testing data along with their associated labels
    colormap = "BGR2GRAY"
    train_matrix, train_labels = di.create_training_data(categories, train_data_dir, colormap)
    test_matrix, test_labels = di.create_testing_data(categories, test_data_dir, colormap)

    # resize images with the earlier defined size and pass in the matrices to be resized
    proc = Processing()
    train_matrix = proc.resize_images(Img_Size[0], Img_Size[1], train_matrix, colormap, temp_path)
    test_matrix = proc.resize_images(Img_Size[0], Img_Size[1], test_matrix, colormap, temp_path)

    # convert data to numpy array
    aug = Augmentation()
    train_data = aug.create_numpy_data(train_matrix)
    test_data = aug.create_numpy_data(test_matrix)
    print('data shape:', type(train_data.shape))

    # reshaping the images in order to make it ready for convolution
    input_shape, train_data, __, _ = aug.data_reshape(train_data, train_labels, colormap, 1)
    ___, test_data, classes, nClasses = aug.data_reshape(test_data, test_labels, colormap, 1)
    print(input_shape)

    print(test_data, classes, nClasses)
    # scaling data
    train_data = proc.scale_images(train_data, 255)
    test_data = proc.scale_images(test_data, 255)

    # one hot encoding labels
    train_labels, test_labels = aug.one_hot_encode_labels(train_labels, test_labels)
    print(train_labels)

    # create an object of CNN for modelling the data
    cnn = CNN(train_matrix, train_labels, test_matrix, test_labels)

    # create CNN model. we have 32 filters in each layer, with activation function as sigmoid, along with filter size as
    layer_activation = "RELU"
    final_activation = "SOFTMAX"
    kernel_initializer = "RAND_UNIF"
    filters_list = [64, 256, 128]
    filter_size_list = [3, 5, 3]
    pooling_list = [3, 5, 3]
    model = cnn.create_model(input_shape, final_activation=final_activation, layer_activation=layer_activation,
                             conv_layers=3, dense_layers=1, no_of_filters=filters_list, filter_size=filter_size_list,
                             pool_size=pooling_list, final_dense_neurons=3, kernel_initializer=kernel_initializer)

    # compile model with setting these hyper parameters
    alpha = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    model = cnn.compile_model(model=model, loss="CAT_CROSSENTROPY", optimizer="ADAM",
                              metrics=['accuracy', 'mse'], alpha=alpha[3])

    # fit model and generate history
    epochs_list = [3, 5, 7, 10, 15]
    accuracy_list = list()
    metric = Metrics(plot_path)  # setting the metrics object

    for i in range(len(epochs_list)):
        validation_data = (test_data, test_labels)
        history = cnn.fit_model(model=model, train_data=train_data, train_labels=train_labels, batch_size=10,
                                epochs=epochs_list[i], verbose=1, validation_data=validation_data)
        print("History", history)

        # find out model scores
        scores = cnn.evaluate_model(model=model, test_data=test_data, test_labels=test_labels)
        print("Scores", scores)

        # find testing accuracy and predicted values
        predicted_values = cnn.predict_using_model(model=model, test_data=test_data, test_labels=test_labels)
        print(predicted_values)

        # ************************** PERFORMANCE EVALUATION USING DIFFERENT METRICS ************************************

        # 1. Getting the model accuracy
        _, __, accuracy = metric.get_accuracy(predicted_values, test_labels)
        accuracy_list.append(accuracy)

        # 2. Getting the MSE
        mse = metric.mean_squared_error(history, True)
        print(mse)

        # 3. Calculating the train vs validation accuracy
        train_acc, val_acc = metric.train_validation_accuracy(history, True)

        # 4. Calculating the train vs validation loss
        train_loss, val_loss = metric.train_validation_loss(history, True)
        print(train_acc, val_acc, train_loss, val_loss)

        # 5. Get the confusion matrix to understand miss-classification and true classification results
        metric.confusion(test_labels.argmax(axis=1), predicted_values.round().argmax(axis=1), True)

        # # 6. Get the AUC score and the ROC curve along with TPR and FPR
        # auc, fpr, tpr = metric.auc_roc(original, predicted, True)
        # print("AUC: {}, FPR: {}, TPR: {}".format(auc, fpr, tpr))

        # 7. Getting the precision and recall scores
        # precision, recall = metric.precision_recall(test_labels, predicted, True)

    # metric.effect_of_epochs(epochs_list, accuracy_list, True)

    # ******************************************************************************************************************


if __name__ == '__main__':
    main()
