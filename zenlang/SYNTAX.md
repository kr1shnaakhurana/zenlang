# ZenLang Syntax Documentation

## File Format

All ZenLang programs use the `.zen` file extension.

## Program Structure

```zenlang
.include <package1>
.include <package2>

// Your code here
```

## Includes

Includes must appear at the top of the file before any code.

```zenlang
.include <zenout>          // Built-in package
.include <dr/myScript>     // Local script
```

## Comments

ZenLang supports three types of comments:

```zenlang
// Single-line comment (C-style)

** Single-line comment (alternative style)

/* Multi-line comment
   spanning multiple lines */
```

## Variables

Variables are automatically declared on first assignment (like JavaScript/Python).

```zenlang
x = 10;
name = "ZenLang";
flag = 1;
```

## Data Types

- **Numbers**: `42`, `3.14`
- **Strings**: `"hello"`, `'world'`
- **Objects**: `{key=value, name="test"}`

## Operators

### Arithmetic
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Modulo

### Comparison
- `==` Equal
- `!=` Not equal
- `<` Less than
- `>` Greater than
- `<=` Less than or equal
- `>=` Greater than or equal

### Logical
- `&&` AND
- `||` OR
- `!` NOT

### Assignment
- `=` Assignment

## Functions

### Named Functions

```zenlang
funct myFunc(arg1, arg2) {
    // code
    return result;
};
```

### Anonymous Functions

```zenlang
callback = funct(x) {
    return x * 2;
};
```

### Function Calls

```zenlang
result = myFunc(10, 20);
```

## Control Flow

### If Statement

```zenlang
if (condition) {
    // code
} else {
    // code
};
```

### While Loop

```zenlang
while (condition) {
    // code
    break;      // Exit loop
    continue;   // Next iteration
};
```

### Do-While Loop

```zenlang
do {
    // code
} while (condition);
```

## Built-in Output

```zenlang
zenout.console("Hello World");
zenout.console("Value: " + x);
```

## Package System

### Built-in Packages

- `zenout` - I/O operations
- `net` - Networking (HTTP requests)
- `fs` - File system operations
- `web` - Web server
- `math` - Mathematical functions
- `sys` - System operations
- `time` - Time/date functions

### Using Packages

```zenlang
.include <zenout>
.include <net>

zenout.console("Making request...");
response = net.get("https://api.example.com");
zenout.console(response);
```

## Member Access

Access object members and call methods using dot notation:

```zenlang
zenout.console("text");
fs.read("file.txt");
math.sqrt(16);
```

## Object Literals

```zenlang
obj = {name="John", age=30};
```

## Statements

All statements must end with a semicolon (`;`).

```zenlang
x = 10;
zenout.console("Hello");
myFunc();
```

## Blocks

Code blocks use curly braces `{ }`:

```zenlang
if (x > 0) {
    zenout.console("Positive");
    x = x - 1;
};
```

## String Concatenation

Use `+` operator:

```zenlang
message = "Hello " + name + "!";
zenout.console("Value: " + x);
```

## Examples

### Complete Program

```zenlang
.include <zenout>
.include <net>

funct greet(name) {
    zenout.console("Hello " + name);
};

greet("Krishna");

x = 0;
while (x < 3) {
    zenout.console("Count: " + x);
    x = x + 1;
};

if (x == 3) {
    zenout.console("Done!");
};
```

### Recursion

```zenlang
.include <zenout>

funct factorial(n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    };
};

result = factorial(5);
zenout.console("5! = " + result);
```

### File Operations

```zenlang
.include <fs>
.include <zenout>

fs.write("data.txt", "Hello ZenLang!");
content = fs.read("data.txt");
zenout.console(content);

data = {name="John", age=30};
fs.writeJSON("data.json", data);
loaded = fs.readJSON("data.json");
```

### HTTP Requests

```zenlang
.include <net>
.include <zenout>

response = net.get("https://api.github.com/zen");
zenout.console(response);

data = {message="Hello"};
result = net.post("https://httpbin.org/post", data);
zenout.console(result);
```

## Reserved Keywords

- `funct` - Function definition
- `if` - Conditional statement
- `else` - Alternative branch
- `while` - While loop
- `do` - Do-while loop
- `break` - Exit loop
- `continue` - Next iteration
- `return` - Return from function

## Naming Rules

- Identifiers can contain letters, numbers, and underscores
- Must start with a letter or underscore
- Case-sensitive

Valid: `myVar`, `_private`, `count1`, `userName`
Invalid: `1var`, `my-var`, `my var`

## Error Handling

ZenLang will throw errors for:
- Syntax errors (missing semicolons, brackets, etc.)
- Undefined variables
- Type errors (calling non-functions, etc.)
- Runtime errors (file not found, network errors, etc.)

## Best Practices

1. Always include required packages at the top
2. Use meaningful variable and function names
3. End all statements with semicolons
4. Use proper indentation for readability
5. Add comments to explain complex logic
6. Handle errors appropriately

---

**ZenLang** - Simple, Elegant, Powerful 🔥
