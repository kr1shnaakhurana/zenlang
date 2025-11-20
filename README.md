<div align="center">

<!-- Banner -->
<img src="zenlang/zenlang_icon.png" alt="ZenLang Logo" width="200"/>

# ZenLang

### *A Modern Programming Language for Web & Desktop*

<p>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License"/>
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python"/>
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey.svg" alt="Platform"/>
  <img src="https://img.shields.io/badge/Version-1.0.0-green.svg" alt="Version"/>
</p>

<p>
  <strong>Simple Syntax • Real Web Server • Desktop GUI • Built-in Database</strong>
</p>

<p>
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-features">Features</a> •
  <a href="#-documentation">Documentation</a> •
  <a href="#-examples">Examples</a> •
  <a href="zenlang/GUIDE.md">Full Guide</a>
</p>

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎯 **Easy to Learn**
- Simple, intuitive syntax
- No complex setup required
- Get started in minutes
- Comprehensive documentation

</td>
<td width="50%">

### 🌐 **Real Web Server**
- Built-in HTTP server
- REST API support
- HTML builder included
- Template engine

</td>
</tr>
<tr>
<td width="50%">

### 🖥️ **Desktop GUI**
- Native window support
- Form controls
- Event handling
- Cross-platform ready

</td>
<td width="50%">

### 💾 **Built-in Database**
- In-memory database
- SQL-like queries
- JSON support
- Data pipelines

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/kr1shnaakhurana/zenlang.git
cd zenlang
install.bat
```

### Hello World

<table>
<tr>
<td width="50%">

**Create `hello.zen`:**
```zen
.include <zenout>

zenout.console("Hello, World!");
```

</td>
<td width="50%">

**Run it:**
```bash
zen run hello.zen
```

**Output:**
```
Hello, World!
```

</td>
</tr>
</table>

### Web Server Example

<table>
<tr>
<td>

**Create `server.zen`:**
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

**Run it:**
```bash
zen run server.zen
```

**Visit:** [http://localhost:8080](http://localhost:8080) 🎉

</td>
</tr>
</table>

---

## 📖 Documentation

<div align="center">

| Document | Description |
|----------|-------------|
| **[📘 Complete Guide](zenlang/GUIDE.md)** | Everything you need to know |
| **[⚡ Quick Reference](zenlang/GETTING_STARTED.txt)** | Quick start card |
| **[📚 Examples](zenlang/examples/)** | 50+ example programs |
| **[🔧 Syntax](zenlang/SYNTAX.md)** | Language syntax reference |

</div>

---

## 🎯 What You Can Build

<table>
<tr>
<td width="33%" align="center">

### 🌐 Web Applications
✅ REST APIs<br/>
✅ Blog platforms<br/>
✅ Todo apps<br/>
✅ E-commerce sites<br/>
✅ Admin dashboards

</td>
<td width="33%" align="center">

### 🖥️ Desktop Apps
✅ Calculators<br/>
✅ Notepads<br/>
✅ Todo lists<br/>
✅ Data entry forms<br/>
✅ Custom tools

</td>
<td width="33%" align="center">

### 📊 Data Processing
✅ Data pipelines<br/>
✅ ETL workflows<br/>
✅ Report generators<br/>
✅ Analytics tools<br/>
✅ Data transformations

</td>
</tr>
</table>

---

## 💻 Code Examples

<details>
<summary><b>🔹 Variables & Types</b></summary>

```zen
** Variables
name = "Alice";
age = 25;
scores = [95, 87, 92];
user = {name = "Bob", age = 30};
```

</details>

<details>
<summary><b>🔹 Functions</b></summary>

```zen
funct greet(name) {
    return "Hello, " + name + "!";
}

message = greet("Alice");
zenout.console(message);
```

</details>

<details>
<summary><b>🔹 Classes</b></summary>

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

person = new Person("Alice");
zenout.console(person.greet());
```

</details>

<details>
<summary><b>🔹 Web Routes</b></summary>

```zen
router.get("/users/:id", funct(request) {
    userId = request.getParam("id");
    user = db.findById(userId);
    
    response = new Response();
    return response.json(user);
});
```

</details>

<details>
<summary><b>🔹 Database Operations</b></summary>

```zen
.include <zenlang/lib/database>

db = new Database();
users = db.createTable("users");

** Insert
id = users.insert({name = "Alice", age = 25});

** Query
adults = users.findWhere(funct(u) {
    return u["age"] >= 18;
});

** Update
users.update(id, {age = 26});
```

</details>

---

## 📦 Libraries

<div align="center">

