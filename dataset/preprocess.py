

# import libraries
import arff
import numpy as np
import json
from sklearn.model_selection import train_test_split, KFold


# importing dataset and printing the datapoints it consists
phish_df = arff.load(open('dataset.arff', 'r'))
data = np.array(phish_df['data'])
print(phish_df['data'])


# In[18]:


print('This dataset contains {0} datapoints with {1} features'.format(data.shape[0], data.shape[1]-1))
print('Features: {0}'.format([feature[0] for feature in phish_df['attributes']]))


# In[19]:


data = data[:, [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 22, 30]]


# In[20]:


X, y = data[:, :-1], data[:, -1]
y.reshape(y.shape[0])
print('Values before dataset is split:')
print('X:{0}, y:{1}'.format(X.shape, y.shape))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
print('Values after dataset is split:')
print('X_train:{0}, y_train:{1}, X_test:{2}, y_test:{3}'.format(X_train.shape, y_train.shape, X_test.shape, y_test.shape))

# saves the results as *npy files
np.save('X_train.npy', X_train)
np.save('X_test.npy', X_test)
np.save('y_train.npy', y_train)
np.save('y_test.npy', y_test)
print('Saved!')

# Saves the test data to JSON file
#test_data = dict()
#test_data['X_test'] = X_test.tolist()
#test_data['y_test'] = y_test.tolist()
#with open('../../static/testdata.json', 'w') as tdfile:
    #json.dump(test_data, tdfile)
    #print('Test Data written to testdata.json')

