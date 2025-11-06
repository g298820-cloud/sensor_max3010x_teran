https://github.com/BitDogLab/BitDogLab/blob/main/softwares/I2C/teste%20e%20Scam%20de%20I2C%20V2A%20mostrando%20no%20OLED%20%20funcionando.py


# <AHT10 — Sensor de umedade y Temperatura en BitDogLab> — Sensores na BitDogLab

**Dupla:** Gustavo Santos Terán Rupay (298820 / @gustavosantosteran)  
**Turma:** EA801 — 2025S2  
**Repositório:** [sensor_AHT10_teran](https://github.com/g298820-cloud/sensor_AHT10_teran)

## 1. Descrição do sensor
- Fabricante / modelo: Aosong (ASAIR) AHT10 
- Princípio de funcionamento: O AHT10 é um sensor digital de umidade e temperatura que utiliza um polímero capacitivo para medir a umidade relativa e um termistor interno para a temperatura. A conversão analógico-digital é realizada internamente, e os dados são transmitidos via I²C.
- Tensão/consumo típicos: 1.8 V – 3.6 V, consumo típico de 0.5 mA em operação normal. O consumo em modo de baixa potência é de aproximadamente 0.2 µA.
- Faixa de medição / resolução:
  Umidade relativa: 0 – 100 % RH (±2 % RH típico)
  Temperatura: –40 °C – 85 °C (±0.3 °C típico)
  Resolução: 0.024 % RH / 0.01 °C
  
- Datasheet (URL): https://server4.eca.ir/eshop/AHT10/Aosong_AHT10_en_draft_0c.pdf](https://server4.eca.ir/eshop/AHT10/Aosong_AHT10_en_draft_0c.pdf

## 2. Conexões de hardware
- Tabela indicando as conexões entre BitDogLab e sensor:

  <img width="1130" height="558" alt="image" src="https://github.com/user-attachments/assets/f3db34bd-29a3-407c-8a48-95ad635cbc58" />

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
