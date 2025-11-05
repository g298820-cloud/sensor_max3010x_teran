# <NOME DO SENSOR> — Sensores na BitDogLab

**Dupla:** Gustavo Santos Terán Rupay (298820 / @gustavosantosteran)  
**Turma:** EA801 — 2025S2  
**Repositório:** https://github.com/g298820-cloud/sensor_max3010x_teran

## 1. Descrição do sensor
- Fabricante / modelo: GY-MAX3010X
- Princípio de funcionamento: o sensor emite luz vermelha e infravermelha e mede a variação da luz refletida nos tecidos para estimar a pulsação e a saturação de oxigênio no sangue
- Tensão/consumo típicos: 3,3 V a 5 V
  
- Faixa de medição / resolução:
  Frequência cardíaca: 30–240 bpm
  SpO₂: 70–100 % (precisão ±2 %)
  <img width="703" height="153" alt="image" src="https://github.com/user-attachments/assets/02be8f73-e8e9-4c44-8fd6-c87fac4d77dc" />

  
- Datasheet (URL): MAX30102 Datasheet – Analog Devices 

## 2. Conexões de hardware
- Tabela indicando as conexões entre BitDogLab e sensor:


# max30102.py – Biblioteca simplificada para MicroPython

import time
from micropython import const

_MAX30102_ADDR = const(0x57)
_PART_ID = const(0xFF)
_EXPECTED_PART_ID = const(0x15)
_REG_INTR_STATUS_1 = const(0x00)
_REG_INTR_STATUS_2 = const(0x01)
_REG_FIFO_WR_PTR = const(0x04)
_REG_FIFO_RD_PTR = const(0x06)
_REG_FIFO_DATA = const(0x07)
_REG_MODE_CONFIG = const(0x09)
_REG_SPO2_CONFIG = const(0x0A)
_REG_LED1_PA = const(0x0C)
_REG_LED2_PA = const(0x0D)
_REG_MULTI_LED_CTRL1 = const(0x11)
_REG_MULTI_LED_CTRL2 = const(0x12)
_REG_TEMP_INT = const(0x1F)
_REG_TEMP_FRAC = const(0x20)

class MAX30102:
    def __init__(self, i2c, addr=_MAX30102_ADDR):
        self.i2c = i2c
        self.addr = addr

    def check_part_id(self):
        part_id = self.i2c.readfrom_mem(self.addr, _PART_ID, 1)[0]
        return part_id == _EXPECTED_PART_ID

    def setup_sensor(self):
        self.i2c.writeto_mem(self.addr, _REG_MODE_CONFIG, b'\x03')
        self.i2c.writeto_mem(self.addr, _REG_SPO2_CONFIG, b'\x27')
        self.i2c.writeto_mem(self.addr, _REG_LED1_PA, b'\x24')
        self.i2c.writeto_mem(self.addr, _REG_LED2_PA, b'\x24')

    def read_sequential(self, n=1):
        red_buf = []
        ir_buf = []
        for _ in range(n):
            data = self.i2c.readfrom_mem(self.addr, _REG_FIFO_DATA, 6)
            red = (data[0]<<16 | data[1]<<8 | data[2]) & 0x3FFFF
            ir = (data[3]<<16 | data[4]<<8 | data[5]) & 0x3FFFF
            red_buf.append(red)
            ir_buf.append(ir)
        return red_buf, ir_buf

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/c0056803-fe4c-45ed-9acb-35768cb9c72d" />

# main.py — prueba básica del sensor MAX30102 (GY-MAX3010X)

from machine import Pin, I2C
import time
from max30102 import MAX30102

# --- Configurar bus I2C ---
# BitDogLab / Pico: SDA=GP6, SCL=GP7
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)

print("🔍 Escaneando bus I2C...")
devices = i2c.scan()
print("Dispositivos encontrados:", devices)

if 0x57 not in devices:
    print("No se detectó el sensor MAX30102.")
    print("Verifica conexiones: VIN→3V3, GND→GND, SDA→GP6, SCL→GP7")
else:
    print("Sensor detectado en dirección 0x57")

    # --- Inicializar sensor ---
    sensor = MAX30102(i2c)
    if sensor.check_part_id():
        print("ID correcto del chip MAX30102")
    else:
        print("Error: ID incorrecto (revisa conexiones o modelo)")

    sensor.setup_sensor()
    print("Leyendo valores RAW (RED e IR)... coloca el dedo sobre el sensor")

    # --- Lectura continua ---
    while True:
        red, ir = sensor.read_sequential(1)
        print("RED:", red[-1], "IR:", ir[-1])
        time.sleep(0.5)




- Observações (resistores, alimentação externa, níveis lógicos):




**Tabela de conexões (imagem em `docs/`):**  
![conexoes](docs/conexoes.jpg)

## 3. Dependências
- MicroPython/C versão:
- Bibliotecas utilizadas:
- Como instalar (passo a passo):

## 4. Como executar
```bash
# MicroPython (Thonny): copiar src/main.py para a placa e rodar
# C (Pico SDK): ver docs/compilacao.md
```

## 5. Exemplos de uso
- `src/exemplo_basico.py` — leitura bruta  
- `src/exemplo_filtrado.py` — leitura com média móvel  
- `test/` — códigos de teste com instruções  

## 6. Resultados e validação
- Prints/plots, fotos do setup, limitações, ruídos, dicas.

## 7. Licença
- Ver arquivo `LICENSE`.

---

> **Checklist de entrega**
> - [ ] README preenchido  
> - [ ] Foto/diagrama em `docs/`  
> - [ ] Código comentado em `src/`  
> - [ ] Testes em `test/` com instruções  
> - [ ] `relatorio.md` com lições aprendidas

## 📁 7. Estrutura do Repositório

O projeto segue o padrão definido pela disciplina EA801 — Sistemas Embarcados, 
visando padronizar as entregas e facilitar o reuso dos códigos e documentação.

Todos os arquivos de código devem estar em src/.
Diagramas, fotos, gráficos e documentos vão em docs/.
Scripts ou logs de teste ficam em test/.
O relatório técnico (relatorio.md) documenta todo o processo de engenharia.

Mantenha os nomes dos arquivos em minúsculas, sem acentos ou espaços, usando _ ou -.

```text
template_sensor/
├── README.md          → Descrição completa do projeto (sensor, ligações, execução e checklist)
├── relatorio.md       → Relatório técnico da dupla (resultados, análise e conclusões)
├── LICENSE            → Licença MIT de uso e distribuição
├── .gitignore         → Regras para ignorar arquivos temporários e binários
│
├── docs/              → Documentação e mídias
│   ├── ligacao.jpg    → Diagrama ou foto da ligação na BitDogLab
│   ├── esquema.pdf    → Esquemático opcional
│   └── outros arquivos de apoio
│
├── src/               → Códigos-fonte principais
│   ├── main.py        → Código principal (MicroPython)
│   ├── main.c         → Versão alternativa (C / Pico SDK)
│   ├── exemplos/      → Códigos ilustrativos adicionais
│   └── bibliotecas/   → Drivers, módulos auxiliares
│
└── test/              → Testes e validações
    ├── test_basico.py → Teste de leitura e resposta do sensor
    ├── test_ruido.py  → Avaliação de ruído ou estabilidade
    └── logs/          → Registros experimentais, dados e gráficos

```
