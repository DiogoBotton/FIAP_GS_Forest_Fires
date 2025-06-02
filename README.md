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


Modelo de classificação de queimada (CNN)
Problema: classificar imagens em 'fire' vs. 'no fire'

fire (queimada)
no fire (nçao queimada)

## Resultados da CNN Treinada do Zero

### Visão Geral

Este modelo foi treinado do zero para classificar imagens em duas categorias: "fire" (fogo) e "no fire" (sem fogo). O objetivo era criar um modelo base para comparar com abordagens de Transfer Learning e Fine-Tuning.

### Desempenho Durante o Treinamento

O modelo mostrou um rápido aumento na acurácia durante as primeiras épocas, com sinais de overfitting à medida que o treinamento avançava.

*   **Acurácia:** A acurácia no conjunto de treinamento atingiu quase 100% ao final das 10 épocas, enquanto a acurácia no conjunto de validação se estabilizou em torno de 95-97%.
*   **Perda (Loss):** A perda no conjunto de treinamento diminuiu para perto de zero, enquanto a perda no conjunto de validação permaneceu acima de 0.10, indicando overfitting.

### Gráficos de Acurácia e Perda

![Acurácia por época](assets/cnn_zero_acuracia_por_epoca)


*Este gráfico mostra a acurácia ao longo das épocas para os conjuntos de treinamento e validação.*

![Perda por época](assets/cnn_zero_perda_por_epoca)

*Este gráfico exibe a perda (loss) ao longo das épocas para os conjuntos de treinamento e validação.*

### Matriz de Confusão

![Matriz de Confusão](assets/cnn_zero_matriz_confusao)

A matriz de confusão revela o seguinte:

*   **Classe "no fire":** 21 amostras corretamente classificadas, 1 amostra classificada incorretamente como "fire" (falso positivo).
*   **Classe "fire":** 43 amostras corretamente classificadas, 3 amostras classificadas incorretamente como "no fire" (falso negativo).

### Métricas de Classificação
          precision    recall  f1-score   support

       0       0.88      0.95      0.91        22
       1       0.98      0.93      0.96        46

accuracy                           0.94        68


*   **Acurácia:** 94%
*   **Precisão:** 88% para "no fire" e 98% para "fire"
*   **Recall:** 95% para "no fire" e 93% para "fire"
*   **F1-score:** 91% para "no fire" e 96% para "fire"

### Curva ROC e AUC

![Curva ROC](assets/cnn_zero_roc_curve)

A curva ROC e o valor AUC indicam um excelente desempenho do modelo na discriminação entre as classes "fire" e "no fire". O valor de AUC de 0.95 para ambas as classes reforça a capacidade do modelo de classificar corretamente as imagens.

### Conclusão

O modelo CNN treinado do zero alcançou um alto desempenho, mas demonstrou sinais de overfitting. Para melhorar a generalização, recomenda-se:

*   Aplicar data augmentation.
*   Adicionar camadas de Dropout ou BatchNormalization.
*   Ajustar o Early Stopping.

## Resultados da Transferência de Aprendizado

### Visão Geral

Este modelo utilizou Transferência de Aprendizado com a arquitetura InceptionV3, pré-treinada no ImageNet, para classificar imagens em "fire" e "no fire".

### Desempenho Durante o Treinamento

O modelo demonstrou um desempenho muito bom desde o início, com alta acurácia tanto no conjunto de treinamento quanto no de validação.

*   **Acurácia:** A acurácia no conjunto de treinamento subiu rapidamente, atingindo quase 100% ao final das épocas. A acurácia no conjunto de validação também foi alta, oscilando em torno de 97-98%.
*   **Perda (Loss):** A perda no conjunto de treinamento diminuiu significativamente, enquanto a perda no conjunto de validação se manteve em níveis baixos, indicando uma boa capacidade de generalização.

### Gráficos de Acurácia e Perda

