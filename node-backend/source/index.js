const express = require('express');
const morgan = require('morgan');
const app = express()

const PORT = process.env.PORT || 3000;


//this doesn't work because I didn't export the weights in a readable way, and I don't know how to load them.
// import NeuralNet from 'neocortex-js';
//
// let neuralNetInstance = new NeuralNet({
//   modelFilePath: './encoded_model_for_js/model.json',
//   arrayType: 'float64'
// });
//
// neuralNetInstance.init().then (() => {
//   console.log('yes the neural net worked');
//   let predictions = neuralNetInstance.predict([0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]);
//   res.send('yes it worked on the neural net:', predictions);
// });

app.use(morgan('combined'));

import { Model } from 'keras-js';
const model = new Model({
  filepath: 'encoded_model_for_js/model.bin',
  filesystem: false
})

app.get('/', (req,res) => {
  res.send('hello');
});

app.listen(PORT, () => console.log("listening on port", PORT));
