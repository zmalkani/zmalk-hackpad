import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.peg_oled import Display, SSD1306

keyboard = KMKKeyboard()

# Pin Configuration
keyboard.pins = [board.D9, board.D10, board.D11]


# Encoder Configuration
encoder = EncoderHandler()
keyboard.modules.append(encoder)
encoder.pins = ((keyboard.pin_a, keyboard.pin_b, None, False))

# OLED Configuration
i2c_bus = board.I2C()
oled = Display(display=SSD1306(i2c=i2c_bus, device_address=0x3C))
keyboard.extensions.append(oled)

# Keymap
keyboard.keymap = [
    [KC.F7, KC.F8, KC.F9]
]

# Encoder Rotation (Left = Vol Down, Right = Vol Up)
encoder.map = [
    ((KC.VOLD, KC.VOLU),)
]

if __name__ == '__main__':
    keyboard.go()