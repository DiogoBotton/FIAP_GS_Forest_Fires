FROM python:3.11-slim

WORKDIR /api

COPY . .

# Instala gdown para baixar o modelo do google drive
RUN pip install gdown

# Baixa o modelo treinado
RUN gdown --id 17c7iQHbJ1j6e_FScGvXnbbqxSvOmBWwr -O /api/cnn_model.h5

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]