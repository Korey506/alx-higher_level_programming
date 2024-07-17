### 0x12. JavaScript - Warm Up

#### Overview
This project is designed to get you comfortable with the basics of JavaScript, focusing on syntax and fundamental programming concepts. By the end of this project, you'll be familiar with essential JavaScript operations, data types, control structures, and functions.

#### Key Concepts

1. **Variables and Data Types**:
    - Variables can be declared using `var`, `let`, and `const`.
    - Basic data types include strings, numbers, booleans, null, undefined, and objects.

2. **Operators**:
    - Arithmetic operators: `+`, `-`, `*`, `/`, `%`.
    - Comparison operators: `==`, `===`, `!=`, `!==`, `>`, `<`, `>=`, `<=`.
    - Logical operators: `&&`, `||`, `!`.

3. **Control Structures**:
    - Conditional statements: `if`, `else if`, `else`, `switch`.
    - Loops: `for`, `while`, `do...while`.

4. **Functions**:
    - Function declaration: `function name(params) { ... }`.
    - Function expression: `const name = function(params) { ... }`.
    - Arrow functions: `const name = (params) => { ... }`.

5. **Arrays and Objects**:
    - Arrays: Ordered collections of values, e.g., `let arr = [1, 2, 3];`.
    - Objects: Collections of key-value pairs, e.g., `let obj = { key: value };`.

6. **ES6 Features**:
    - Template literals: `let text = `Hello, ${name}`;`.
    - Destructuring: `const [a, b] = [1, 2];`, `const {key} = obj;`.
    - Spread and Rest operators: `...`.

#### Example Tasks

1. **Printing Statements**:
    - Use `console.log()` to print messages or variables to the console.

    ```javascript
    console.log("Hello, World!");
    ```

2. **Conditional Statements**:
    - Use `if-else` statements to make decisions based on conditions.

    ```javascript
    let number = 10;
    if (number > 5) {
        console.log("Number is greater than 5");
    } else {
        console.log("Number is 5 or less");
    }
    ```

3. **Loops**:
    - Use `for` loops to iterate over arrays or perform repetitive tasks.

    ```javascript
    let arr = [1, 2, 3, 4, 5];
    for (let i = 0; i < arr.length; i++) {
        console.log(arr[i]);
    }
    ```

4. **Functions**:
    - Define and invoke functions to encapsulate reusable code.

    ```javascript
    function add(a, b) {
        return a + b;
    }
    console.log(add(2, 3));
    ```

5. **Arrays and Objects**:
    - Manipulate arrays and objects to store and retrieve data.

    ```javascript
    let fruits = ["apple", "banana", "cherry"];
    fruits.push("date");
    console.log(fruits);

    let person = {
        name: "Alice",
        age: 25
    };
    console.log(person.name);
    ```

#### Practical Tips

- Always test your code in a browser's console or a JavaScript runtime environment like Node.js.
- Practice using different data types and control structures to build a solid foundation.
- Explore and understand ES6 features as they provide powerful tools for modern JavaScript development.
- Write clean and readable code by following consistent naming conventions and indentation.

By working through these concepts and tasks, you'll build a strong foundation in JavaScript that will prepare you for more advanced topics and projects.
