const express = require('express');
const morgan = require('morgan');
const app = express()

const PORT = process.env.PORT || 3000;

//import NeuralNet from 'neocortex-js';
// let neuralNetInstance = new NeuralNet({
//   modelFilePath: './encoded_model_for_js/model.json',
//   arrayType: 'float64'
// });

app.use(morgan('combined'));

app.get('/', (req,res) => {
  // neuralNetInstance.init().then (() => {
  //   console.log('yes the neural net worked');
  //   res.send('yes it worked on the neural net');
  // });
  res.send('hello');
});

app.listen(PORT, () => console.log("listening on port", PORT));
