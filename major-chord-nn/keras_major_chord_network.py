from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(88)

# load pima indians dataset
dataset = numpy.loadtxt("major-chords-set-train.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:88]
Y = dataset[:,88]

from keras.utils import to_categorical
Y_train = to_categorical(Y)

# dataset = numpy.loadtxt("pima-indians-diabetes_validate.csv", delimiter=",")
# # split into input (X) and output (Y) variables
# X_validate = dataset[:,0:8]
# Y_validate = dataset[:,8]

#create model
model = Sequential()
# model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(40, input_dim=88, activation='sigmoid'))
model.add(Dense(12, activation='softmax'))

# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#fit the model
model.fit(X,Y_train, epochs=150, batch_size=4)

scores = model.evaluate(X,Y_train)

print ("Evaluation of the network using the test version")

print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
