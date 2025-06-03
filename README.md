# FIAP - Faculdade de Informática e Administração Paulista
Projeto voltado a desenvolver soluções com Redes Neurais Convolucionais (CNN) e Redes Recorrentes abordando problemas de séries temporais.

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto
Monitoramento de Queimadas via Visão Computacional e Previsão de Focos de Incêndio a Partir de Análises de Séries Temporais

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/bryanjfagundes/">Bryan Fagundes</a>
- <a href="https://br.linkedin.com/in/brenner-fagundes">Brenner Fagundes</a>
- <a href="https://www.linkedin.com/in/diogo-botton-46ba49197/">Diogo Botton</a> 
- <a href="https://www.linkedin.com/in/hyankacoelho/">Hyanka Coelho</a> 
- <a href="https://www.linkedin.com/in/julianahungaro/">Juliana Hungaro Fidelis</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godoi</a>

## 📜 Descrição

A fazer...

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>src</b>: Todo o código fonte criado. (Complementar)

## 🔧 Como executar o código

A fazer...


# 🚒 Classificador de Queimadas (CNN)

Projeto de classificação de imagens em duas categorias:  
- **`fire`** (queimada)  
- **`no_fire`** (não queimada)

## 🔍 Descrição

Este projeto implementa e compara três abordagens de Deep Learning para detectar queimadas em imagens:

1. **CNN treinada do zero** – arquitetura customizada e treinada em ~10 épocas.  
2. **Transfer Learning** – utilizando InceptionV3 pré-treinado no ImageNet.  
3. **Fine-Tuning** – refinamento do modelo pré-treinado em nosso conjunto de dados.

O objetivo é avaliar acurácia, generalização e custo computacional de cada abordagem.

## 📊 Resultados

## Resultados da CNN Treinada do Zero

- Acurácia (test): 94%
- Precision/Recall/F1 (classe 0): 0.88 / 0.95 / 0.91
- Precision/Recall/F1 (classe 1): 0.98 / 0.93 / 0.96

Observação: sinais claros de overfitting (train_loss→0 vs val_loss≈0.10).

### Gráficos de Acurácia e Perda

![Acurácia por época](assets/cnn_zero_acuracia_por_epoca)

![Perda por época](assets/cnn_zero_perda_por_epoca)

## Resultados da Transferência de Aprendizado

- Acurácia (test): 100%
- Precision/Recall/F1 (ambas classes): 1.00

Observação: excelente generalização, mas maior custo computacional.

![Acurácia por época](assets/cnn_transferencia_acuracia_por_epoca)

![Perda por época](assets/cnn_transferencia_perda_por_epoca)


# Interpretação do Fine-Tuning

- Acurácia (test): 100%
- Precision/Recall/F1 (ambas classes): 1.00

Observação: treinamento interrompido em 11/50 épocas via EarlyStopping.
Este documento traz a análise dos resultados obtidos após o fine-tuning do modelo de classificação de imagens de queimadas.


![Acurácia por época](docs/images/accuracy_per_epoch.png)  


## 📝 Conclusões e Próximos Passos

Melhor abordagem: Transfer Learning e Fine-Tuning superaram CNN do zero em acurácia e generalização.

Overfitting (CNN do zero):

- Adicionar data augmentation
- Incluir Dropout e BatchNormalization
- Aumentar volume de dados ou usar validação cruzada


Hyperparam tuning: explorar learning_rate, batch_size e callbacks (EarlyStopping, ReduceLROnPlateau)

Escalabilidade: converter Fine-Tuning para TinyML no ESP32-CAM para inferência embarcada








## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
