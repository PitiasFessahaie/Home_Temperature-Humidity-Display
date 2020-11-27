from machine import Pin,I2C
from time import sleep
import dht
from esp8266_i2c_lcd import I2cLcd


i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
d = dht.DHT11(Pin(0))



while 1:
    lcd.hide_cursor()
    lcd.putstr("**Pitias Home**\nTemp & Humidity")  # 16 characters
    sleep(1)
    lcd.clear()
    sleep(2)
    d.measure()
    lcd.putstr("Temperature :")
    lcd.putstr(str(d.temperature())) # eg. 23 (°C)
    lcd.putstr("C")
    sleep(1)
    lcd.putstr("Humidity :")
    lcd.putstr(str(d.humidity()))    # eg. 41 (% RH)
    lcd.putstr("% RH")
    sleep(4)
    lcd.clear()