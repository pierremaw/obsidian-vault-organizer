The **await** keyword is only used inside async functions.

The **await** keyword is used in asynchronous JavaScript code to wait for a promise to be resolved before proceeding to the next line of code.

| Feature | Description                                                                                                                                                                                                      |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Asynchronous Code           | The await keyword is used in asynchronous JavaScript code to wait for a promise to be resolved before proceeding to the next line of code.                                                                       |
| Promise Handling            | The await keyword is used in conjunction with Promises to handle asynchronous code. When a Promise is returned, you can use await to pause the execution of the code until the Promise has resolved or rejected. |
| Async Functions             | await can only be used inside an async function, which is a function that returns a Promise. When an async function is called, it always returns a Promise.                                                      |
| Error Handling              | await can be used to catch errors that occur during Promise resolution. If a Promise is rejected, an error will be thrown, which can be caught using a try-catch block.                                          |
| Chaining Promises           | await can be used to chain multiple Promises together. You can use await to wait for the resolution of a Promise, and then use the result of that Promise in the next Promise in the chain.                      |
| Examples                    | async function fetchData() { const response = await fetch('https://example.com/data'); const data = await response.json(); return data; }                                                                        |

___
Type: #microtopic 
Topics: [[Computer Science]], [[JavaScript]], [[Functions in Javascript]]