![Acurácia por época](assets/cnn_transferencia_acuracia_por_epoca)

*Este gráfico mostra a acurácia ao longo das épocas para os conjuntos de treinamento e validação.*

![Perda por época](assets/cnn_transferencia_perda_por_epoca)

*Este gráfico exibe a perda (loss) ao longo das épocas para os conjuntos de treinamento e validação.*

### Matriz de Confusão

![Matriz de Confusão](assets/cnn_transferencia_matriz_confusao)

A matriz de confusão revela o seguinte:

*   **Classe "no fire":** 22 amostras corretamente classificadas, 0 amostras classificadas incorretamente.
*   **Classe "fire":** 46 amostras corretamente classificadas, 0 amostras classificadas incorretamente.

### Métricas de Classificação
          precision    recall  f1-score   support

       0       1.00      1.00      1.00        22
       1       1.00      1.00      1.00        46

accuracy                           1.00        68


*   **Acurácia:** 100%
*   **Precisão:** 100% para ambas as classes
*   **Recall:** 100% para ambas as classes
*   **F1-score:** 100% para ambas as classes

### Curva ROC e AUC

![Curva ROC](assets/cnn_transferencia_roc_curve)

A curva ROC e o valor AUC indicam um desempenho perfeito do modelo. O valor de AUC de 1.00 para ambas as classes demonstra a capacidade do modelo de classificar corretamente as imagens.

### Conclusão

O modelo de Transferência de Aprendizado com InceptionV3 alcançou um desempenho excepcional, com acurácia e outras métricas perfeitas nos dados de teste. Isso sugere que a utilização de uma arquitetura pré-treinada foi altamente eficaz para este problema de classificação.

# Interpretação do Fine-Tuning

Este documento traz a análise dos resultados obtidos após o fine-tuning do modelo de classificação de imagens de queimadas.

---

## 1. Visão Geral do Treinamento

- **Épocas previstas:** 50  
- **Épocas executadas:** 11 (interrompido por EarlyStopping com `patience=10`)  
- **Tempo total de treinamento:** 1 min 44 s

---

## 2. Métricas por Época

### 2.1 Acurácia por Época  
![Acurácia por época](docs/images/accuracy_per_epoch.png)  
- Treino: oscila entre 99.1 % e 99.7 %.  
- Validação: mantém-se em ~97.82 %, sem melhoria.

### 2.2 Perda por Época  
![Perda por época](docs/images/loss_per_epoch.png)  
- Treino: varia entre 0.3 e 1.3.  
- Validação: estabiliza em ~5.8, indicando possível desajuste entre loss e accuracy.

---

## 3. Avaliação no Conjunto de Teste

### 3.1 Matriz de Confusão  
![Matriz de Confusão](docs/images/confusion_matrix.png)  

### 3.2 Curva ROC  
![ROC Curve](docs/images/roc_curve.png)  

### 3.3 Relatório de Classificação

| Classe | Precision | Recall | F1-Score | Suporte |
|:------:|:---------:|:------:|:--------:|:-------:|
|   0    |   1.00    |  1.00  |   1.00   |   22    |
|   1    |   1.00    |  1.00  |   1.00   |   46    |
| **—**  |    —      |   —    |   —      |   —     |
| **Accuracy** |       —       |   —    | **1.00** |   68    |

> **Obs.:** Desempenho perfeito pode indicar conjunto pequeno ou overfitting.

---

## 4. Conclusões e Próximos Passos

1. **Overfitting**:  
   - Validar com _data augmentation_ ou usar k-fold cross-validation.  
2. **Validação Estagnada**:  
   - Reavaliar _class weights_ ou normalização das labels.  
3. **Callbacks**:  
   - Se quiser treinar as 50 épocas completas, remova ou aumente o `patience` do `EarlyStopping`.  
   - Ajustar `ReduceLROnPlateau` para resposta mais rápida (p.ex. `factor=0.1`, `patience=3`).  

