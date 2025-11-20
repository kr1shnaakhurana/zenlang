"""ZenLang zenin package - Input operations"""
import sys

def console(prompt=""):
    """Read input from console with optional prompt"""
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled")
        sys.exit(0)

def number(prompt=""):
    """Read number input from console"""
    while True:
        try:
            value = input(prompt)
            # Try to parse as int first, then float
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            print("Please enter a valid number")
        except (KeyboardInterrupt, EOFError):
            print("\nInput cancelled")
            sys.exit(0)

def text(prompt=""):
    """Read text input from console (alias for console)"""
    return console(prompt)

def yesno(prompt=""):
    """Read yes/no input from console"""
    while True:
        try:
            response = input(prompt + " (y/n): ").lower().strip()
            if response in ['y', 'yes']:
                return 1
            elif response in ['n', 'no']:
                return 0
            else:
                print("Please enter 'y' or 'n'")
        except (KeyboardInterrupt, EOFError):
            print("\nInput cancelled")
            sys.exit(0)

def choice(prompt, options):
    """Present multiple choice options"""
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    
    while True:
        try:
            choice = input("Enter choice number: ")
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return options[idx]
            else:
                print(f"Please enter a number between 1 and {len(options)}")
        except ValueError:
            print("Please enter a valid number")
        except (KeyboardInterrupt, EOFError):
            print("\nInput cancelled")
            sys.exit(0)

def password(prompt="Enter password: "):
    """Read password input (hidden)"""
    import getpass
    try:
        return getpass.getpass(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled")
        sys.exit(0)