### Core Libraries
| Library | Description |
|---------|-------------|
| **zenout** | Console output |
| **zenin** | User input |
| **fs** | File system operations |
| **net** | HTTP networking |
| **zendb** | SQLite database |

### Web Libraries
| Library | Description |
|---------|-------------|
| **http_server** | Real HTTP web server |
| **router** | URL routing with parameters |
| **html_builder** | Programmatic HTML generation |
| **template_engine** | Template rendering |
| **form_handler** | Form building & validation |

### Data Libraries
| Library | Description |
|---------|-------------|
| **database** | In-memory database |
| **query_builder** | SQL-like queries |
| **json_parser** | JSON handling |
| **cache** | LRU caching |
| **collections** | Data structures |

### Advanced Libraries
| Library | Description |
|---------|-------------|
| **state_machine** | Finite state machines |
| **scheduler** | Task scheduling |
| **pipeline** | Data pipelines |
| **observer** | Reactive programming |
| **event_emitter** | Event-driven programming |

</div>

<details>
<summary><b>📚 View All 30+ Libraries</b></summary>

**Utility Libraries:**
- string_utils, array_utils, math_utils
- date_utils, validation, crypto
- algorithms, functional

**See [GUIDE.md](zenlang/GUIDE.md#libraries-reference) for complete documentation**

</details>

---

## 🎮 Examples

<div align="center">

| Example | Command | Description |
|---------|---------|-------------|
| 🌐 **Web Server** | `zen run zenlang\examples\simple_web_server.zen` | Basic HTTP server |
| 📝 **Blog App** | `zen run zenlang\examples\real_web_server.zen` | Full blog with database |
| 🧮 **Calculator** | `zen run zenlang\examples\gui_calculator.zen` | Desktop calculator |
| 💾 **Database** | `zen run zenlang\examples\database_demo.zen` | Database operations |
| 📚 **Libraries** | `zen run zenlang\examples\comprehensive_libraries_demo.zen` | All libraries |

</div>

---

## 🛠️ System Requirements

<table>
<tr>
<td align="center">

**Operating System**<br/>
Windows 10/11

</td>
<td align="center">

**Python**<br/>
3.7 or higher

</td>
<td align="center">

**RAM**<br/>
512 MB minimum

</td>
<td align="center">

**Disk Space**<br/>
50 MB

</td>
</tr>
</table>

---

## 📋 Commands

<div align="center">

```bash
zen help                 # Show all commands
zen version              # Show version
zen run program.zen      # Run a program
```

</div>

---

## 🏗️ Project Structure

```
zenlang/
├── 📄 install.bat          # Installation script
├── 🚀 zen.bat             # ZenLang launcher
├── 📖 GUIDE.md            # Complete documentation
├── 📁 cli/                # Command-line interface
├── 🔧 src/                # Core interpreter
│   ├── runtime/          # Runtime modules
│   ├── lexer.py          # Lexical analyzer
│   ├── parser.py         # Parser
│   └── interpreter.py    # Interpreter
├── 📦 lib/                # 30+ ZenLang libraries
├── 📚 examples/           # 50+ example programs
└── 🎨 vscode-extension/   # VSCode support
```

---

## 🤝 Contributing

<div align="center">

Contributions are welcome! Feel free to:

🐛 **Report bugs** • 💡 **Suggest features** • 🔧 **Submit PRs** • 📖 **Improve docs**

</div>

---

## 📄 License

<div align="center">

**MIT License** - Feel free to use ZenLang for any purpose!

</div>

---

## 🌟 Get Started Now!

<div align="center">

<table>
<tr>
<td align="center">

**1️⃣**<br/>
Clone the repo

</td>
<td align="center">

**2️⃣**<br/>
Run `install.bat`

</td>
<td align="center">

**3️⃣**<br/>
Read [GUIDE.md](zenlang/GUIDE.md)

</td>
<td align="center">

**4️⃣**<br/>
Build something! 🚀

</td>
</tr>
</table>

</div>

---

<div align="center">

### 📞 Links

**[🌐 Repository](https://github.com/kr1shnaakhurana/zenlang)** • 
**[📖 Documentation](zenlang/GUIDE.md)** • 
**[📚 Examples](zenlang/examples/)**

---

### ZenLang - *Simple. Powerful. Modern.*

Made with ❤️ by [Krishna Khurana](https://github.com/kr1shnaakhurana)

<img src="https://img.shields.io/github/stars/kr1shnaakhurana/zenlang?style=social" alt="Stars"/>
<img src="https://img.shields.io/github/forks/kr1shnaakhurana/zenlang?style=social" alt="Forks"/>

</div>
