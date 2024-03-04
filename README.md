# Minimal Graphics library

## Table of Contents

+ [About](#about)
+ [Getting Started](#getting_started)
+ [Usage](#usage)

## <a name = "about">About</a>

This is another small project I work on in my free time, it's a port of my 3D renderer to a pi pico with a ssd1306 128*64 monochrome oled display

## <a name = "getting_started">Getting Started</a>

To get this example running just copy all files into your pi pico preinstalled with circut python

## <a name = "usage">Usage</a>

### Changing displayed object:
just copy the object over to the pico and change the model attribute in code.py just like you would in the main library:
```
model = Local_model_path_string
```
### Rotating/moving the object:
To rotate the object short GPIO pins 16-21.
To move the object short GPIO pins 10-15.
