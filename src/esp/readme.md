# Monitoramento de Risco de Queimada com ESP32 e ThingSpeak

## Descrição
Este projeto simula um sistema de monitoramento de **temperatura**, **umidade** e **gás (MQ-2)** usando um ESP32. Quando as condições indicam risco de queimadas, um LED de alerta acende. Periodicamente, os dados são enviados à nuvem via **ThingSpeak**, onde podem ser visualizados em gráficos.

![Diagrama do Projeto no Wokwi](esp32_diagrama.png)

## Materiais Necessários
- Simulação no [Wokwi ESP32 Simulator](https://wokwi.com/): **Nenhum hardware físico é necessário!**

## Software e Bibliotecas
1. **Navegador Web:** Apenas um navegador  para acessar o Wokwi.
2. **Bibliotecas** (já inclusas no ambiente Wokwi):
   - WiFi (já incluída no core ESP32)
   - ThingSpeak

## Configuração do Canal ThingSpeak
1. Acesse https://thingspeak.com e crie uma conta gratuita.
2. Crie um novo **Channel** e habilite três campos:
   - **Field 1** – Temperatura (°C)
   - **Field 2** – Umidade (%)
   - **Field 3** – Tensão MQ-2 (V)
3. Na aba **API Keys**, copie sua **Write API Key**.

## Ajustes no Código
1. **Acesse o projeto no Wokwi:**
   - Clique neste link para abrir o projeto pré-configurado: [https://wokwi.com/projects/432712668245983233]
   - (Substitua "432712668245983233" pelo ID real do seu projeto no Wokwi, se necessário)

2. **Edite as credenciais:**
   - No editor de código do Wokwi, ajuste as seguintes linhas:
```cpp
// 1) CREDENCIAIS WI-FI (rede local ou Wokwi-GUEST)
const char* ssid       = "Wokwi-GUEST";    // rede padrão do Wokwi
const char* password   = "";               // Wokwi-GUEST não tem senha

// 2) THINGSPEAK
const unsigned long channelID    = 2978911;           // substitua pelo seu Canal ID
const char*           writeAPIKey = "TOTTK66L75EN77RN"; // sua Write API Key
```

   - Certifique-se de inserir seu **Channel ID** e **Write API Key** do ThingSpeak.

---

## Como Funciona o Sketch

1. **setup()**
   - Inicia a porta Serial (115200 bps)
   - Configura pinos do LED e MQ-2 (simulados)
   - Conecta ao Wi-Fi (simulado no Wokwi)
   - Inicializa a biblioteca ThingSpeak

2. **loop()**
   - **Simulação** de temperatura (oscila entre 25 °C e 40 °C)
   - **Simulação** de umidade (oscila entre 80 % e 20 %)
   - **Simulação** de leitura MQ-2 (20 % de chance de valor alto)
   - Acende o LED se houver risco de queimadas
   - A cada 20 s envia `field1`, `field2` e `field3` ao ThingSpeak
   - Imprime no Serial Monitor o `responseCode` (200 = OK)

---

## Passo a Passo de Uso (Wokwi)

1. **Abra o projeto no Wokwi** usando o link fornecido.
2. **Ajuste as credenciais** no código.
3. Clique no botão **"Start Simulator"** no Wokwi.
4. Abra o **Serial Monitor** na parte inferior da tela do Wokwi (115200 bps).
5. Observe a saída no Serial Monitor:
   - Verifique a conexão Wi-Fi.
   - Observe as leituras simuladas.
   - Verifique se `ThingSpeak response: 200` aparece, indicando envio bem-sucedido.
6. Acesse seu canal em ThingSpeak para visualizar os gráficos em tempo real.

---

## Personalizações

- Ajuste as condições de alerta (limiar de tensão, temperatura/umidade).
- Reduza ou aumente o intervalo de envio alterando `tsInterval`.
- Explore os componentes do Wokwi para simular sensores reais (DHT22, MQ-2, etc.).

---

## Licença
Este projeto está sob a licença **MIT**. Sinta-se livre para usar, modificar e redistribuir.

---
