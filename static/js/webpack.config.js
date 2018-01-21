// const HtmlWebpackPlugin = require('html-webpack-plugin');
const webpack = require('webpack');

const config = {
  entry: ['./app.js',],
  output: {
    path: __dirname+'/build',
    filename: 'app_build.js'
  },
  module: {
    loaders: [
      {test: /\.js$/, loader: 'babel-loader', query:{presets:["es2015"]}},
      {test: /\.sass$/, loader: ['style-loader','css-loader','sass-loader']},
      {test: /\.css$/, loader: ['style-loader','css-loader']},
       {test: /.(ttf|otf|eot|svg|woff(2)?)(\?[a-z0-9]+)?$/,
         use: [{
           loader: 'file-loader',
           options: {
             name: '[name].[ext]',
             outputPath: '../fonts/',    // where the fonts will go
             publicPath: '/static/js/fonts/'       // override the default path
           }
      },]},
      {test: /\.json$/, loader: 'json-loader'}
    ]
  },
  plugins: [
    // new webpack.optimize.UglifyJsPlugin()
    // new HtmlWebpackPlugin({template: '../../templates/articles/list.html'})
  ],


};

module.exports = config;