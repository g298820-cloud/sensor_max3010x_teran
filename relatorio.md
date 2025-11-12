# Relatório Técnico da Dupla

Disciplina: EA801 — Sistemas Embarcados

Dupla: Gustavo Santos Terán Rupay (RA: 298820 / @g298820@g.unicamp.br)

Período: 2025S2

Placa: BitDogLab (Raspberry Pi Pico / RP2040)

Sensor: AHT10 — Sensor de Umidade e Temperatura

## 1. Escopo
Descreva de forma clara o propósito do experimento ou desenvolvimento realizado, delimitando o escopo do trabalho e os objetivos técnicos a serem atingidos.  
Inclua também os critérios de sucesso utilizados para validar o funcionamento do sistema.

O presente experimento tem como escopo o desenvolvimento, integração e validação de um sistema embarcado baseado na placa BitDogLab (RP2040), utilizando o sensor digital AHT10 para medições de umidade relativa do ar e temperatura ambiente, com exibição dos dados em tempo 
real no display OLED SSD1306, através da comunicação I2C.

**Os objetivos específicos**

-Implementar a comunicação correta entre o AHT10 e o microcontrolador RP2040 via protocolo I2C.

-Exibir continuamente os valores de temperatura e umidade no terminal e no display OLED.

-Validar o funcionamento do sistema por meio de scripts de teste (test_basico.py e test_ruido.py).

-Avaliar a estabilidade das leituras, observando variações naturais e possíveis ruídos.

**O trabalho procura consolidar o entendimento dos seguintes conceitos técnicos:**

-Configuração e utilização de múltiplos barramentos I2C em sistemas embarcados.

-Leitura de sensores digitais e interpretação de dados binários.

-Controle e atualização de um display gráfico (SSD1306) utilizando bibliotecas externas em MicroPython.

-Estruturação modular do código, com arquivos principais e scripts de teste.

**Os critérios de sucesso considerados para validação**

-Detecção do sensor AHT10 no endereço 0x38 e do display OLED no endereço 0x3C durante o escaneamento I2C.

-Exibição correta e contínua das medições no terminal e no OLED, com atualização a cada 2 segundos.

-Estabilidade das leituras com variação máxima de ±0.3 °C para temperatura e ±2 %RH para umidade.

## 2. Metodologia e Implementação
Apresente os procedimentos adotados, incluindo a arquitetura do sistema, estratégias de programação, bibliotecas utilizadas e justificativas de projeto.  
Se aplicável, descreva o esquema de ligação elétrica, o protocolo de comunicação, as rotinas de aquisição e processamento de dados e o fluxo lógico do programa.  


**2.1 Diagrama de blocos e descrição funcional dos módulos**

<img width="346" height="459" alt="image" src="https://github.com/user-attachments/assets/38c67d2f-8ae0-4069-9f40-2f90ea54808c" />


O funcionamento geral do sistema é representado no diagrama de blocos, que descreve o fluxo de dados desde as medições físicas realizadas pelo sensor AHT10 até a exibição final dos resultados no display OLED e no terminal serial.

O sistema é dividido em módulos funcionais integrados via barramentos digitais

-Ambiente: representa o meio físico onde são medidas as variáveis de temperatura (T) e umidade relativa (UR).

-Sensor AHT10: converte as grandezas físicas do ambiente em sinais digitais utilizando conversão analógico-digital interna. A comunicação é feita via protocolo I2C, no endereço 0x38.

-Comunicação I2C0: o sensor AHT10 é conectado à BitDogLab por meio do barramento I2C0 (SDA = GP0, SCL = GP1), transmitindo os dados digitais para o microcontrolador RP2040.

-Processamento (RP2040): o microcontrolador processa os dados recebidos, aplica as fórmulas de conversão para °C e %UR e atualiza as saídas (display OLED e terminal serial).

-Controle: uma rotina de temporização (time.sleep(2)) define o intervalo entre leituras, garantindo atualização contínua e estável a cada 2 segundos.

-Comunicação I2C1: o display OLED SSD1306 está conectado ao barramento I2C1 para exibir as medições processadas.

-Display OLED: apresenta em tempo real os valores de temperatura e umidade processados, utilizando a biblioteca externa ssd1306.py.

-Terminal Serial (Thonny IDE): exibe os mesmos dados em formato de texto via porta USB, permitindo depuração e monitoramento das leituras.

-Saída final: os resultados são exibidos simultaneamente no display e no terminal, com atualização contínua a cada 2 segundos.

**2.2 Bibliotecas Utilizadas**

   * machine para controle dos periféricos (I2C, Pin)

   * time para temporização entre leituras

   * ssd1306 é biblioteca externa para o controle do display OLED via I2C

   * Funções internas do arquivo aht10_prueba_2.py implementam a comunicação e cálculo de             temperatura e umidade.

Essas bibliotecas garantem portabilidade e fácil manutenção do código em outros projetos baseados em MicroPython.

**2.3 Estratégias de Depuração e Calibração**

