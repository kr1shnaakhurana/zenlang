# ZenLang Logo and Icon

This folder contains the ZenLang logo and icon files.

## Files Needed

- `zenlang.ico` - Windows icon file (required for file association)
- `zenlang.png` - PNG version of the logo
- `zenlang.svg` - Vector version (optional)

## How to Create the Icon

### Quick Method (Automated):

1. Run the PowerShell script from the parent directory:
   ```powershell
   .\create_simple_icon.ps1
   ```

2. This will create `zenlang.png` in this folder

3. Convert the PNG to ICO format:
   - Visit: https://convertio.co/png-ico/
   - Upload `zenlang.png`
   - Download `zenlang.ico`
   - Save it in this folder

### Manual Method:

1. Create a 512x512 pixel image with your design
2. Use these recommended colors:
   - **Purple**: #8A2BE2 (BlueViolet)
   - **Orange**: #FF6B35 (Fire theme)
   - **Blue**: #00BCD4 (Cyan)

3. Design ideas:
   - Large "Z" letter
   - Zen circle (enso)
   - Flame icon 🔥
   - Code brackets with Z

4. Convert to .ico format using online tools

## Icon Specifications

- **Size**: 256x256 or 512x512 pixels
- **Format**: ICO for Windows
- **Transparency**: Recommended
- **Multiple sizes**: Include 16x16, 32x32, 48x48, 256x256 in the ICO file

## After Creating the Icon

1. Place `zenlang.ico` in this folder
2. Run `setup_file_association.bat` as Administrator
3. Restart Windows Explorer or log out/in
4. All .zen files will now show your custom icon!

## Design Guidelines

### Colors
- Primary: Purple/Violet (#8A2BE2)
- Secondary: White (#FFFFFF)
- Accent: Orange/Red (#FF6B35)

### Style
- Modern and minimalist
- Clear and recognizable at small sizes
- Professional appearance

### Inspiration
- Zen philosophy (simplicity, elegance)
- Fire/energy (🔥 emoji from tagline)
- Code/programming (technical aspect)

---

**ZenLang** - Simple, Elegant, Powerful 🔥
