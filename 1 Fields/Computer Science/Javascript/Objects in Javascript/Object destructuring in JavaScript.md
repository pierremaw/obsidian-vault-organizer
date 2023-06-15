**1. JavaScript Objects**: Key-value pairs for storing complex data
   - **Keys**: Unique identifiers for values within the object
   - **Values**: Data associated with corresponding keys

**2. Object Destructuring**: Syntax for extracting properties from objects
   - **Purpose**: Simplify access to object properties and improve code readability
   - **Syntax**: Use curly braces `{}` with property names to extract values

**3. Basic Destructuring**: Extracting single properties from an object
   - **Example**:
     ```javascript
     const person = {
       name: 'John',
       age: 30
     };

     const { name, age } = person;
     console.log(name); // Output: 'John'
     console.log(age);  // Output: 30
     ```

**4. Renaming Variables**: Assigning destructured properties to new variable names
   - **Syntax**: Use colon `:` followed by the new variable name
   - **Example**:
     ```javascript
     const { name: firstName, age: years } = person;
     console.log(firstName); // Output: 'John'
     console.log(years);     // Output: 30
     ```

**5. Default Values**: Specifying fallback values when destructuring
   - **Purpose**: Provide default values for properties that may not exist
   - **Syntax**: Use `=` followed by the default value
   - **Example**:
     ```javascript
     const { name, age, country = 'USA' } = person;
     console.log(country); // Output: 'USA'
     ```

**6. Nested Objects**: Destructuring properties from nested objects
   - **Example**:
     ```javascript
     const person = {
       name: 'John',
       age: 30,
       address: {
         city: 'New York',
         state: 'NY'
       }
     };

     const { name, age, address: { city, state } } = person;
     console.log(city);  // Output: 'New York'
     console.log(state); // Output: 'NY'
     ```

Conclusion: Object destructuring in JavaScript is a powerful technique for extracting properties from objects, improving code readability and reducing redundancy. By understanding basic destructuring, renaming variables, default values, and nested objects, developers can leverage this feature to write more efficient and maintainable code.

___
Type: #microtopic 
Topics: [[Computer Science]], [[JavaScript]], [[Objects in Javascript]]

