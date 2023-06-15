# `require`

In Node.js, the `require` keyword is used to import external modules or files. It is a built-in feature in Node.js that allows you to load other JavaScript modules, libraries, and files into your own code.

## Basic Usage

To use the `require` keyword, you simply write the keyword followed by the name of the module or file you want to import. Here's a basic example:

```
const myModule = require('./myModule');
```

In this example, we're using `require` to import a module located in a file called `myModule.js`. The `./` at the beginning of the filename specifies that it's located in the same directory as the current file.

## Importing External Libraries

You can also use `require` to import external libraries or packages that you've installed using a package manager like npm. Here's an example:

```
const axios = require('axios');
```

In this example, we're using `require` to import the `axios` library, which is a popular HTTP client for making requests in Node.js.

## Exporting Modules

In addition to importing modules, you can also use `require` to export your own modules from a file. To do this, you need to assign your module to `module.exports`. Here's an example:

```
// myModule.js function myFunction() {   console.log('Hello, world!'); }  module.exports = {   myFunction: myFunction };
```

In this example, we're defining a function called `myFunction` and exporting it as a module using `module.exports`. To use this module in another file, we can simply `require` it like this:

```
const myModule = require('./myModule');  myModule.myFunction(); // Output: Hello, world!
```

## Conclusion

The `require` keyword is a powerful tool in Node.js that allows you to import and export modules, libraries, and files. It's an essential feature for building complex Node.js applications and enables code reuse and modularity.
___
Type: #microtopic 
Topics: [[Computer Science]], [[Node.js]], [[Modules in Node.js]]

