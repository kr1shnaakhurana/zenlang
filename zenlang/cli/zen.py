#!/usr/bin/env python3
"""ZenLang CLI Tool"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set ZenLang icon for Windows taskbar
if sys.platform == 'win32':
    try:
        import ctypes
        # Set the app user model ID to show ZenLang in taskbar
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('ZenLang.Interpreter.1.0')
    except:
        pass

from src.lexer import Lexer
from src.parser import Parser
from src.interpreter import Interpreter
import json

ZENPKGS_DIR = os.path.expanduser("~/.zenpkgs")

def run_file(filepath):
    """Run a ZenLang file"""
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found")
        sys.exit(1)
    
    with open(filepath, 'r') as f:
        source = f.read()
    
    try:
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        interpreter = Interpreter()
        interpreter.run(ast)
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user (Ctrl+C)")
        sys.exit(0)
    except EOFError:
        print("\n\nProgram terminated (EOF)")
        sys.exit(0)
    except Exception as e:
        print(f"ZenLang Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def build_file(filepath):
    """Build/compile a ZenLang file (currently just validates)"""
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found")
        sys.exit(1)
    
    with open(filepath, 'r') as f:
        source = f.read()
    
    try:
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        print(f"✓ Build successful: {filepath}")
    except Exception as e:
        print(f"Build Error: {e}")
        sys.exit(1)

def install_package(package_name):
    """Install a ZenLang package"""
    os.makedirs(ZENPKGS_DIR, exist_ok=True)
    
    pkg_path = os.path.join(ZENPKGS_DIR, package_name)
    
    if os.path.exists(pkg_path):
        print(f"Package '{package_name}' already installed")
        return
    
    # Create package directory
    os.makedirs(pkg_path, exist_ok=True)
    
    # Create package metadata
    metadata = {
        "name": package_name,
        "version": "1.0.0",
        "installed": True
    }
    
    with open(os.path.join(pkg_path, "package.json"), 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"✓ Installed package: {package_name}")

def remove_package(package_name):
    """Remove a ZenLang package"""
    pkg_path = os.path.join(ZENPKGS_DIR, package_name)
    
    if not os.path.exists(pkg_path):
        print(f"Package '{package_name}' not installed")
        return
    
    import shutil
    shutil.rmtree(pkg_path)
    print(f"✓ Removed package: {package_name}")

def list_packages():
    """List installed packages"""
    if not os.path.exists(ZENPKGS_DIR):
        print("No packages installed")
        return
    
    packages = os.listdir(ZENPKGS_DIR)
    
    if not packages:
        print("No packages installed")
    else:
        print("Installed packages:")
        for pkg in packages:
            print(f"  - {pkg}")

def show_version():
    """Show ZenLang version"""
    print("ZenLang v1.0.0")

def show_help():
    """Show help message"""
    print("""ZenLang CLI Tool

Usage:
  zen run <file.zen>        Run a ZenLang program
  zen build <file.zen>      Build/validate a ZenLang program
  zen install <package>     Install a package
  zen remove <package>      Remove a package
  zen list                  List installed packages
  zen version               Show version
  zen help                  Show this help message
""")

def main():
    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "run":
        if len(sys.argv) < 3:
            print("Error: No file specified")
            sys.exit(1)
        run_file(sys.argv[2])
    
    elif command == "build":
        if len(sys.argv) < 3:
            print("Error: No file specified")
            sys.exit(1)
        build_file(sys.argv[2])
    
    elif command == "install":
        if len(sys.argv) < 3:
            print("Error: No package specified")
            sys.exit(1)
        install_package(sys.argv[2])
    
    elif command == "remove":
        if len(sys.argv) < 3:
            print("Error: No package specified")
            sys.exit(1)
        remove_package(sys.argv[2])
    
    elif command == "list":
        list_packages()
    
    elif command == "version":
        show_version()
    
    elif command == "help":
        show_help()
    
    else:
        print(f"Unknown command: {command}")
        show_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
