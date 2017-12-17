from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
#this line makes sure that theta values are randomized to same value for every run.
#It is not a necessary line. - should ask the tutorial writer about it.
numpy.random.seed(88)

dataset = numpy.loadtxt("major-chords-compre-set-train.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:88]
Y = dataset[:,88]

from keras.utils import to_categorical
Y_train = to_categorical(Y)

# validate_dataset = numpy.loadtxt("major-chords-compre-set-validate.csv", delimiter=",")
validate_dataset = numpy.loadtxt("test.csv", delimiter=",")
X_validate = validate_dataset[:,0:88]
Y_validate = validate_dataset[:,88]

Y_train_validate = to_categorical(Y_validate)

#create model
model = Sequential()
# model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(44, input_dim=88, activation='sigmoid'))
model.add(Dense(12, activation='softmax'))

# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#fit the model
model.fit(X,Y_train, epochs=20, batch_size=4)

scores = model.evaluate(X_validate,Y_train_validate, verbose=1)

print ("Evaluation of the network using the test version")

print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
print(model.predict(X_validate))

# model.save_weights('model.hdf5')
# with open('model.json', 'w') as f:
#     f.write(model.to_json())

print(X_validate[0])
