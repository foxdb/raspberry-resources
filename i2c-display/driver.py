# http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/

import I2C_LCD_driver
from time import sleep

lcd_display = I2C_LCD_driver.lcd()

# Display 10 seconds then turn backlight off
# TODO: handle backlight management in fn params


def display(first_line, second_line):
    lcd_display.lcd_clear()
    lcd_display.lcd_display_string(first_line, 1)
    lcd_display.lcd_display_string(second_line, 2)
    sleep(10)
    lcd_display.backlight(0)
