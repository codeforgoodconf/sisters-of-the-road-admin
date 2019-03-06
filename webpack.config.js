const path = require('path');

var BundleTracker = require('webpack-bundle-tracker');


module.exports = {
  context: __dirname,
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
    ],
  entry: './assets/js/index.js',
  output: {
    path: path.resolve(__dirname, 'assets', 'bundles'),
    filename: 'bundle.js'
  },
  resolve: {
    extensions: ['.js', '.jsx', '*']
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /(node_modules)/,
        use: {
          loader: 'babel-loader',
          query: {
            presets: ['@babel/env', '@babel/react']
          }
        },
      }
    ]
  },
  devtool: 'source-map'
};