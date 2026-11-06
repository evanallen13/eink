import sys
from PIL import Image, ImageDraw, ImageFont
import epaper # From the waveshare-epaper package

# 1. Initialize the specific display model
epd = epaper.epaper('epd2in9_V2').EPD()
epd.init()
epd.Clear()

# 2. Create a blank image canvas in memory matching the screen dimensions
# E-ink requires '1' (1-bit pixels, black and white) or 'L' for grayscale
image = Image.new('1', (epd.width, epd.height), 255) 
draw = ImageDraw.Draw(image)

# 3. Draw text, lines, or shapes using Pillow
font = ImageFont.load_default()
draw.text((10, 10), 'Hello, e-Ink!', font=font, fill=0)
draw.line([(0, 30), (epd.width, 30)], fill=0, width=2)

# 4. Push the buffer to the physical panel
epd.display(epd.getbuffer(image))

# 5. Put the display into deep sleep to protect the hardware
epd.sleep()
