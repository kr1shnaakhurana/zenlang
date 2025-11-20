# ZenLang for Visual Studio Code

Official Visual Studio Code extension for ZenLang programming language.

## Features

- **Syntax Highlighting** - Full syntax highlighting for ZenLang code
- **File Icon** - Custom ZenLang icon for `.zen` files
- **Auto-completion** - Bracket and quote auto-closing
- **Code Folding** - Fold code blocks
- **Comment Support** - Line (`**`) and block (`/* */`) comments

## Installation

### Method 1: Install from VSIX (Recommended)

1. Open VS Code
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
3. Type "Extensions: Install from VSIX"
4. Select the `zenlang-1.0.0.vsix` file

### Method 2: Install from Folder

1. Copy the `vscode-extension` folder to:
   - **Windows**: `%USERPROFILE%\.vscode\extensions\zenlang-1.0.0`
   - **Mac/Linux**: `~/.vscode/extensions/zenlang-1.0.0`

2. Restart VS Code

### Method 3: Development Mode

1. Open the `vscode-extension` folder in VS Code
2. Press `F5` to launch Extension Development Host
3. Open a `.zen` file to test

## Usage

Once installed, all `.zen` files will automatically:
- Show the ZenLang icon in the file explorer
- Have syntax highlighting
- Support code folding and auto-completion

## Syntax Highlighting

The extension highlights:
- **Keywords**: `if`, `else`, `while`, `for`, `funct`, `class`, `new`, etc.
- **Comments**: `**` (line) and `/* */` (block)
- **Strings**: Double and single quoted
- **Numbers**: Integer and decimal
- **Functions**: Function names and calls
- **Classes**: Class definitions and instantiation
- **Operators**: Arithmetic, logical, and comparison

## File Icon

The ZenLang icon (purple Z) will appear next to `.zen` files in:
- VS Code file explorer
- Editor tabs
- File search results

## Example Code

```zen
** ZenLang Example
.include <zenout>

class Calculator {
    public funct add(a, b) {
        return a + b;
    }
}

calc = new Calculator();
result = calc.add(5, 3);
zenout.console("Result: " + result);
```

## Building VSIX Package

To create a distributable VSIX package:

```bash
npm install -g vsce
cd vscode-extension
vsce package
```

This creates `zenlang-1.0.0.vsix` that can be shared and installed.

## Configuration

No additional configuration needed! The extension works out of the box.

## Known Issues

None currently. Please report issues on GitHub.

## Release Notes

### 1.0.0

- Initial release
- Syntax highlighting for ZenLang
- Custom file icon
- Auto-completion support
- Code folding

## Contributing

Contributions welcome! Please submit pull requests on GitHub.

## License

MIT License

## Links

- [ZenLang Documentation](../README.md)
- [ZenLang Syntax Guide](../SYNTAX.md)
- [ZenLang Examples](../examples/)

---

**Enjoy coding in ZenLang!** 🚀
