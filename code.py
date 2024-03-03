import board, busio, displayio, os, time
import adafruit_displayio_ssd1306
import triangle
import Main

model = 'cube.obj'
renderer = Main.gl(128,64, 55, 1000, 0.1)
cube = Main.object(model,0,0,1,0,35,0, 3, 3, 3, None)

renderer.camera_absolute(_camera_x = 0, _camera_y = 0, _camera_z = 10, _camera_angle_x = 0, _camera_angle_y = 0, _camera_angle_z = 0)

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

FPS = 100
FPS_DELAY = 1 / FPS

displayio.release_displays()

board_type = os.uname().machine

if 'Pico' in board_type:
    sda, scl = board.GP0, board.GP1

i2c = busio.I2C(scl, sda)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

# Make the display context
splash = displayio.Group()
display.show(splash)

# Make a background color fill
color_bitmap = displayio.Bitmap(SCREEN_WIDTH, SCREEN_HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000
bg_sprite = displayio.TileGrid(color_bitmap, x=0, y=0, pixel_shader=color_palette)
splash.append(bg_sprite)

last_update_time = 0
now = 0

while True:
    # update time variable
    now = time.monotonic()

    # check if the delay time has passed since the last game update
    if last_update_time + FPS_DELAY <= now:
        splash = displayio.Group()
        triangles = renderer.new_frame()
        renderer.move_camera(_camera_angle_z = 1, _camera_angle_y=2)
        for tri in triangles:
            splash.append(triangle.Triangle(tri[0], tri[1], tri[2], tri[3], tri[4], tri[5],outline=0xFFFFFF))
            pass
        display.show(splash)
        last_update_time = now