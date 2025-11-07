https://github.com/BitDogLab/BitDogLab/blob/main/softwares/I2C/teste%20e%20Scam%20de%20I2C%20V2A%20mostrando%20no%20OLED%20%20funcionando.py


# <AHT10 — Sensor de umedade y Temperatura en BitDogLab> — Sensores na BitDogLab

**Dupla:** Gustavo Santos Terán Rupay (298820 / @gustavosantosteran)  
**Turma:** EA801 — 2025S2  
**Repositório:** https://github.com/g298820-cloud/sensor_aht10_teran

## 1. Descrição do sensor
- Fabricante / modelo: Aosong (ASAIR) AHT10 
- Princípio de funcionamento: O AHT10 é um sensor digital de umidade e temperatura que utiliza um polímero capacitivo para medir a umidade relativa e um termistor interno para a temperatura. A conversão analógico-digital é realizada internamente, e os dados são transmitidos via I²C.
- Tensão/consumo típicos: 1.8 V – 3.6 V, consumo típico de 0.5 mA em operação normal. O consumo em modo de baixa potência é de aproximadamente 0.2 µA.
- Faixa de medição / resolução:
  Umidade relativa: 0 – 100 % RH (±2 % RH típico)
  Temperatura: –40 °C – 85 °C (±0.3 °C típico)
  Resolução: 0.024 % RH / 0.01 °C
  
- Datasheet (URL): [https://server4.eca.ir/eshop/AHT10/Aosong_AHT10_en_draft_0c.pdf]

## 2. Conexões de hardware
- Tabela indicando as conexões entre BitDogLab e sensor:

  <img width="1130" height="558" alt="image" src="https://github.com/user-attachments/assets/f3db34bd-29a3-407c-8a48-95ad635cbc58" />

- Observações (resistores, alimentação externa, níveis lógicos):
  É recomendado o uso de resistores de pull-up (4.7 kΩ – 10 kΩ) nos pinos SDA e SCL. 
  A comunicação segue o protocolo I²C padrão (100 kHz – 400 kHz).
  
**Tabela de conexões (imagem em `docs/`):**

![Conexões do sensor AHT10](‎docs/conexoes_aht10.jpg)

## 3. Dependências
- MicroPython/C versão:
  Placa: BitDogLab (Raspberry Pi Pico W / RP2040)
  Firmware: MicroPython v1.22.1 ou superior
  IDE: Thonny (versão igual ou superior 4.1.0)
  
- Bibliotecas utilizadas:
  machine (interna) : Pin, I2C 
  time (interna) : sleep_ms
  ssd1306 (externa) : SSD1306_I2C
  O projeto utiliza tanto módulos nativos do MicroPython quanto uma biblioteca externa para o display OLED.
    
- Como instalar (passo a passo):
  

  

  ssd1306 (externa) OLED
  https://raw.githubusercontent.com/stlehmann/micropython-ssd1306/master/ssd1306.py

## 4. Como executar
```bash
# MicroPython (Thonny): copiar src/main.py para a placa e rodar

1. Conecte a placa BitDogLab via USB.

2. Carregue os arquivos para a placa:
   - Copie o arquivo `ssd1306.py` para a pasta `/lib/` da placa.  
   - Copie os scripts de teste (`i2c_scan.py`, `i2c_scan_oled.py` e `aht10_prueba_2.py`) para a
     pastaprincipal da placa ou dentro de `/src/`.

3. **Etapa1** – Verificar dispositivos I²C:
   - Execute o arquivo `i2c_scan.py` no Thonny.  
   - O terminal exibirá os endereços detectados,
     como:
     Dispositivo encontrado no endereço: 0x38
     Dispositivo encontrado no endereço: 0x3C

     Confirmando que o AHT10 (0x38) e o SSD1306 (0x3C) estão sendo reconhecidos corretamente.

4. **Etapa2** – Testar exibição no OLED:
   - Execute `i2c_scan_oled.py`.  
   - Os endereços detectados aparecerão **diretamente no display OLED**, validando a comunicação I²C com      o módulo.

5. **Etapa3** – Rodar o código principal:
   - Execute `aht10_prueba_2.py`.  
   - O programa fará a leitura contínua dos valores de temperatura e umidade do **AHT10** e exibirá:
   - No terminal do Thonny:
       Temperatura: 23.0 °C
       Umidade: 61.5 %
   - No display OLED SSD1306, com atualização automática a cada 2 segundos.


## 5. Exemplos de uso

- `src/i2c_scan.py` (teste)
  
  realiza a varredura dos dispositivos I²C conectados nos barramentos I2C0 e I2C1,
  exibindo no terminal os endereços detectados (0x38, 0x3c, 0x40).
  Utilizado para confirmar o reconhecimento do sensor AHT10 e do display OLED.

- `src/ssd1306.py`
  Biblioteca que implementa todas as funções de controle do display
  OLED SSD1306 via protocolo I²C.
  Inclui métodos como fill(), text(), pixel(), e show() que permitem desenhar,
  escrever texto e atualizar o conteúdo da tela.
  Esta biblioteca é utilizada pelos demais scripts (como i2c_scan_oled.py e
  aht_prueba_2.py) para exibir informações em tempo real no display OLED conectado ao
  BitDogLab.

- `src/i2c_scan_oled.py` (teste)
  
  mostra no display OLED SSD1306 os endereços I²C detectados nos dois barramentos.
  Serve para testar a comunicação entre o microcontrolador RP2040 e o módulo OLED,
  exibindo o resultado diretamente na tela.
  
- `src/aht10_prueba_2.py`
   
  Lê continuamente os dados de temperatura e umidade do sensor
  AHT10, mostrando os valores em tempo real tanto no terminal quanto no display OLED.
  Exemplo final de integração entre sensor e display, com leituras estáveis como
  23.0 °C e 61.5 % atualizadas a cada 2 segundos.
  

## 6. Resultados e validação
- Prints/plots, fotos do setup, limitações, ruídos, dicas.

## 7. Licença
- Ver arquivo `LICENSE`.

MIT License
Copyright (c) 2025 Gustavo Santos Terán Rupay

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
