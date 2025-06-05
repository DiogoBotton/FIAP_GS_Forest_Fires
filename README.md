# FIAP - Faculdade de Informática e Administração Paulista

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

Projeto voltado a desenvolver soluções com Redes Neurais Convolucionais (CNN), ESP32 e abordar problemas de séries temporais no contexto de incêndios florestais.

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>src</b>: Todo o código fonte criado.
- <b>src/Wildfire_Classificator</b>: Desenvolvimento de uma rede neural convolucional para classificação de fogo e não fogo em contextos florestais.
- <b>src/Wildfire_TimeSeries</b>: Análises exploratórias e desenvolvimento de um modelo capaz de prever a sazonalidade das queimadas e um percentual de risco de fogo.
- <b>src/api</b>: API para disponibilizar os dois modelos.
- <b>src/esp</b>: Desenvolvimento de um protótipo no ESP32 para dar alertas de risco de fogo baseado em características de temperatura e humidade.

## 🔧 Como executar o código

Para subir uma aplicação com os dois modelos disponibilizados via API em um container do Docker, vá para o diretório *scripts* e digite:

```bash
    docker-compose up -d --build
```

OBS: É necessário ter Docker instalado na máquina para funcionar este comando.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>