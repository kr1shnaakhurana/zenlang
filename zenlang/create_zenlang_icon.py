"""Create ZenLang icon file"""
from PIL import Image, ImageDraw, ImageFont
import os

# Create a 256x256 image with transparent background
size = 256
img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw a modern "Z" logo
# Background circle
circle_color = (138, 43, 226, 255)  # Purple
draw.ellipse([20, 20, 236, 236], fill=circle_color)

# Draw "Z" in white
z_color = (255, 255, 255, 255)
# Top horizontal line
draw.rectangle([60, 60, 196, 85], fill=z_color)
# Diagonal line
points = [(196, 85), (60, 171), (85, 196), (221, 110)]
draw.polygon(points, fill=z_color)
# Bottom horizontal line
draw.rectangle([60, 171, 196, 196], fill=z_color)

# Save as ICO file (Windows icon format)
icon_path = os.path.join(os.path.dirname(__file__), 'zenlang.ico')
img.save(icon_path, format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])

print(f"ZenLang icon created: {icon_path}")

# Also save as PNG for reference
png_path = os.path.join(os.path.dirname(__file__), 'zenlang_icon.png')
img.save(png_path, format='PNG')
print(f"ZenLang PNG icon created: {png_path}")
