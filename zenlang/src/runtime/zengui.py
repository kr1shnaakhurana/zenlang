"""ZenLang zengui package - Real GUI operations using tkinter"""
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import sys

# Global window reference
_current_window = None
_widgets = {}
_widget_counter = 0

def createWindow(title, width=800, height=600):
    """Create a new GUI window"""
    global _current_window
    
    _current_window = tk.Tk()
    _current_window.title(title)
    _current_window.geometry(f"{width}x{height}")
    
    # Set ZenLang icon
    try:
        # Try multiple paths to find the icon
        import os
        possible_paths = [
            "zenlang.ico",
            "zenlang/zenlang.ico",
            os.path.join(os.path.dirname(__file__), "..", "..", "zenlang.ico"),
            os.path.join(os.path.dirname(__file__), "..", "..", "..", "zenlang", "zenlang.ico"),
        ]
        
        icon_set = False
        for icon_path in possible_paths:
            if os.path.exists(icon_path):
                _current_window.iconbitmap(icon_path)
                icon_set = True
                break
        
        # If no .ico file found, try to use PNG with PhotoImage
        if not icon_set:
            png_paths = [
                "zenlang_icon.png",
                "zenlang/zenlang_icon.png",
                os.path.join(os.path.dirname(__file__), "..", "..", "zenlang_icon.png"),
            ]
            for png_path in png_paths:
                if os.path.exists(png_path):
                    icon = tk.PhotoImage(file=png_path)
                    _current_window.iconphoto(True, icon)
                    break
    except Exception as e:
        # Silently fail if icon can't be set
        pass
    
    return "window_main"

def setTitle(window_id, title):
    """Set window title"""
    global _current_window
    if _current_window:
        _current_window.title(title)

def setSize(window_id, width, height):
    """Set window size"""
    global _current_window
    if _current_window:
        _current_window.geometry(f"{width}x{height}")

def setResizable(window_id, resizable):
    """Set if window is resizable"""
    global _current_window
    if _current_window:
        _current_window.resizable(resizable, resizable)

