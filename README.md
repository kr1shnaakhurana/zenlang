# ZenLang

**A modern, easy-to-learn programming language for building web apps, desktop GUIs, and more.**

## Installation

Simply run:
```cmd
install.bat
```

Then restart your terminal and test:
```cmd
zen version
```

## Quick Start

```zen
.include <zenout>
zenout.console("Hello, World!");
```

Run it:
```cmd
zen run hello.zen
```

## Web Server Example

```cmd
zen run zenlang\examples\simple_web_server.zen
```

Then visit: **http://localhost:8080**

## Documentation

📖 **[Complete Guide](zenlang/GUIDE.md)** - Everything you need to know

- [Installation](zenlang/GUIDE.md#installation)
- [Language Basics](zenlang/GUIDE.md#language-basics)
- [Web Development](zenlang/GUIDE.md#web-development)
- [GUI Applications](zenlang/GUIDE.md#gui-applications)
- [Examples](zenlang/GUIDE.md#examples)

## Project Structure

```
.
├── install.bat          # Installation script
├── zen.bat             # ZenLang launcher
└── zenlang/            # ZenLang directory
    ├── GUIDE.md        # Complete documentation
    ├── README.md       # Detailed overview
    ├── cli/            # Command-line tool
    ├── src/            # Core interpreter
    ├── lib/            # 30+ libraries
    └── examples/       # Example programs
```

## Commands

```cmd
zen help                 # Show help
zen version              # Show version
zen run program.zen      # Run a program
```

## Examples

```cmd
zen run zenlang\examples\simple_web_server.zen
zen run zenlang\examples\gui_calculator.zen
zen run zenlang\examples\database_demo.zen
```

## Features

✨ Simple syntax  
🌐 Real HTTP web server  
🖥️ Desktop GUI support  
💾 Built-in database  
📦 30+ libraries  
🎨 HTML builder  
⚡ Fast development  

---

**Get Started:** Run `install.bat` and read [zenlang/GUIDE.md](zenlang/GUIDE.md)
