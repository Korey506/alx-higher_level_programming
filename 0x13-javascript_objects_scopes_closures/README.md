### 0x13. JavaScript - Objects, Scopes, and Closures

#### Overview
In this project, you will dive deeper into JavaScript, focusing on objects, scopes, and closures. These concepts are fundamental to understanding JavaScript's behavior, particularly in object-oriented and functional programming paradigms.

#### Key Concepts

1. **Objects**:
    - Objects in JavaScript are collections of key-value pairs.
    - They can be created using object literals, constructors, or the `Object.create` method.

    ```javascript
    // Object literal
    let obj = { key: value };

    // Constructor
    function Person(name, age) {
        this.name = name;
        this.age = age;
    }

    let person1 = new Person('Alice', 25);

    // Object.create
    let obj2 = Object.create(obj);
    ```

2. **Scopes**:
    - JavaScript has function scope and block scope.
    - Variables declared with `var` have function scope.
    - Variables declared with `let` and `const` have block scope.

    ```javascript
    function myFunction() {
        var functionScoped = 'I am function scoped';
        if (true) {
            let blockScoped = 'I am block scoped';
            const anotherBlockScoped = 'I am also block scoped';
        }
        console.log(functionScoped); // Works
        // console.log(blockScoped); // Error
        // console.log(anotherBlockScoped); // Error
    }
    ```

3. **Closures**:
    - A closure is a function that retains access to its lexical scope, even when the function is executed outside that scope.

    ```javascript
    function outerFunction() {
        let outerVariable = 'I am outside!';
        
        function innerFunction() {
            console.log(outerVariable);
        }
        
        return innerFunction;
    }
    
    let closure = outerFunction();
    closure(); // Outputs: 'I am outside!'
    ```

#### Example Tasks

1. **Creating and Manipulating Objects**:
    - Create objects using different methods and manipulate their properties.

    ```javascript
    let car = {
        make: 'Toyota',
        model: 'Corolla',
        year: 2020
    };

    car.color = 'red';
    console.log(car);
    ```

2. **Understanding Scopes**:
    - Practice writing functions and blocks to understand how scoping works in JavaScript.

    ```javascript
    function scopeExample() {
        var x = 1;
        let y = 2;
        const z = 3;
        
        if (true) {
            var x = 4; // Reassigned
            let y = 5; // Block scoped
            const z = 6; // Block scoped
            console.log(x, y, z); // 4, 5, 6
        }
        
        console.log(x, y, z); // 4, 2, 3
    }

    scopeExample();
    ```

3. **Using Closures**:
    - Create functions that demonstrate how closures work.

    ```javascript
    function counter() {
        let count = 0;
        
        return function() {
            count++;
            return count;
        };
    }

    let increment = counter();
    console.log(increment()); // 1
    console.log(increment()); // 2
    console.log(increment()); // 3
    ```

4. **Object Methods**:
    - Define methods within objects to understand how `this` keyword works.

    ```javascript
    let person = {
        firstName: 'John',
        lastName: 'Doe',
        fullName: function() {
            return this.firstName + ' ' + this.lastName;
        }
    };

    console.log(person.fullName()); // John Doe
    ```

#### Practical Tips

- **Experiment with Object Creation**: Try creating objects using literals, constructors, and `Object.create` to understand the differences.
- **Practice Scope Rules**: Write functions with nested blocks and functions to see how variable scoping works.
- **Utilize Closures**: Use closures to create private variables and functions, mimicking encapsulation found in other programming languages.
- **Debugging**: Use tools like console.log() and debugging features in your browser's developer tools to inspect object properties and scope.

By mastering these concepts, you'll gain a deeper understanding of JavaScript, making it easier to write robust, maintainable, and efficient code.
