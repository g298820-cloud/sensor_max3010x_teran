from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# Dirección del sensor AHT10
AHT10_ADDR = 0x38

# Configuración del bus I2C para OLED y AHT10
i2c_oled = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)   # Bus I2C1 → OLED
oled = SSD1306_I2C(128, 64, i2c_oled)

i2c_sensor = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000) # Bus I2C0 → AHT10

def leer_aht10():
    # Reset e inicialización
    i2c_sensor.writeto(AHT10_ADDR, b'\xBA')
    time.sleep_ms(20)
    i2c_sensor.writeto(AHT10_ADDR, b'\xE1\x08\x00')
    time.sleep_ms(20)

    # Comando de medición
    i2c_sensor.writeto(AHT10_ADDR, b'\xAC\x33\x00')
    time.sleep_ms(100)

    # Leer 6 bytes
    data = i2c_sensor.readfrom(AHT10_ADDR, 6)
    print("Datos crudos:", [hex(x) for x in data])

    # Calcular humedad y temperatura
    humidity_raw = ((data[1] << 12) | (data[2] << 4) | (data[3] >> 4))
    humidity = humidity_raw * 100 / 1048576
    temp_raw = ((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]
    temperature = temp_raw * 200 / 1048576 - 50

    return temperature, humidity

# Bucle principal
while True:
    temp, hum = leer_aht10()
    print(f"Temperatura: {temp:.2f} °C  |  Humedad: {hum:.2f} %")

    # Mostrar en OLED
    oled.fill(0)
    oled.text("AHT10 Sensor", 10, 0)
    oled.text(f"Temp: {temp:.2f} C", 0, 20)
    oled.text(f"Hum:  {hum:.2f} %", 0, 40)
    oled.show()

    time.sleep(2)  # Actualizar cada 2 segundos
