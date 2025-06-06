from fastapi import APIRouter, HTTPException, UploadFile, File
import os
import tensorflow as tf
from schemas import PredictRiskRequest
from enums import Bioma, Mes
from utils import prepare_image_for_predict
import pandas as pd

ALLOWED_EXTENSIONS = ['.png', '.jpg', '.jpeg']

main_path = os.path.dirname(__file__)
cnn_model_path = os.path.join(main_path, '..', 'cnn_model.h5')
regression_model_path = os.path.join(main_path, '..', 'regression_best_model.keras')
ref_stats_path = os.path.join(main_path, '..', 'referencia_estatistica_bioma_mes.csv')

router = APIRouter(tags=["Predicts"])

@router.post("/fire-detect", summary='Realiza a detecção de fogo em florestas em uma imagem.')
async def Fire_Detect(file: UploadFile = File(...)):
    """
    ### Detecção de fogo

    Realiza a detecção de fogo em contextos florestais.

    **Arquivos válidos:**
    - png
    - jpg
    - jpeg
    """
    filename = file.filename

    file_extension = os.path.splitext(filename)[1].lower()
    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f'Extensão de arquivo inválida: {file_extension}. Permitidos: {ALLOWED_EXTENSIONS}')
    
    try:
        cnn_model = tf.keras.models.load_model(cnn_model_path)
    except:
        raise HTTPException(status_code=404, detail='Modelo CNN não encontrado.')
    
    img = await file.read()  # lê o conteúdo do arquivo
    img = prepare_image_for_predict(img)
    
    pred = cnn_model.predict(img)
    print(pred)
    
    fire_prob = pred[0][0]
    nofire_prob = pred[0][1]
    
    return {
        "fire": round(float(fire_prob) * 100, 2),
        "nofire": round(float(nofire_prob) * 100, 2)
    }
    
@router.post("/predict-risk", summary='Realiza a previsão do risco de fogo.')
async def Predict_Risk(data: PredictRiskRequest):
    """
    ### Predição de riscos

    Realiza a previsão de risco de fogo para uma determinada região.
    
    **Enums validos para mês:**
    - Janeiro = 1
    - Fevereiro = 2
    - Março = 3
    - Abril = 4
    - Maio = 5
    - Junho = 6
    - Julho = 7
    - Agosto = 8
    - Setembro = 9
    - Outrubro = 10
    - Novembro = 11
    - Dezembro = 12
    
    **Enums válidos para bioma**
    - Amazônia = 1
    - Cerrado = 2
    - Caatinga = 3
    - Pantanal = 4
    - Pampa = 5
    - Mata Atlântica = 6
    """
    try:
        regression_model = tf.keras.models.load_model(regression_model_path)
    except:
        raise HTTPException(status_code=404, detail='Modelo de regressão não encontrado.')
    
    # A ordem dos dados devem ser iguais a ordem que foi treinado (desta forma já esta ordenado)
    # Formato (1, n_features)
    data_dict = {
        'mes_April': [True if data.mes == Mes.April else False],
        'mes_August': [True if data.mes == Mes.August else False],
        'mes_December': [True if data.mes == Mes.December else False],
        'mes_February': [True if data.mes == Mes.February else False],
        'mes_January': [True if data.mes == Mes.January else False],
        'mes_July': [True if data.mes == Mes.July else False],
        'mes_June': [True if data.mes == Mes.June else False],
        'mes_March': [True if data.mes == Mes.March else False],
        'mes_May': [True if data.mes == Mes.May else False],
        'mes_November': [True if data.mes == Mes.November else False],
        'mes_October': [True if data.mes == Mes.October else False],
        'mes_September': [True if data.mes == Mes.September else False],
        'bioma_Amazônia': [True if data.bioma == Bioma.Amazonia else False],
        'bioma_Caatinga': [True if data.bioma == Bioma.Caatinga else False],
        'bioma_Cerrado': [True if data.bioma == Bioma.Cerrado else False],
        'bioma_Mata Atlântica': [True if data.bioma == Bioma.MataAtlantica else False],
        'bioma_Pampa': [True if data.bioma == Bioma.Pampa else False],
        'bioma_Pantanal': [True if data.bioma == Bioma.Pantanal else False],
        'ano_normalizado': [2], # Deixado como 2 (2024) pois o modelo não leva muito em consideração o ano para prever o resultado
        'media_precipitacao': [data.precipitacao],
        'media_dias_sem_chuva': [data.dias_sem_chuva]
    }
    
    dataframe = pd.DataFrame(data_dict)
    
    pred = regression_model.predict(dataframe)[0]
    
    df_ref = pd.read_csv(ref_stats_path)
    
     # Adquire o limite baseado no mês e bioma
    stats = df_ref[(df_ref['mes'] == data.mes.name) & (df_ref['bioma'] == data.bioma.name)].iloc[0]
    
    risk = (pred - stats['mean']) / stats['std']
    risk_percent = min(max((risk[0] * 10) + 50, 1), 100)
    print(risk_percent)
    
    return {
        "percentualRisco": round(risk_percent, 2)
    }