Durante o desenvolvimento, foram utilizadas leituras simultâneas no terminal serial e no display OLED para verificar a consistência dos dados.
A variação típica observada foi de ±0.3 °C em temperatura e ±2 %UR em umidade, valores compatíveis com as especificações do sensor.
A calibração não foi necessária, visto que o AHT10 possui compensação interna de temperatura e umidade.

**2.4 Protocolo de comunicação e fluxo lógico**

<img width="278" height="444" alt="image" src="https://github.com/user-attachments/assets/d15cc9cd-6a89-4329-8b70-593f13313e9c" />

**Sequência lógica**

2.4.1 Iniciação das interfaces I2C e do display OLED → corresponde à configuração inicial do MicroPython, onde são definidos os objetos I2C(0) e I2C(1) e a inicialização do SSD1306.

2.4.2 Detecção e comunicação com o AHT10 → confirma que o sensor está respondendo no endereço 0x38.

2.4.3 Leitura dos valores digitais → o AHT10 envia os dados crus de temperatura e umidade (20 bits cada).

2.4.4 Conversão dos dados para valores físicos → o RP2040 aplica as fórmulas conforme o datasheet do AHT10 para °C e %UR.

2.4.5 Exibição dos resultados → o programa mostra as leituras no OLED (via biblioteca ssd1306.py) e no terminal do Thonny.

2.4.6 Espera de 2s e repetição do ciclo → implementada com time.sleep(2) no loop principal.

**2.5 Esquema de ligação elétrica**

O esquema de ligação elétrica representa as conexões entre o sensor AHT10, a placa BitDogLab (baseada no microcontrolador RP2040) e o display OLED SSD1306. A comunicação entre os dispositivos é realizada por meio do protocolo I²C.

**Tabela de Conexões**
<img width="637" height="358" alt="image" src="https://github.com/user-attachments/assets/dd093a6f-b9b7-4e9a-a57a-c5db43254197" />

**Descrição do Circuito**

-O sensor AHT10 comunica-se com o microcontrolador via barramento I2C0, enquanto o display OLED utiliza o barramento I2C1. Ambos os módulos compartilham a mesma alimentação de 3.3 V proveniente da BitDogLab. As linhas SDA e SCL são utilizadas para transmissão de dados e sincronização, respectivamente.

-O AHT10 converte a umidade e temperatura em sinais digitais, que são lidos pelo RP2040. Em seguida, o microcontrolador envia as informações processadas ao display SSD1306 para exibição. A taxa de atualização é controlada por temporização no código (time.sleep(2)).


## 3. Resultados e Análise
Apresente os principais resultados obtidos, acompanhados de gráficos, tabelas ou imagens que sustentem a análise.  
Discuta o comportamento observado, eventuais desvios em relação ao esperado e hipóteses para as causas identificadas.  

<img width="268" height="492" alt="image" src="https://github.com/user-attachments/assets/55db78b0-5546-49ca-ac6a-721d9b013855" />

<img width="292" height="482" alt="image" src="https://github.com/user-attachments/assets/793dab73-6816-4068-9442-2dc7be6d0710" />

Durante os testes realizados com o sensor AHT10 conectado à BitDogLab, o sistema demonstrou comunicação I²C estável com o microcontrolador RP2040, exibindo os valores de temperatura e umidade em tempo real no display OLED SSD1306.

**Durante o funcionamento, observou-se:**

<img width="315" height="363" alt="image" src="https://github.com/user-attachments/assets/6e399faa-71fd-46ea-a8c5-70f924b82c4e" />


-Tempo de estabilização inicial de cerca de 1 s após energização do sensor.
-Pequenas flutuações (< ±2 %) atribuídas à variação natural do ar e à precisão do sensor.
-Atualização contínua no OLED a cada 2 s, conforme definido no código principal (aht10_prueba_2.py).


                              Valor Médio    Variação Observada         Faixa do Datasheet              

Temperatura                   26,7 °C           ±0,3 °C             –40 °C a 85 °C (±0,3 °C típico) 


Umidade Relativa              57,1 % RH         ±2 % RH              0 – 100 % RH (±2 % RH típico)   


**Esses valores estão em conformidade com o comportamento esperado para o AHT10, considerando as condições de temperatura ambiente (21-25 °C) e umidade relativa do ar em Campinas (55 – 60 %) no momento da medição.**

-------------------------------------------------------------------------------------------------------------------------------------

<img width="427" height="546" alt="image" src="https://github.com/user-attachments/assets/f3ac3f65-801b-490c-968c-e7a874207ea9" />


	                              Média	          Desvio             Padrão	 Variação Total

Temperatura (°C)	              24,52	          ±0,013	          24,50 – 24,55


Umidade Relativa (%)	          51,13	          ±0,161	          50,91 – 51,43

**Estabilidade da Temperatura:**

1) As leituras mantiveram-se praticamente constantes, com uma variação total inferior a 0,05 °C.

2) O desvio padrão muito baixo indica excelente estabilidade térmica do sensor e baixo ruído de medição.

3) O valor médio de 24,52 °C está de acordo com a temperatura ambiente esperada, validando o desempenho do AHT10.

**Estabilidade da Umidade Relativa:**