# Análise Comparativa dos Modelos de Classificação de Imagens de Queimadas

## 1. Resumo dos Resultados

| Modelo                       | Acurácia | Precisão (Classe 0) | Recall (Classe 0) | F1-Score (Classe 0) | Precisão (Classe 1) | Recall (Classe 1) | F1-Score (Classe 1) |
| ---------------------------- | -------- | ------------------- | ----------------- | ------------------- | ------------------- | ----------------- | ------------------- |
| CNN Treinada do Zero         | 94%      | 88%                 | 95%               | 91%                 | 98%                 | 93%               | 96%                 |
| Transferência de Aprendizado | 100%     | 100%                | 100%              | 100%                | 100%                | 100%              | 100%                |
| Fine-Tuning                  | 100%     | 100%                | 100%              | 100%                | 100%                | 100%              | 100%                |

## 2. Análise Detalhada

### 2.1. CNN Treinada do Zero

*   **Vantagens:**
    *   Modelo base para comparação.
    *   Bom desempenho inicial com ajustes básicos.
*   **Desvantagens:**
    *   Sinais de overfitting (alta acurácia no treino, menor na validação).
    *   Requer mais dados e ajustes para generalizar bem.
*   **Considerações:**
    *   Apesar do bom desempenho, a diferença entre as métricas de treino e validação sugere que o modelo está memorizando os dados de treino em vez de aprender padrões generalizáveis.

### 2.2. Transferência de Aprendizado (InceptionV3)

*   **Vantagens:**
    *   Excelente desempenho com poucas épocas de treinamento.
    *   Alta capacidade de generalização devido ao uso de conhecimento pré-existente.
*   **Desvantagens:**
    *   Pode ser excessivo para um problema relativamente simples.
    *   Requer mais recursos computacionais.
*   **Considerações:**
    *   A Transferência de Aprendizado se mostrou extremamente eficaz, atingindo acurácia perfeita nos dados de teste. Isso demonstra o poder de utilizar modelos pré-treinados em tarefas similares.

### 2.3. Fine-Tuning

*   **Vantagens:**
    *   Aproveita um modelo pré-treinado, ajustando-o para o problema específico.
    *   Potencial para alta precisão com menos dados e tempo de treinamento.
*   **Desvantagens:**
    *   Requer ajuste cuidadoso dos hiperparâmetros para evitar overfitting.
    *   Pode ser interrompido prematuramente pelo EarlyStopping se a validação não melhorar.
*   **Considerações:**
    *   O Fine-Tuning alcançou resultados semelhantes à Transferência de Aprendizado, mas com a necessidade de monitorar e ajustar os callbacks para garantir um treinamento adequado.

## 3. Conclusão Geral

*   A **Transferência de Aprendizado** e o **Fine-Tuning** foram superiores à CNN treinada do zero, atingindo acurácia perfeita nos dados de teste.
*   A escolha entre Transferência de Aprendizado e Fine-Tuning depende dos recursos disponíveis e da necessidade de ajustes finos no modelo.
*   Para a CNN treinada do zero, recomenda-se aplicar técnicas de regularização e aumentar a quantidade de dados para melhorar a generalização.
*   É importante monitorar os callbacks durante o treinamento (especialmente o EarlyStopping) para garantir que o modelo seja treinado adequadamente.

## 4. Próximos Passos

*   **Data Augmentation:** Aplicar transformações nas imagens para aumentar a variabilidade dos dados de treinamento.
*   **Regularização:** Adicionar camadas de Dropout ou BatchNormalization para reduzir o overfitting.
*   **Validação Cruzada:** Utilizar validação cruzada para obter uma estimativa mais robusta do desempenho do modelo.
*   **Ajuste de Hiperparâmetros:** Realizar uma busca mais detalhada pelos melhores hiperparâmetros para cada modelo.



## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
