"""ZenLang zenwares package - Software development utilities"""
import os
import sys
import json
import time as pytime

# ============ UI/Display Functions ============

def clear():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def title(text):
    """Display a title banner"""
    width = len(text) + 4
    print("=" * width)
    print(f"  {text}  ")
    print("=" * width)

def header(text):
    """Display a header"""
    print(f"\n=== {text} ===\n")

def separator(char="-", length=50):
    """Display a separator line"""
    print(char * length)

def box(text):
    """Display text in a box"""
    lines = text.split('\n')
    width = max(len(line) for line in lines) + 4
    
    print("+" + "-" * (width - 2) + "+")
    for line in lines:
        padding = width - len(line) - 4
        print(f"| {line}{' ' * padding} |")
    print("+" + "-" * (width - 2) + "+")

def progress(current, total, prefix="Progress:", length=40):
    """Display a progress bar"""
    percent = current / total
    filled = int(length * percent)
    bar = "█" * filled + "-" * (length - filled)
    print(f"\r{prefix} |{bar}| {int(percent * 100)}%", end="", flush=True)
    if current >= total:
        print()  # New line when complete

def spinner(message="Loading", duration=2):
    """Display a spinner animation"""
    frames = ['|', '/', '-', '\\']
    end_time = pytime.time() + duration
    i = 0
    while pytime.time() < end_time:
        print(f"\r{message} {frames[i % len(frames)]}", end="", flush=True)
        pytime.sleep(0.1)
        i += 1
    print(f"\r{message} Done!     ")

# ============ Menu System ============

def menu(title_text, options):
    """Display a menu and get user choice"""
    print(f"\n{title_text}")
    separator()
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    separator()
    
    while True:
        try:
            choice = input("Select option: ")
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return idx
            else:
                print(f"Please enter a number between 1 and {len(options)}")
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\nCancelled")
            return -1

# ============ Data Management ============

def table(headers, rows):
    """Display data in a table format"""
    # Calculate column widths
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Print header
    header_line = " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
    print(header_line)
    print("-" * len(header_line))
    
    # Print rows
    for row in rows:
        row_line = " | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))
        print(row_line)

def saveData(filename, data):
    """Save data to JSON file"""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

def loadData(filename):
    """Load data from JSON file"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return json.load(f)
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# ============ Validation ============

def validate(value, rules):
    """Validate input against rules"""
    # Rules can be: "required", "number", "email", "min:5", "max:10"
    for rule in rules:
        if rule == "required" and not value:
            return False
        elif rule == "number":
            try:
                float(value)
            except ValueError:
                return False
        elif rule.startswith("min:"):
            min_len = int(rule.split(":")[1])
            if len(str(value)) < min_len:
                return False
        elif rule.startswith("max:"):
            max_len = int(rule.split(":")[1])
            if len(str(value)) > max_len:
                return False
    return True

# ============ Utilities ============

def pause(message="Press Enter to continue..."):
    """Pause execution until user presses Enter"""
    input(message)

def confirm(message):
    """Ask for confirmation"""
    response = input(f"{message} (y/n): ").lower().strip()
    return response in ['y', 'yes']

def timestamp():
    """Get current timestamp string"""
    return pytime.strftime("%Y-%m-%d %H:%M:%S")

def log(message, level="INFO"):
    """Log a message with timestamp"""
    print(f"[{timestamp()}] [{level}] {message}")

def error(message):
    """Display error message"""
    print(f"ERROR: {message}")

def success(message):
    """Display success message"""
    print(f"✓ {message}")

def warning(message):
    """Display warning message"""
    print(f"⚠ {message}")

def info(message):
    """Display info message"""
    print(f"ℹ {message}")

# ============ Color Support (Basic) ============

class colors:
    """ANSI color codes for terminal"""
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

def colorize(text, color):
    """Colorize text (basic support)"""
    color_map = {
        'red': colors.RED,
        'green': colors.GREEN,
        'yellow': colors.YELLOW,
        'blue': colors.BLUE,
        'magenta': colors.MAGENTA,
        'cyan': colors.CYAN,
        'white': colors.WHITE,
    }
    color_code = color_map.get(color.lower(), '')
    return f"{color_code}{text}{colors.RESET}"

# ============ Application Framework ============

class App:
    """Simple application framework"""
    def __init__(self, name, version="1.0.0"):
        self.name = name
        self.version = version
        self.running = True
    
    def start(self):
        """Start the application"""
        clear()
        title(f"{self.name} v{self.version}")
        print()
    
    def stop(self):
        """Stop the application"""
        self.running = False
        print(f"\nThank you for using {self.name}!")
    
    def isRunning(self):
        """Check if application is running"""
        return self.running

def createApp(name, version="1.0.0"):
    """Create a new application instance"""
    return App(name, version)
