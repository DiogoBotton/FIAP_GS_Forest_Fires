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

![Acurácia por época](image_url: 3)

*Este gráfico mostra a acurácia ao longo das épocas para os conjuntos de treinamento e validação.*

![Perda por época](image_url: 2)

*Este gráfico exibe a perda (loss) ao longo das épocas para os conjuntos de treinamento e validação.*

### Matriz de Confusão

![Matriz de Confusão](image_url: 1)

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

![Curva ROC](image_url: 0)

A curva ROC e o valor AUC indicam um excelente desempenho do modelo na discriminação entre as classes "fire" e "no fire". O valor de AUC de 0.95 para ambas as classes reforça a capacidade do modelo de classificar corretamente as imagens.

### Conclusão

O modelo CNN treinado do zero alcançou um alto desempenho, mas demonstrou sinais de overfitting. Para melhorar a generalização, recomenda-se:

*   Aplicar data augmentation.
*   Adicionar camadas de Dropout ou BatchNormalization.
*   Ajustar o Early Stopping.




## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
