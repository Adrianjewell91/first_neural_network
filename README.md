# A simple neural network for musical information analysis.

## major-chord-comprehensive

This NN builds upon major chords. In this NN, I've built a comprehensive validate_dataset off all major chords and their inversions (first and second).
Then, I built a custom validation set using unusual combinations of notes, but still are major chords (Currently building this validation set out more).

Instructions:

1. Clone repo
2. Install dependencies (see tutorials below)
3. 'python build-compre-major-chord-set.py'
4. 'python keras-compre-major_chord_network'
5. You should see the outputs for the validation set at the bottom. The numbers represent the prediction that the input value is that chord name.

## major-chord-nn

`major-chord` is an expansion upon a tutorial (listed below). I built my own dataset of major chords (all root position), and trained a network to accurately predict the chord name from a root position major chord played at any location on the piano. It's pretty simple dataset, and I'm currently in the works for building a more comprehensive data set (and more to come), but the main idea is there. See `build-major-chord-set.py` for explanation of how I built it, and how I am representing major chords.

Instructions:
1. Clone the repo.
2. Follow the tutorial to install the dependencies here: https://machinelearningmastery.com/setup-python-environment-machine-learning-deep-learning-anaconda/  
3. Make sure the `deepversions.py` and `versions.py` show the versions.
4. `python keras_major_chord_network.py` to see it run.

Differences between first_nn and major-chords
1. `first-nn` is simply outputting yes or no, while `major-chord-nn` is outputting the likelihood of the input data being any one of the 12 chord names. So, it outputs 12 values, those values being probabilities that sum to one. To achieve this, the softmax function is applied to the output values in `major-chord-nn`.
2. To accomodate for the increased complexity of the `major-chord` dataset, a filter is applied to the training set before passing it into the neural network.
  ex. If the chord is a A chord, the value is 9, but this actually needs to look like this: [0,0,0,0,0,0,0,0,0,9,0,0].


Next Steps:
1. Develop the data set to include inversions and create a validation set.

## /first-nn

A neural network learns to predict outcomes given a set of data, in which the set of data includes the inputs and their expected outputs. The neural network then decides the importance of each input such that, given a new set of data, the outputs will match the expected outputs. In this way, the neural network has 'learned' to answer questions.

The math behind how a neural network does this is rather complicated and not in scope of their brief demonstration. Basically, a neural network is the  transformation of a vector of inputs into a single output by transforming the input vector into the output value, where the number of layers in the neural network corespond with the number of intermediate vectors between the  input and the output. eg. A three-layer NN starts with the input vector, which is transformed into a hidden vector, which is transformed into the final vector (single value, but could be multiple value, depending on the desired output.).

`first-NN` is the result of my following of a tutorial (https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/), and also after being motivated to build a network.

Also, thank you to New Ruggeri for his lectures on machine learning theory.

Some key things to keep in mind.

1. You need to set up Python 3, Anaconda, and all of the dependencies.  The `versions.py` and `deepversions.py` are there for you verify that you have all of them.

2. I split the data set, into training and validation. Not hard, just a minor modification of the code.
