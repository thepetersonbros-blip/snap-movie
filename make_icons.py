"""Draws the Snap Movie app icon (a toy camera) at every size the iPad wants."""
from PIL import Image, ImageDraw

S = 2048  # draw big, shrink down for smooth edges
img = Image.new("RGB", (S, S))
top, bot = (123, 92, 255), (42, 26, 130)
d = ImageDraw.Draw(img)
for y in range(S):
    t = y / (S - 1)
    d.line([(0, y), (S, y)], fill=tuple(round(a + (b - a) * t) for a, b in zip(top, bot)))

def r(v):
    return round(v * S / 1024)

white, ink, red, amber = (255, 255, 255), (43, 29, 107), (255, 77, 94), (245, 165, 36)
d.rounded_rectangle([r(330), r(250), r(560), r(380)], radius=r(40), fill=white)      # top bump
d.rounded_rectangle([r(160), r(330), r(864), r(800)], radius=r(96), fill=white)      # body
d.ellipse([r(512 - 200), r(565 - 200), r(512 + 200), r(565 + 200)], fill=ink)        # lens
d.ellipse([r(512 - 150), r(565 - 150), r(512 + 150), r(565 + 150)], fill=red)
d.ellipse([r(512 - 88), r(565 - 88), r(512 + 88), r(565 + 88)], fill=ink)
d.ellipse([r(440 - 30), r(500 - 30), r(440 + 30), r(500 + 30)], fill=white)          # shine
d.rounded_rectangle([r(700), r(385), r(800), r(440)], radius=r(16), fill=amber)      # flash

for size in (1024, 512, 192, 180):
    img.resize((size, size), Image.LANCZOS).save(f"icon-{size}.png")
print("icons done")
