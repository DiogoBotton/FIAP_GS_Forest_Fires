# 🚒 Classificador de Queimadas (CNN)

Projeto de classificação de imagens em duas categorias:  
- **`fire`** (queimada)  
- **`no_fire`** (não queimada)

![Amostras das imagens](../../assets/amostras.png "Amostra das Imagens)")


## 🔍 Descrição

Este projeto implementa e compara três abordagens de Deep Learning para detectar queimadas em imagens:

1. **CNN treinada do zero** – arquitetura customizada e treinada em ~10 épocas.  
2. **Transfer Learning** – utilizando InceptionV3 pré-treinado no ImageNet.  
3. **Fine-Tuning** – refinamento do modelo pré-treinado em nosso conjunto de dados.

O objetivo é avaliar acurácia, generalização e custo computacional de cada abordagem.

## 📊 Resultados

## Resultados da CNN Treinada do Zero


### Epochs e Iterações

O treinamento foi executado por 8 épocas, com 46 passos (batches) por época.


- Métricas de Treinamento e Validação  
- Acurácia (accuracy): Para cada época, a acurácia do treino é apresentada, começando em aproximadamente 80.56% na primeira época e chegando a quase 98.69% na última.
- Perda (loss): A função de perda diminui ao longo das épocas, de cerca de 0.5887 na primeira época para 0.0481 na última, indicando que o modelo está melhorando seu desempenho no conjunto de treinamento.
- Acurácia de Validação (val_accuracy) e Perda de Validação (val_loss):
  - Essas métricas mostram o desempenho do modelo em um conjunto de validação separado. Por exemplo, na primeira época, a acurácia de validação foi de 89.92% (com loss 0.3042) e, na última, atingiu 95.91% (com loss 0.1439).


### Matriz de Confusão
Mostra que o modelo teve algumas dificuldades em classificar corretamente as imagens, com alguns erros de classificação.

![Matriz de Confusão](../../assets/raw_matriz_confusao.png "Matriz de Confusão)")

### Curva ROC 
A curva ROC está bem próxima do canto superior esquerdo, o que indica um bom desempenho do modelo. A área sob a curva (AUC) é de 0.98, o que significa que o modelo tem uma alta capacidade de distinguir entre as classes.

![Curva ROC](../../assets/raw_roc.png "Curva ROC)")

### Curva Precisão-Recall
A curva Precisão-Recall do modelo Raw mostra um desempenho muito bom, com alta precisão para a maioria dos valores de recall. No entanto, há uma queda na precisão quando o recall se aproxima de 1.0, o que indica que o modelo tem mais dificuldade em identificar todos os casos positivos sem gerar falsos positivos.

![Curva Precisão-Recall](../../assets/raw_precision.png "Curva Precisão-Recall)")

### Performance Final
O modelo atinge sua melhor acurácia de validação de aproximadamente 95.91%, o que é indicado ao final do log como “Raw model melhor val_accuracy: 0.959128081798553.

Em resumo, o modelo está aprendendo bem a distinguir entre as classes (incêndio e não-incêndio), com uma melhoria consistente tanto no conjunto de treinamento quanto no de validação ao longo das 10 épocas.



## Resultados da Transferência de Aprendizado

O treinamento do modelo de Transfer Learning (TL) foi feito ao longo de 8 épocas, com os seguintes resultados:

### Epochs e Iterações
O treinamento foi executado por 8 épocas, com 46 passos (batches) por época.

### Métricas de Treinamento e Validação

- Acurácia (accuracy): A acurácia no conjunto de treinamento começa em 84.72% na primeira época e atinge valores acima de 99% nas últimas épocas, indicando uma boa capacidade de aprendizado do modelo.
- Perda (loss): A perda no treinamento diminui significativamente, começando em 1.0075 na primeira época e chegando a valores muito baixos nas épocas seguintes, mostrando que o modelo está convergindo.
- Acurácia de Validação (val\_accuracy) e Perda de Validação (val\_loss)
  - A acurácia de validação atinge um pico de 98.37% (com perda de 0.1833) na sétima época, indicando um desempenho muito bom na generalização para dados não vistos.

### Matriz de Confusão
Matriz perfeita, sem erros, mostra que ele aprendeu a distinguir as classes muito bem.

![Amostras das imagens](../../assets/tl_matriz.png "Matriz de Confusão)")

### Curva ROC 
A curva ROC para o modelo TL mostra um desempenho perfeito, com AUC = 1.0. A curva atinge o canto superior esquerdo do gráfico, indicando que o modelo é capaz de classificar todas as imagens corretamente, sem gerar falsos positivos ou falsos negativos.

![Curva ROC](../../assets/tl_roc.png "Curva ROC)")

### Curvas Precisão-Recall (TL Model)
A curva atinge o valor máximo de Precisão (1.0) e Recall (1.0) em praticamente todo o intervalo. Isso indica um classificador perfeito, onde não há trade-off entre Precisão e Recall. O modelo consegue identificar todos os casos positivos (Recall = 1.0) sem gerar falsos positivos (Precisão = 1.0).

![Curva Precisão-Recall](../../assets/tl_precision.png "Curva Precisão-Recall)")



## 📝 Conclusões 

O modelo de Transfer Learning (TL) superou significativamente o modelo "Raw" em termos de desempenho. O modelo TL alcançou 100% de precisão, indicando uma classificação perfeita no conjunto de teste. O modelo Raw, embora ainda bom, apresentou alguns erros de classificação.

Você gostaria de aprofundar a análise em algum aspecto específico, como explorar as razões para os erros do modelo Raw ou investigar a possibilidade de otimizar ainda mais o modelo TL?

Performance Final
O modelo de Transfer Learning alcançou uma acurácia de validação de 98.37%, conforme indicado em "TL model melhor val\_accuracy: 0.9836512207984924".

Em resumo, o modelo de Transfer Learning teve um desempenho excelente, superando o modelo "raw" em termos de acurácia de validação. O modelo aprendeu a classificar as imagens de forma muito precisa, com uma perda de validação relativamente baixa.

Por fim, uma interface gráfica foi desenvolvida para apresentar os resultados das previsões e detecções em tempo real, utilizando ferramentas como Streamlit ou Dash. O sistema permite a visualização de áreas com risco de incêndio, monitoramento das condições ambientais em tempo real e geração de alertas automáticos em caso de detecção de focos de incêndio.

