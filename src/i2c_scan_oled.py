from machine import Pin, I2C
import time
from ssd1306 import SSD1306_I2C
AHT10_ADDR = 0x38
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

# Reset
i2c.writeto(AHT10_ADDR, b'\xBA')
time.sleep_ms(20)

# Inicialización
i2c.writeto(AHT10_ADDR, b'\xE1\x08\x00')
time.sleep_ms(20)

# Medición
i2c.writeto(AHT10_ADDR, b'\xAC\x33\x00')
time.sleep_ms(100)

# Leer datos
data = i2c.readfrom(AHT10_ADDR, 6)
print("Datos crudos:", [hex(x) for x in data])

# Procesar
humidity_raw = ((data[1] << 12) | (data[2] << 4) | (data[3] >> 4))
humidity = humidity_raw * 100 / 1048576
temp_raw = ((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]
temperature = temp_raw * 200 / 1048576 - 50

print("Temperatura:", round(temperature, 2), "°C")
print("Humedad:", round(humidity, 2), "%")


