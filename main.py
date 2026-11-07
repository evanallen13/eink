from PIL import Image, ImageDraw, ImageFont
import epaper # From the waveshare-epaper package

# 1. Initialize the specific display model
epd = epaper.epaper('epd2in9_V2').EPD()
epd.init()
epd.Clear()

# 2. Draw in landscape orientation, then rotate to the panel's native dimensions
# E-ink requires '1' (1-bit pixels, black and white) or 'L' for grayscale
image = Image.new('1', (epd.height, epd.width), 255)
draw = ImageDraw.Draw(image)

# 3. Draw text, lines, or shapes using Pillow
font = ImageFont.load_default()
draw.text((50, 50), '                  Hello, e-Ink!', font=font, fill=0)
draw.line([(0, 30), (image.width, 30)], fill=0, width=2)
image = image.transpose(Image.Transpose.ROTATE_90)

# 4. Push the buffer to the physical panel
epd.display(epd.getbuffer(image))

# 5. Put the display into deep sleep to protect the hardware
epd.sleep()
