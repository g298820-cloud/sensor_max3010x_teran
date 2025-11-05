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
  <img width="703" height="153" alt="image" src="https://github.com/user-attachments/assets/c4a4cf46-dfdc-47f6-acc3-99f2d5547fd5" />








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
