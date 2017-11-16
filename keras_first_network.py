from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)

# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes_train.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]

dataset = numpy.loadtxt("pima-indians-diabetes_validate.csv", delimiter=",")
# split into input (X) and output (Y) variables
X_validate = dataset[:,0:8]
Y_validate = dataset[:,8]

#create model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile model 
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#fit the model
model.fit(X,Y, epochs=150, batch_size=10)

scores = model.evaluate(X_validate,Y_validate)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


