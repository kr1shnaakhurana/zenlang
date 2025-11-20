# ZenLang

**A modern, easy-to-learn programming language for building web apps, desktop GUIs, and more.**

## Features

✨ **Simple Syntax** - Easy to learn, powerful to use  
🌐 **Real Web Server** - Build actual web applications with HTTP server  
🖥️ **GUI Support** - Create desktop applications with native windows  
💾 **Built-in Database** - In-memory database with SQL-like queries  
📦 **Rich Libraries** - 30+ libraries for common tasks  
🎨 **HTML Builder** - Generate HTML programmatically  
🔄 **State Management** - Reactive programming and state machines  
⚡ **Fast Development** - Get started in minutes  

---

## Quick Start

### Installation

```cmd
cd zenlang
install.bat
```

### Hello World

```zen
.include <zenout>

zenout.console("Hello, World!");
```

Run it:
```cmd
zen run hello.zen
```

### Web Server in 10 Lines

```zen
.include <zenlang/lib/http_server>
.include <zenlang/lib/router>

router = new Router();

router.get("/", funct(request) {
    response = new Response();
    return response.html("<h1>Hello from ZenLang!</h1>");
});

server = new HttpServer("localhost", 8080);
server.setRouter(router);
server.start();
```

Visit **http://localhost:8080** in your browser!

---

## Documentation

📖 **[Complete Guide](GUIDE.md)** - Everything you need to know

### Quick Links

- [Installation](GUIDE.md#installation)
- [Language Basics](GUIDE.md#language-basics)
- [Web Development](GUIDE.md#web-development)
- [GUI Applications](GUIDE.md#gui-applications)
- [Database & Data](GUIDE.md#database--data)
- [Libraries Reference](GUIDE.md#libraries-reference)
- [Examples](GUIDE.md#examples)

---

## Examples

Check out the `examples/` folder:

- **simple_web_server.zen** - Basic web server
- **real_web_server.zen** - Full-featured blog with database
- **gui_calculator.zen** - Desktop calculator app
- **database_demo.zen** - Database operations
- **comprehensive_libraries_demo.zen** - All libraries showcase

Run any example:
```cmd
zen run examples/simple_web_server.zen
```

---

## What You Can Build

### Web Applications
- REST APIs
- Blog platforms
- Todo apps
- E-commerce sites
- Admin dashboards

### Desktop Applications
- Calculators
- Notepads
- Todo lists
- Data entry forms
- Custom tools

### Data Processing
- Data pipelines
- ETL workflows
- Report generators
- Analytics tools

---

## Language Highlights

### Variables & Types
```zen
name = "Alice";
age = 25;
scores = [95, 87, 92];
user = {name = "Bob", age = 30};
```

### Functions
```zen
funct greet(name) {
    return "Hello, " + name + "!";
}
```

### Classes
```zen
class Person {
    private name;
    
    funct Person(n) {
        this.name = n;
    }
    
    public funct greet() {
        return "Hi, I'm " + this.name;
    }
}
```

### Web Routes
```zen
router.get("/users/:id", funct(request) {
    userId = request.getParam("id");
    user = db.findById(userId);
    
    response = new Response();
    return response.json(user);
});
```

---

## Libraries

### Core
- **zenout** - Console output
- **zenin** - User input
- **fs** - File system
- **net** - Networking
- **zendb** - SQLite database

### Web
- **http_server** - HTTP web server
- **router** - URL routing
- **html_builder** - HTML generation
- **template_engine** - Templates
- **form_handler** - Forms & validation

### Data
- **database** - In-memory database
- **query_builder** - SQL-like queries
- **json_parser** - JSON handling
- **cache** - Caching with LRU
- **collections** - Data structures

### Advanced
- **state_machine** - State machines
- **scheduler** - Task scheduling
- **pipeline** - Data pipelines
- **observer** - Reactive programming
- **event_emitter** - Events
- **logger** - Logging
- **testing** - Unit tests

---

## System Requirements

- **OS**: Windows 10/11
- **Python**: 3.7 or higher
- **RAM**: 512 MB minimum
- **Disk**: 50 MB for ZenLang

---

## Commands

```cmd
zen run program.zen    # Run a program
zen --version          # Show version
zen --help             # Show help
```

---

## Project Structure

```
zenlang/
├── cli/              # Command-line interface
├── src/              # Core interpreter
│   ├── runtime/      # Runtime modules
│   ├── lexer.py      # Lexical analyzer
│   ├── parser.py     # Parser
│   └── interpreter.py # Interpreter
├── lib/              # ZenLang libraries
├── examples/         # Example programs
├── install.bat       # Installation script
├── zen.bat           # Launcher script
├── GUIDE.md          # Complete documentation
└── README.md         # This file
```

---

## Contributing

ZenLang is open for contributions! Feel free to:

- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation
- Share your projects

---

## License

MIT License - Feel free to use ZenLang for any purpose!

---

## Get Started Now!

1. Run `install.bat`
2. Read [GUIDE.md](GUIDE.md)
3. Try `zen run examples/simple_web_server.zen`
4. Build something awesome! 🚀

---

**ZenLang** - Simple. Powerful. Modern.
