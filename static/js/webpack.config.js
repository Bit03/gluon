// const HtmlWebpackPlugin = require('html-webpack-plugin');
const webpack = require('webpack');

const config = {
  entry: './app.js',
  output: {
    path: __dirname+'/build',
    filename: 'bundle.js'
  },
  module: {
    loaders: [
      {test: /\.css$/, loader: 'style-loader!css-loader'},
      {test: /\.json$/, loader: 'json-loader'}
    ]
  },
  plugins: [
    new webpack.optimize.UglifyJsPlugin()
    // new HtmlWebpackPlugin({template: '../../templates/articles/list.html'})
  ]
};

module.exports = config;