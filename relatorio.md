# Relatório Técnico da Dupla

Disciplina: EA801 — Sistemas Embarcados
Dupla: Gustavo Santos Terán Rupay (RA: 298820 / @g298820@g.unicamp.br)
Período: 2025S2
Placa: BitDogLab (Raspberry Pi Pico W / RP2040)
Sensor: AHT10 — Sensor de Umidade e Temperatura

## 1. Escopo
Descreva de forma clara o propósito do experimento ou desenvolvimento realizado, delimitando o escopo do trabalho e os objetivos técnicos a serem atingidos.  
Inclua também os critérios de sucesso utilizados para validar o funcionamento do sistema.

O presente experimento tem como escopo o desenvolvimento, integração e validação de um sistema embarcado baseado na placa BitDogLab (RP2040), utilizando o sensor digital AHT10 para medições de umidade relativa do ar e temperatura ambiente, com exibição dos dados em tempo 
real no display OLED SSD1306, através da comunicação I²C.

**Os objetivos específicos**

-Implementar a comunicação correta entre o AHT10 e o microcontrolador RP2040 via protocolo I²C.
-Exibir continuamente os valores de temperatura e umidade no terminal e no display OLED.
-Validar o funcionamento do sistema por meio de scripts de teste (test_basico.py e test_ruido.py).
-Avaliar a estabilidade das leituras, observando variações naturais e possíveis ruídos.

**O trabalho procura consolidar o entendimento dos seguintes conceitos técnicos:**

-Configuração e utilização de múltiplos barramentos I²C em sistemas embarcados.
-Leitura de sensores digitais e interpretação de dados binários.
-Controle e atualização de um display gráfico (SSD1306) utilizando bibliotecas externas em MicroPython.
-Estruturação modular do código, com arquivos principais e scripts de teste.

**Os critérios de sucesso considerados para validação**

-Detecção do sensor AHT10 no endereço 0x38 e do display OLED no endereço 0x3C durante o escaneamento I²C.
-Exibição correta e contínua das medições no terminal e no OLED, com atualização a cada 2 segundos.
-Estabilidade das leituras com variação máxima de ±0.3 °C para temperatura e ±2 %RH para umidade.

## 2. Metodologia e Implementação
Apresente os procedimentos adotados, incluindo a arquitetura do sistema, estratégias de programação, bibliotecas utilizadas e justificativas de projeto.  
Se aplicável, descreva o esquema de ligação elétrica, o protocolo de comunicação, as rotinas de aquisição e processamento de dados e o fluxo lógico do programa.  

**Sugestão de tópicos a abordar:**
- Diagrama de blocos e descrição funcional dos módulos;  
- Linguagem e ambiente de desenvolvimento utilizados;  
- Configurações específicas da BitDogLab e periféricos;  
- Estratégias de depuração e calibração.

2.1 Diagrama de blocos e descrição funcional dos módulos

<img width="346" height="459" alt="image" src="https://github.com/user-attachments/assets/38c67d2f-8ae0-4069-9f40-2f90ea54808c" />


O funcionamento geral do sistema é representado no diagrama de blocos, que descreve o fluxo de dados desde as medições físicas realizadas pelo sensor AHT10 até a exibição final dos resultados no display OLED e no terminal serial.

O sistema é dividido em módulos funcionais integrados via barramentos digitais

-Ambiente: representa o meio físico onde são medidas as variáveis de temperatura (T) e umidade relativa (UR).

-Sensor AHT10: converte as grandezas físicas do ambiente em sinais digitais utilizando conversão analógico-digital interna. A comunicação é feita via protocolo I²C, no endereço 0x38.

-Comunicação I²C0: o sensor AHT10 é conectado à BitDogLab por meio do barramento I²C0 (SDA = GP0, SCL = GP1), transmitindo os dados digitais para o microcontrolador RP2040.

-Processamento (RP2040 – BitDogLab): o microcontrolador processa os dados recebidos, aplica as fórmulas de conversão para °C e %UR e atualiza as saídas (display OLED e terminal serial).

-Controle: uma rotina de temporização (time.sleep(2)) define o intervalo entre leituras, garantindo atualização contínua e estável a cada 2 segundos.

-Comunicação I²C1: o display OLED SSD1306 está conectado ao barramento I²C1 (SDA = GP14, SCL = GP15) para exibir as medições processadas.

-Display OLED: apresenta em tempo real os valores de temperatura e umidade processados, utilizando a biblioteca externa ssd1306.py.

-Terminal Serial (Thonny IDE): exibe os mesmos dados em formato de texto via porta USB, permitindo depuração e monitoramento das leituras.

-Saída final: os resultados são exibidos simultaneamente no display e no terminal, com atualização contínua a cada 2 segundos.

-Essa arquitetura modular garante simplicidade, estabilidade e clareza no fluxo de dados, desde a aquisição até a exibição final das medições.










---

## 3. Resultados e Análise
Apresente os principais resultados obtidos, acompanhados de gráficos, tabelas ou imagens que sustentem a análise.  
Discuta o comportamento observado, eventuais desvios em relação ao esperado e hipóteses para as causas identificadas.  

**Inclua, sempre que possível:**
- Valores medidos e respectivos limites de erro;  
- Comparação entre medições experimentais e dados de referência do datasheet;  
- Registros fotográficos do setup de teste;  
- Logs ou capturas de tela relevantes.

---

## 4. Dificuldades e Soluções
Relate os principais desafios técnicos enfrentados e as soluções implementadas.  
Explique como eventuais limitações foram contornadas ou mitigadas, de modo a registrar aprendizados úteis para reproduções futuras.

**Exemplos:**
- Ajuste de timing no barramento I²C;  
- Necessidade de adaptação da biblioteca para MicroPython;  
- Filtragem de ruído em leitura analógica.

---

## 5. Conclusões e Trabalhos Futuros
Resuma as conclusões técnicas alcançadas e a avaliação crítica dos resultados.  
Indique aprimoramentos possíveis e oportunidades de extensão do trabalho, incluindo aplicações derivadas ou integração com outros módulos.

**Exemplos:**
- Otimizar a estabilidade do sinal por meio de filtragem digital;  
- Adaptar o código para o ambiente C/C++ (Pico SDK);  
- Integrar múltiplos sensores e consolidar dados via comunicação serial.

---

## 6. Referências
Liste as fontes técnicas e documentações consultadas, como datasheets, manuais de aplicação, artigos ou links de bibliotecas utilizadas.  
O formato de citação é livre, desde que contenha autor, título e origem.







