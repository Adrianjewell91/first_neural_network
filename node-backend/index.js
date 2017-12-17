const express = require('express');
const morgan = require('morgan');
const app = express()

const PORT = process.env.PORT || 3000;

app.use(morgan('combined'));

app.get('/', (req,res) => {
  console.log('yes it worked');
  res.send('yes it worked');
});

app.listen(PORT, () => console.log("listening on port", PORT));
