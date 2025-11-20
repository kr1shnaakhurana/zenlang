# ZenLang Complete Guide

**ZenLang** - A modern, easy-to-learn programming language with powerful features for building desktop apps, web services, and more.

---

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Language Basics](#language-basics)
4. [Web Development](#web-development)
5. [GUI Applications](#gui-applications)
6. [Database & Data](#database--data)
7. [Libraries Reference](#libraries-reference)
8. [Examples](#examples)

---

## Installation

### Windows Installation

1. **Download or clone ZenLang**
2. **Run the installer:**
   ```cmd
   cd zenlang
   install.bat
   ```
3. **Restart your terminal**
4. **Test installation:**
   ```cmd
   zen --version
   ```

### Manual Setup

If the installer doesn't work:

1. Ensure Python 3.7+ is installed
2. Add ZenLang directory to PATH
3. Create `zen.bat` with:
   ```batch
   @echo off
   python "C:\path\to\zenlang\cli\zen.py" %*
   ```

---

## Quick Start

### Hello World

```zen
.include <zenout>

zenout.console("Hello, World!");
```

Run it:
```cmd
zen run hello.zen
```

### Variables and Types

```zen
** Variables
name = "Alice";
age = 25;
score = 95.5;
isActive = true;

** Arrays
numbers = [1, 2, 3, 4, 5];
names = ["Alice", "Bob", "Charlie"];

** Objects
user = {
    name = "Alice",
    age = 25,
    email = "alice@example.com"
};
```

### Control Flow

```zen
** If statements
if (age >= 18) {
    zenout.console("Adult");
} else {
    zenout.console("Minor");
}

** For loops
for (i = 0; i < 10; i = i + 1) {
    zenout.console(i);
}

** While loops
count = 0;
while (count < 5) {
    zenout.console(count);
    count = count + 1;
}

** For-each loops
items = [1, 2, 3, 4, 5];
for (item in items) {
    zenout.console(item);
}
```

### Functions

```zen
** Function definition
funct greet(name) {
    return "Hello, " + name + "!";
}

** Call function
message = greet("Alice");
zenout.console(message);

** Anonymous functions
add = funct(a, b) {
    return a + b;
};

result = add(5, 3);
```

### Classes

```zen
** Define class
class Person {
    private name;
    private age;
    
    funct Person(personName, personAge) {
        this.name = personName;
        this.age = personAge;
    }
    
    public funct greet() {
        return "Hello, I'm " + this.name;
    }
    
    public funct getAge() {
        return this.age;
    }
}

** Create instance
person = new Person("Alice", 25);
zenout.console(person.greet());
```

---

## Web Development

### Simple Web Server

```zen
.include <zenout>
.include <zenlang/lib/http_server>
.include <zenlang/lib/router>

** Create router
router = new Router();

** Define route
router.get("/", funct(request) {
    response = new Response();
    return response.html("<h1>Hello World!</h1>");
});

** Start server
server = new HttpServer("localhost", 8080);
server.setRouter(router);

zenout.console("Server running on http://localhost:8080");
server.start();
```

### HTML Builder

```zen
.include <zenlang/lib/html_builder>

** Build HTML programmatically
page = HtmlBuilder.div()
    .addClass("container")
    .child(
        HtmlBuilder.h1().text("Welcome")
    )
    .child(
        HtmlBuilder.p().text("This is a paragraph")
    )
    .child(
        HtmlBuilder.button()
            .addClass("btn")
            .text("Click Me")
    );

html = page.render();
```

### Complete Web App

```zen
.include <zenout>
.include <zenlang/lib/http_server>
.include <zenlang/lib/router>
.include <zenlang/lib/html_builder>
.include <zenlang/lib/database>

** Setup database
db = new Database();
users = db.createTable("users");
users.insert({name = "Alice", email = "alice@example.com"});

** Setup router
router = new Router();

** Home page
router.get("/", funct(request) {
    doc = new HtmlDocument("Home");
    
    doc.addStyle("
        body { font-family: Arial; padding: 20px; }
        .user { border: 1px solid #ddd; padding: 10px; margin: 10px 0; }
    ");
    
    doc.addToBody("<h1>Users</h1>");
    
    allUsers = users.findAll();
    for (i = 0; i < length(allUsers); i = i + 1) {
        user = allUsers[i];
        userDiv = HtmlBuilder.div()
            .addClass("user")
            .child(HtmlBuilder.h3().text(user["name"]))
            .child(HtmlBuilder.p().text(user["email"]));
        doc.addToBody(userDiv.render());
    }
    
    response = new Response();
    return response.html(doc.render());
});

** API endpoint
router.get("/api/users", funct(request) {
    allUsers = users.findAll();
    response = new Response();
    return response.json(allUsers);
});

** Start server
server = new HttpServer("localhost", 8080);
server.setRouter(router);
server.start();
```

### Forms and Validation

```zen
.include <zenlang/lib/form_handler>

** Build form
form = new FormBuilder("/submit", "POST");
form.text("username", "Username", "")
    .email("email", "Email", "")
    .password("password", "Password")
    .submit("Register");

html = form.render();

** Validate form data
validator = new FormValidator();
validator.required("username")
         .minLength("username", 3)
         .required("email")
         .email("email");

data = {username = "alice", email = "alice@example.com"};
isValid = validator.validate(data);

if (!isValid) {
    errors = validator.getErrors();
    ** Handle errors
}
```

---

## GUI Applications

### Simple Window

```zen
.include <zengui>

** Create window
window = zengui.createWindow("My App", 800, 600);

** Add label
label = zengui.createLabel(window, "Hello, GUI!", 50, 50, 200, 30);

** Add button
button = zengui.createButton(window, "Click Me", 50, 100, 100, 30);

** Button click handler
zengui.onClick(button, funct() {
    zengui.showMessage("Button clicked!");
});

** Show window
zengui.show(window);
zengui.mainloop();
```

### Calculator App

```zen
.include <zengui>

window = zengui.createWindow("Calculator", 300, 400);

** Display
display = zengui.createEntry(window, "", 10, 10, 280, 40);

** Number buttons
buttons = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0"];
x = 10;
y = 60;

for (i = 0; i < length(buttons); i = i + 1) {
    num = buttons[i];
    btn = zengui.createButton(window, num, x, y, 60, 60);
    
    zengui.onClick(btn, funct() {
        current = zengui.getValue(display);
        zengui.setValue(display, current + num);
    });
    
    x = x + 70;
    if (x > 200) {
        x = 10;
        y = y + 70;
    }
}

zengui.show(window);
zengui.mainloop();
```

---

## Database & Data

### In-Memory Database

```zen
.include <zenlang/lib/database>

** Create database
db = new Database();
users = db.createTable("users");

** Insert data
id = users.insert({
    name = "Alice",
    age = 25,
    email = "alice@example.com"
});

** Find by ID
user = users.findById(id);

** Find all
allUsers = users.findAll();

** Find with condition
adults = users.findWhere(funct(u) {
    return u["age"] >= 18;
});

** Update
users.update(id, {age = 26});

** Delete
users.delete(id);
```

### Query Builder

```zen
.include <zenlang/lib/query_builder>

products = [
    {name = "Laptop", price = 999, category = "Electronics"},
    {name = "Mouse", price = 25, category = "Electronics"},
    {name = "Desk", price = 299, category = "Furniture"}
];

** Build query
query = new Query(products);

results = query.whereEquals("category", "Electronics")
               .whereGreaterThan("price", 50)
               .orderBy("price")
               .limit(10)
               .get();

** Aggregations
avgPrice = Aggregator.avg(products, "price");
maxPrice = Aggregator.max(products, "price");
minPrice = Aggregator.min(products, "price");
```

### JSON Parsing

```zen
.include <zenlang/lib/json_parser>

** Parse JSON
jsonText = "{\"name\":\"Alice\",\"age\":25}";
data = parseJSON(jsonText);

zenout.console(data["name"]);  ** Alice
zenout.console(data["age"]);   ** 25

** Stringify
obj = {name = "Bob", age = 30};
json = stringifyJSON(obj);
```

---

## Libraries Reference

### Core Libraries

**zenout** - Console output
```zen
.include <zenout>
zenout.console("Hello");
```

**zenin** - User input
```zen
.include <zenin>
name = zenin.input("Enter name: ");
```

**fs** - File system
```zen
.include <fs>
content = fs.read("file.txt");
fs.write("file.txt", "content");
fs.append("file.txt", "more");
```

**net** - Networking
```zen
.include <net>
response = net.get("https://api.example.com");
```

**zendb** - Database
```zen
.include <zendb>
db = zendb.connect("mydb.db");
zendb.execute(db, "CREATE TABLE users (id, name)");
```

### Web Libraries

- **http_server** - HTTP web server
- **router** - URL routing
- **html_builder** - HTML generation
- **template_engine** - Template rendering
- **form_handler** - Form building and validation
- **web_utils** - URL parsing, cookies, sessions

### Data Libraries

- **database** - In-memory database
- **query_builder** - SQL-like queries
- **json_parser** - JSON parsing/serialization
- **cache** - Caching with LRU
- **collections** - Data structures (ArrayList, Stack, Queue, HashMap)

### Advanced Libraries

- **state_machine** - Finite state machines
- **scheduler** - Task scheduling
- **pipeline** - Data transformation pipelines
- **observer** - Observer pattern and reactive programming
- **event_emitter** - Event-driven programming
- **logger** - Logging system
- **testing** - Unit testing framework

### Utility Libraries

- **string_utils** - String manipulation
- **array_utils** - Array operations
- **math_utils** - Math functions
- **date_utils** - Date/time handling
- **validation** - Data validation
- **crypto** - Cryptography
- **algorithms** - Common algorithms
- **functional** - Functional programming

---

## Examples

### Example 1: Todo List Web App

```zen
.include <zenout>
.include <zenlang/lib/http_server>
.include <zenlang/lib/router>
.include <zenlang/lib/html_builder>
.include <zenlang/lib/database>

db = new Database();
todos = db.createTable("todos");

router = new Router();

router.get("/", funct(request) {
    doc = new HtmlDocument("Todo List");
    
    doc.addStyle("
        body { font-family: Arial; max-width: 600px; margin: 50px auto; }
        .todo { padding: 10px; border: 1px solid #ddd; margin: 5px 0; }
        input { padding: 8px; width: 70%; }
        button { padding: 8px 20px; }
    ");
    
    doc.addToBody("<h1>Todo List</h1>");
    
    ** Add form
    doc.addToBody("
        <form method='POST' action='/add'>
            <input type='text' name='task' placeholder='New task'>
            <button type='submit'>Add</button>
        </form>
    ");
    
    ** List todos
    allTodos = todos.findAll();
    for (i = 0; i < length(allTodos); i = i + 1) {
        todo = allTodos[i];
        todoDiv = HtmlBuilder.div()
            .addClass("todo")
            .child(HtmlBuilder.span().text(todo["task"]));
        doc.addToBody(todoDiv.render());
    }
    
    response = new Response();
    return response.html(doc.render());
});

router.post("/add", funct(request) {
    ** Add todo (parse form data from request.body)
    todos.insert({task = "New task", done = false});
    
    response = new Response();
    return response.redirect("/");
});

server = new HttpServer("localhost", 8080);
server.setRouter(router);
server.start();
```

### Example 2: REST API

```zen
.include <zenlang/lib/http_server>
.include <zenlang/lib/router>
.include <zenlang/lib/database>

db = new Database();
products = db.createTable("products");

** Sample data
products.insert({name = "Laptop", price = 999});
products.insert({name = "Mouse", price = 25});

router = new Router();

** GET all products
router.get("/api/products", funct(request) {
    allProducts = products.findAll();
    response = new Response();
    return response.json(allProducts);
});

** GET single product
router.get("/api/products/:id", funct(request) {
    id = int(request.getParam("id"));
    product = products.findById(id);
    
    response = new Response();
    if (product != null) {
        return response.json(product);
    } else {
        return response.setStatus(404).json({error = "Not found"});
    }
});

** POST new product
router.post("/api/products", funct(request) {
    ** Parse JSON from request.body
    data = parseJSON(request.body);
    id = products.insert(data);
    
    response = new Response();
    return response.setStatus(201).json({id = id});
});

** PUT update product
router.put("/api/products/:id", funct(request) {
    id = int(request.getParam("id"));
    data = parseJSON(request.body);
    products.update(id, data);
    
    response = new Response();
    return response.json({updated = true});
});

** DELETE product
router.delete("/api/products/:id", funct(request) {
    id = int(request.getParam("id"));
    products.delete(id);
    
    response = new Response();
    return response.json({deleted = true});
});

server = new HttpServer("localhost", 8080);
server.setRouter(router);
server.start();
```

### Example 3: Data Processing Pipeline

```zen
.include <zenlang/lib/pipeline>
.include <zenlang/lib/query_builder>

** Sample data
sales = [
    {product = "Laptop", amount = 999, region = "North"},
    {product = "Mouse", amount = 25, region = "South"},
    {product = "Keyboard", amount = 75, region = "North"},
    {product = "Monitor", amount = 399, region = "East"}
];

** Create pipeline
pipeline = new Pipeline();

** Filter high-value sales
pipeline.pipe(funct(data) {
    query = new Query(data);
    return query.whereGreaterThan("amount", 100).get();
});

** Group by region
pipeline.pipe(funct(data) {
    return Aggregator.groupBy(data, "region");
});

** Process data
result = pipeline.process(sales);
```

---

## Built-in Functions

### Type Conversion
- `str(value)` - Convert to string
- `int(value)` - Convert to integer
- `float(value)` - Convert to float
- `bool(value)` - Convert to boolean

### Type Checking
- `type(value)` - Get type name
- `isNumber(value)` - Check if number
- `isString(value)` - Check if string
- `isArray(value)` - Check if array
- `isObject(value)` - Check if object

### Array Functions
- `length(array)` - Get length
- `push(array, item)` - Add to end
- `pop(array)` - Remove from end
- `shift(array)` - Remove from start
- `unshift(array, item)` - Add to start
- `slice(array, start, end)` - Get slice
- `indexOf(array, item)` - Find index
- `includes(array, item)` - Check if contains
- `reverse(array)` - Reverse array
- `sort(array)` - Sort array
- `join(array, separator)` - Join to string
- `filter(array, func)` - Filter items
- `map(array, func)` - Transform items

### String Functions
- `upper(str)` - To uppercase
- `lower(str)` - To lowercase
- `trim(str)` - Remove whitespace
- `split(str, delimiter)` - Split to array
- `replace(str, search, replace)` - Replace text
- `startsWith(str, prefix)` - Check start
- `endsWith(str, suffix)` - Check end
- `substring(str, start, end)` - Get substring
- `charAt(str, index)` - Get character
- `repeat(str, count)` - Repeat string

### Object Functions
- `keys(object)` - Get keys array
- `values(object)` - Get values array
- `hasKey(object, key)` - Check if key exists

### Math Functions
- `sum(array)` - Sum of numbers
- `avg(array)` - Average
- `min(array)` - Minimum value
- `max(array)` - Maximum value

---

## Command Line

```cmd
** Run a program
zen run program.zen

** Show version
zen --version

** Show help
zen --help
```

---

## Tips & Best Practices

1. **Always include required libraries** at the top of your file
2. **Use meaningful variable names** for better readability
3. **Comment your code** with `**` for documentation
4. **Test your web apps** by visiting http://localhost:8080
5. **Use the database library** for data persistence
6. **Validate user input** with FormValidator
7. **Handle errors** with proper checks
8. **Organize code** into functions and classes

---

## Getting Help

- **Documentation**: This guide
- **Examples**: Check the `examples/` folder
- **Issues**: Report bugs or request features

---

## Quick Reference Card

```zen
** Variables
name = "value";

** Arrays
arr = [1, 2, 3];

** Objects
obj = {key = "value"};

** Functions
funct myFunc(param) {
    return param * 2;
}

** Classes
class MyClass {
    funct MyClass() {
        this.value = 0;
    }
}

** Control Flow
if (condition) { }
for (i = 0; i < 10; i = i + 1) { }
while (condition) { }

** Web Server
server = new HttpServer("localhost", 8080);
server.setRouter(router);
server.start();
```

---

**ZenLang** - Simple, Powerful, Modern

Visit the `examples/` folder for more complete applications!
