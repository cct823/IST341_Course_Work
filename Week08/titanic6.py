#
#
# titanic.py
#
#

import numpy as np
from sklearn import datasets
import pandas as pd


try: # different imports for different versions of scikit-learn
    from sklearn.model_selection import cross_val_score   # simpler cv this week
except ImportError:
    try:
        from sklearn.cross_validation import cross_val_score
    except:
        print("No cross_val_score!")


# For Pandas's read_csv, use header=0 when you know row 0 is a header row
# df here is a "dataframe":
df = pd.read_csv('titanic6.csv', header=0)
df.head()
df.info()

# let's drop columns with too few values or that won't be meaningful
# Here's an example of dropping the 'body' column, column M
df = df.drop('body', axis=1)  # axis = 1 indicates we want to drop a column, not a row




# careful!  You will need to drop more columns before dropping all of the N/A data!
'''this drop the whole column'''
df = df.drop('boat', axis=1)
df = df.drop('home.dest', axis=1)
df = df.drop('name', axis=1)
df = df.drop('cabin', axis=1)
df = df.drop('ticket', axis=1)
df = df.drop('embarked', axis=1)

# let's drop all of the rows with missing data:
'''this drop the rows with blanks'''
df = df.dropna()
# let's see our dataframe again...
# after some data-wrangling, I ended up with 1001 rows (anything over 500-600 seems reasonable)
df.head()
df.info()



# You'll need conversion to numeric datatypes for all input columns
#   Here's one example
#
def tr_mf(s):
    """ from string to number
    """
    d = { 'male':0, 'female':1 }
    return d[s]

df['sex'] = df['sex'].map(tr_mf)  # apply the function to the column

# let's see our dataframe again...
df.head()
df.info()


# you may need others!


print("+++ end of pandas +++\n")

# import sys
# sys.exit(0)

# separate into input X and target y dataframes...
X_all_df = df.drop('survived', axis=1)        # everything except the 'survival' column
y_all_df = df[ 'survived' ]                   # the target is survival! 

print("+++ start of numpy/scikit-learn +++")

# The data is currently in pandas "dataframes," but needs to be in numpy arrays
# These next two lines convert two dataframes to numpy arrays (using .values)
X_all = X_all_df.values     # iloc == "integer locations" of rows/cols
y_all = y_all_df.values     # individually addressable columns (by name)

# This "magic value" of 42 is here because we have looked at the dataset!
X_unlabeled = X_all[:42,:]  # unlabeled up to index 42
y_unlabeled = y_all[:42]    # unlabeled up to index 42

X_labeled_orig = X_all[42:,:]  # labeled data starts at index 22
y_labeled_orig = y_all[42:]    # labeled data starts at index 22

#
# Use iris4.py as your guide - it's mostly copy-and-paste

# we scramble the data - but _only_ the labeled data!
#
indices = np.random.permutation(len(y_labeled_orig))  # indices are a permutation

# we scramble both X and y with the same permutation
X_labeled = X_labeled_orig[indices]              # we apply the same permutation to each!
y_labeled = y_labeled_orig[indices]              # again...

#
# We separate into test data and training data ...
#    + We will train on the training data...
#    + We will test on the testing data and see how well we do!
#    + We don't have a separate validation set of rows; we plan to use cross-validation (below)
TEST_SIZE = 100
X_test = X_labeled[:TEST_SIZE]    # first few are for testing
y_test = y_labeled[:TEST_SIZE]

X_train = X_labeled[TEST_SIZE:]   # all the rest are for training
y_train = y_labeled[TEST_SIZE:]



# Create a kNN model and tune its parameters
# There is only one parameter, k, the number of neighbors considered...

from sklearn.neighbors import KNeighborsClassifier
best_k = 0
best_a = 0
for k in range(1,35):  # not likely to be a good value...

    knn = KNeighborsClassifier(n_neighbors=k)   # here, k is the "k" in kNN

    #
    # cross-validation
    #
    # This runs a routine that splits only the training set into two pieces:
    # model-building and model-validation. We'll use "build" and "validate"
    #
    cv_scores = cross_val_score( knn, X_train, y_train, cv=5 ) # cv is the number of splits
    # print('\nthe cv_scores are')
    for s in cv_scores:
        # we format it nicely...
        s_string = "{0:>#7.4f}".format(s) # docs.python.org/3/library/string.html#formatexamples
        # print("   ",s_string)
    av = cv_scores.mean()
    print(k,'+++ with average: ', av)
    if av >= best_a:
        best_a = av
        best_k = k
    print()

print('best k is: ',best_k)
#
'''Here is the code for training data'''
#
# now, train a new model with ALL of the training data...
# using the best value of k, best_k...
# and use this model to predict the labels of the test set
#
# this is a new model! line is where the full training data is used for the model
knn_train = KNeighborsClassifier(n_neighbors=best_k)   # now using the best_k
knn_train.fit(X_train, y_train)                        # using all of the data
print("\nCreated and trained a knn classifier with k =", best_k)  #, knn

# Now, run our test set!
print("For the input data in X_test,")
print("The predicted outputs are")
predicted_labels = knn_train.predict(X_test)
print(predicted_labels)

# and here are the actual labels (iris types)
print("and the actual labels are")
actual_labels = y_test
print(actual_labels)
# BUT -- there are points where things diverge...
# AND -- the goal is that you understand and feel more and more comfortable
#        with each of the parts of "the machine learning pipeline" ... !

'''Here is the code for predicting data'''

knn_final = KNeighborsClassifier(n_neighbors=best_k)  # now using the best_k
knn_final.fit(X_labeled, y_labeled)  # using all of the data
print("\nCreated and trained a knn classifier with k =", best_k)  # , knn

# Now, run our test set!
print("For the input data in X_test,")
print("The predicted outputs are")
predicted_labels = knn_train.predict(X_unlabeled)
print(predicted_labels)

'''How do I put the correct answer to match the actual data, so it can print out beautifully?'''
# and here are the actual labels (iris types)
print("and the actual labels are")
actual_labels = y_unlabeled
print(actual_labels)

#
# Note: for the Titanic data, it's the first 42 passengers who are unlabeled
#





"""
Comments and results:

Briefly mention how this went:
  + what value of k did you decide on for your kNN?
  + how high were you able to get the average cross-validation (testing) score?



Then, include the predicted survival of the unlabeled data (in the original order).
We'll share the known results next week... :-)





"""