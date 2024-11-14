// jest.config.js
module.exports = {
    transform: {
      '^.+\\.vue$': 'vue-jest',
      '^.+\\.ts$': 'ts-jest',
      '^.+\\.js$': 'babel-jest',
    },
    moduleFileExtensions: ['js', 'ts', 'vue', 'json'],
  };