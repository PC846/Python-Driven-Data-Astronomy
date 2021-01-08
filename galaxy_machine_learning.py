#Last lesson completed!

import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from support_functions import generate_features_targets, plot_confusion_matrix, calculate_accuracy


def splitdata_train_test(data, fraction_training):
  np.random.shuffle(data)
  
  split = int(fraction_training * len(data))
  
  return data[:split], data[split:]

def calculate_accuracy(predicted, actual):
  return(sum(predicted == actual) / len(actual))

def generate_features_targets(data):


  targets = data['class']

  features = np.empty(shape=(len(data), 13))
  features[:, 0] = data['u-g']
  features[:, 1] = data['g-r']
  features[:, 2] = data['r-i']
  features[:, 3] = data['i-z'] #COLORS
  features[:, 4] = data['ecc'] # ECC
  features[:, 5] = data['m4_u']
  features[:, 6] = data['m4_g']
  features[:, 7] = data['m4_r']
  features[:, 8] = data['m4_i']
  features[:, 9] = data['m4_z'] # 4TH ADAPTIVE MOVEMENTS


  # concentration in u filter
  features[:, 10] = data['petroR50_u'] / data['petroR90_u']
  # concentration in r filter
  features[:, 11] = data['petroR50_r']/ data['petroR90_r']
  # concentration in z filter
  features[:, 12] = data['petroR50_z'] / data['petroR90_z']

  return features, targets

def dtc_predict_actual(data):
  # split the data into training and testing sets using a training fraction of 0.7
    training, testing = splitdata_train_test(data, 0.7)
  # generate the feature and targets for the training and test sets
  # i.e. train_features, train_targets, test_features, test_targets
    train_features, train_targets = generate_features_targets(training)
    test_features, test_targets =  generate_features_targets(testing)


  # instantiate decision tree classifier
    dtc = DecisionTreeClassifier()

  # train the classifier with the train_features and train_targets
    dtc.fit(train_features, train_targets)
  # get predictions for the test_features
    predictions = dtc.predict(test_features)
  # return the predictions and the test_targets
    return(predictions, test_targets)


def rf_predict_actual(data, n_estimators):
  # generate the features and targets
  features, targets = generate_features_targets(data)

  # instantiate a random forest classifier
  rfc = RandomForestClassifier(n_estimators=n_estimators)
  
  # get predictions using 10-fold cross validation with cross_val_predict
  predicted = cross_val_predict(rfc, features, targets, cv=10)

  # return the predictions and their actual classes
  return predicted, targets

  if __name__ == "__main__":
  data = np.load('galaxy_catalogue.npy')

  features, targets = generate_features_targets(data)

  # Print the shape of each array to check the arrays are the correct dimensions. 
  print("Features shape:", features.shape)
  print("Targets shape:", targets.shape)

  # fraction of data which should be in the training set
  fraction_training = 0.7

  # split the data using your function
  training, testing = splitdata_train_test(data, fraction_training)

  # print the key values
  print('Number data galaxies:', len(data))
  print('Train fraction:', fraction_training)
  print('Number of galaxies in training set:', len(training))
  print('Number of galaxies in testing set:', len(testing))


  predicted_class, actual_class = dtc_predict_actual(data)

  # Print some of the initial results
  print("Some initial results...\n   predicted,  actual")
  for i in range(10):
    print("{}. {}, {}".format(i, predicted_class[i], actual_class[i]))

# get the predicted and actual classes
  number_estimators = 50              # Number of trees
  predicted, actual = rf_predict_actual(data, number_estimators)

  # calculate the model score using your function
  accuracy = calculate_accuracy(predicted, actual)
  print("Accuracy score:", accuracy)