1) As variações ficaram entre 50,91 % e 51,43 %, ou seja, dentro de ±0,16 % RH, muito abaixo do limite de precisão típico do sensor (±2 % RH).

2) Pequenas flutuações são normais e refletem microvariações na umidade do ar e no processo de amostragem interna do sensor.

**Ruído e Repetibilidade:**

1) O ruído medido é quase imperceptível, e as curvas de temperatura e umidade apresentaram comportamento suave e contínuo.

2) Isso demonstra que o sensor mantém alta repetibilidade e baixa deriva nas leituras consecutivas.


<img width="687" height="343" alt="image" src="https://github.com/user-attachments/assets/eebac589-6305-492a-a8fc-57f723b39ef7" />



## 4. Dificuldades e Soluções
Relate os principais desafios técnicos enfrentados e as soluções implementadas.  
Explique como eventuais limitações foram contornadas ou mitigadas, de modo a registrar aprendizados úteis para reproduções futuras.

Durante o desenvolvimento do projeto com o sensor AHT10 e o display OLED SSD1306, algumas dificuldades técnicas foram identificadas e solucionadas ao longo do processo de integração com a placa BitDogLab.

1. Comunicação I2C instável:
Inicialmente, o sensor AHT10 não era reconhecido de forma consistente no barramento I²C. O problema estava relacionado à configuração incorreta dos pinos SDA e SCL. Após revisar o datasheet da BitDogLab, foi confirmado que o sensor estava ligado ao barramento I2C1, enquanto o display OLED operava no I2C0.

Solução:
**Ajuste dos pinos no código e verificação dos endereços detectados com o script i2c_scan.py, garantindo a detecção correta dos dispositivos (0x38 e 0x3C).**

3. Adaptação da biblioteca SSD1306:
A biblioteca original ssd1306.py não estava presente no firmware padrão do MicroPython utilizado.

Solução: 
**O arquivo foi importado manualmente do repositório oficial do MicroPython e copiado para o diretório /src/ da placa, permitindo o controle total do display OLED e a exibição das leituras em tempo real.**

4. Sincronização das leituras e exibição:
Durante os primeiros testes, as medições do AHT10 e as atualizações no display ocorriam em intervalos irregulares, gerando dados intermitentes.

Solução: 
**Foi implementado um delay fixo de 2 segundos (time.sleep(2)) entre as leituras, estabilizando o ritmo de aquisição e visualização dos dados.**

5. Ruído e variação nas medições:
Foram observadas pequenas flutuações nos valores de temperatura (±0.3 °C) e umidade (±2 % RH), especialmente durante o aquecimento do sensor e em ambientes com corrente de ar.

Solução: 
**Adição de uma média simples sobre as últimas amostras coletadas, reduzindo o ruído e melhorando a estabilidade das leituras.**


## 5. Conclusões e Trabalhos Futuros
Resuma as conclusões técnicas alcançadas e a avaliação crítica dos resultados.  
Indique aprimoramentos possíveis e oportunidades de extensão do trabalho, incluindo aplicações derivadas ou integração com outros módulos.

**Conclusões:**

-A comunicação I²C foi corretamente configurada e validada por meio dos scripts de teste (i2c_scan.py e i2c_scan_oled.py).

-O sensor AHT10 apresentou boa estabilidade térmica após o tempo de aquecimento (~1 segundo).

-A implementação do delay e da média móvel reduziu ruídos de leitura e melhorou a consistência das medições.

-O uso do MicroPython simplificou a prototipagem e permitiu depuração rápida diretamente via Thonny.

**Trabalhos futuros e melhorias propostas:**

-Adaptar o código para C/C++ (Pico SDK), permitindo maior desempenho e controle sobre o hardware.

-Adicionar armazenamento local ou envio dos dados via Wi-Fi, possibilitando registro contínuo e monitoramento remoto.

-Integrar o AHT10 com outros sensores (luminosidade, pressão ou CO₂) e consolidar os dados em um sistema único de medição ambiental.

## 6. Referências
Liste as fontes técnicas e documentações consultadas, como datasheets, manuais de aplicação, artigos ou links de bibliotecas utilizadas.  
O formato de citação é livre, desde que contenha autor, título e origem.

[1] Aosong (ASAIR), “AHT10 – Humidity and Temperature Sensor Datasheet”, 2020.
Disponível em: https://server4.eca.ir/eshop/AHT10/Aosong_AHT10_en_draft_0c.pdf

[2] S. Lehmann, “SSD1306.py – MicroPython OLED Driver Library”, GitHub Repository, 2018.
Disponível em: https://raw.githubusercontent.com/stlehmann/micropython-ssd1306/master/ssd1306.py

[3] BitDogLab, “Teste e varredura de dispositivos I²C com exibição no OLED (V2A)”, GitHub Repository, 2024.
Disponível em: https://github.com/BitDogLab/BitDogLab/blob/main/softwares/I2C/teste%20e%20Scam%20de%20I2C%20V2A%20mostrando%20no%20OLED%20%20funcionando.py

[4] Raspberry Pi Foundation, “RP2040 Microcontroller Documentation”, 2023.
Disponível em: https://www.raspberrypi.com/documentation/microcontrollers/

