def addButton(text, x, y, width=100, height=30):
    """Add a button to the window"""
    global _current_window, _widgets, _widget_counter
    
    if not _current_window:
        raise RuntimeError("No window created. Call createWindow first.")
    
    _widget_counter += 1
    widget_id = f"button_{_widget_counter}"
    
    button = tk.Button(_current_window, text=text, width=width//8, height=height//20)
    button.place(x=x, y=y, width=width, height=height)
    
    _widgets[widget_id] = {
        'widget': button,
        'type': 'button',
        'callback': None
    }
    
    return widget_id

def addLabel(text, x, y, width=100, height=30):
    """Add a label to the window"""
    global _current_window, _widgets, _widget_counter
    
    if not _current_window:
        raise RuntimeError("No window created. Call createWindow first.")
    
    _widget_counter += 1
    widget_id = f"label_{_widget_counter}"
    
    label = tk.Label(_current_window, text=text)
    label.place(x=x, y=y, width=width, height=height)
    
    _widgets[widget_id] = {
        'widget': label,
        'type': 'label'
    }
    
    return widget_id

def addTextBox(x, y, width=200, height=30):
    """Add a text input box"""
    global _current_window, _widgets, _widget_counter
    
    if not _current_window:
        raise RuntimeError("No window created. Call createWindow first.")
    
    _widget_counter += 1
    widget_id = f"textbox_{_widget_counter}"
    
    entry = tk.Entry(_current_window)
    entry.place(x=x, y=y, width=width, height=height)
    
    _widgets[widget_id] = {
        'widget': entry,
        'type': 'textbox'
    }
    
    return widget_id

def addTextArea(x, y, width=300, height=200):
    """Add a multi-line text area"""
    global _current_window, _widgets, _widget_counter
    
    if not _current_window:
        raise RuntimeError("No window created. Call createWindow first.")
    
    _widget_counter += 1
    widget_id = f"textarea_{_widget_counter}"
    
    text_area = scrolledtext.ScrolledText(_current_window, wrap=tk.WORD)
    text_area.place(x=x, y=y, width=width, height=height)
    
    _widgets[widget_id] = {
        'widget': text_area,
        'type': 'textarea'
    }
    
    return widget_id

def addCheckbox(text, x, y):
    """Add a checkbox"""
    global _current_window, _widgets, _widget_counter
    
    if not _current_window:
        raise RuntimeError("No window created. Call createWindow first.")
    
    _widget_counter += 1
    widget_id = f"checkbox_{_widget_counter}"
    
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(_current_window, text=text, variable=var)
    checkbox.place(x=x, y=y)
    
    _widgets[widget_id] = {
        'widget': checkbox,
        'type': 'checkbox',
        'var': var
    }
    
    return widget_id

def addListBox(x, y, width=200, height=150):
    """Add a list box"""
    global _current_window, _widgets, _widget_counter
    
    if not _current_window:
        raise RuntimeError("No window created. Call createWindow first.")
    
    _widget_counter += 1
    widget_id = f"listbox_{_widget_counter}"
    
    listbox = tk.Listbox(_current_window)
    listbox.place(x=x, y=y, width=width, height=height)
    
    _widgets[widget_id] = {
        'widget': listbox,
        'type': 'listbox'
    }
    
    return widget_id

def setText(widget_id, text):
    """Set text of a widget"""
    global _widgets
    
    if widget_id not in _widgets:
        return False
    
    widget_info = _widgets[widget_id]
    widget = widget_info['widget']
    widget_type = widget_info['type']
    
    if widget_type == 'label':
        widget.config(text=text)
    elif widget_type == 'button':
        widget.config(text=text)
    elif widget_type == 'textbox':
        widget.delete(0, tk.END)
        widget.insert(0, text)
    elif widget_type == 'textarea':
        widget.delete('1.0', tk.END)
        widget.insert('1.0', text)
    
    return True

def getText(widget_id):
    """Get text from a widget"""
    global _widgets
    
    if widget_id not in _widgets:
        return ""
    
    widget_info = _widgets[widget_id]
    widget = widget_info['widget']
    widget_type = widget_info['type']
    
    if widget_type == 'label':
        return widget.cget('text')
    elif widget_type == 'button':
        return widget.cget('text')
    elif widget_type == 'textbox':
        return widget.get()
    elif widget_type == 'textarea':
        return widget.get('1.0', tk.END).strip()
    
    return ""

def setEnabled(widget_id, enabled):
    """Enable or disable a widget"""
    global _widgets
    
    if widget_id not in _widgets:
        return False
    
    widget = _widgets[widget_id]['widget']
    state = tk.NORMAL if enabled else tk.DISABLED
    widget.config(state=state)
    
    return True

def setVisible(widget_id, visible):
    """Show or hide a widget"""
    global _widgets
    
    if widget_id not in _widgets:
        return False
    
    widget = _widgets[widget_id]['widget']
    
    if visible:
        widget.place()
    else:
        widget.place_forget()
    
    return True

def onClick(widget_id, callback):
    """Set click event handler for a widget"""
    global _widgets
    
    if widget_id not in _widgets:
        return False
    
    widget_info = _widgets[widget_id]
    widget = widget_info['widget']
    
    # Store callback
    widget_info['callback'] = callback
    
    # Set command
    def handler():
        if widget_info['callback']:
            widget_info['callback']()
    
    if widget_info['type'] == 'button':
        widget.config(command=handler)
    
    return True

def showMessage(title, message):
    """Show a message dialog"""
    messagebox.showinfo(title, message)

def showError(title, message):
    """Show an error dialog"""
    messagebox.showerror(title, message)

def showWarning(title, message):
    """Show a warning dialog"""
    messagebox.showwarning(title, message)

def askYesNo(title, message):
    """Show yes/no dialog"""
    return messagebox.askyesno(title, message)

def askOkCancel(title, message):
    """Show OK/Cancel dialog"""
    return messagebox.askokcancel(title, message)

def openFileDialog(title="Open File"):
    """Show open file dialog"""
    return filedialog.askopenfilename(title=title)

def saveFileDialog(title="Save File"):
    """Show save file dialog"""
    return filedialog.asksaveasfilename(title=title)

def addListItem(widget_id, item):
    """Add item to list box"""
    global _widgets
    
    if widget_id not in _widgets:
        return False
    
    widget_info = _widgets[widget_id]
    if widget_info['type'] != 'listbox':
        return False
    
    widget_info['widget'].insert(tk.END, item)
    return True

def clearList(widget_id):
    """Clear all items from list box"""
    global _widgets
    
    if widget_id not in _widgets:
        return False
    
    widget_info = _widgets[widget_id]
    if widget_info['type'] != 'listbox':
        return False
    
    widget_info['widget'].delete(0, tk.END)
    return True

def getSelectedItem(widget_id):
    """Get selected item from list box"""
    global _widgets
    
    if widget_id not in _widgets:
        return None
    
    widget_info = _widgets[widget_id]
    if widget_info['type'] != 'listbox':
        return None
    
    selection = widget_info['widget'].curselection()
    if selection:
        return widget_info['widget'].get(selection[0])
    
    return None

def isChecked(widget_id):
    """Check if checkbox is checked"""
    global _widgets
    
    if widget_id not in _widgets:
        return False
    
    widget_info = _widgets[widget_id]
    if widget_info['type'] != 'checkbox':
        return False
    
    return widget_info['var'].get()

def setChecked(widget_id, checked):
    """Set checkbox state"""
    global _widgets
    
    if widget_id not in _widgets:
        return False
    
    widget_info = _widgets[widget_id]
    if widget_info['type'] != 'checkbox':
        return False
    
    widget_info['var'].set(checked)
    return True

def show(window_id=None):
    """Show the window and start event loop"""
    global _current_window
    
    if _current_window:
        _current_window.mainloop()

def close(window_id=None):
    """Close the window"""
    global _current_window
    
    if _current_window:
        _current_window.destroy()
        _current_window = None

def setBackgroundColor(widget_id, color):
    """Set background color of widget"""
    global _widgets
    
    if widget_id not in _widgets:
        return False
    
    widget = _widgets[widget_id]['widget']
    widget.config(bg=color)
    return True

def setForegroundColor(widget_id, color):
    """Set foreground/text color of widget"""
    global _widgets
    
    if widget_id not in _widgets:
        return False
    
    widget = _widgets[widget_id]['widget']
    widget.config(fg=color)
    return True

def setFont(widget_id, font_name, size):
    """Set font of widget"""
    global _widgets
    
    if widget_id not in _widgets:
        return False
    
    widget = _widgets[widget_id]['widget']
    widget.config(font=(font_name, size))
    return True
