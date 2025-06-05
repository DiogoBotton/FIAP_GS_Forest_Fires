from pydantic import BaseModel
from enums import Mes, Bioma

class PredictRiskRequest(BaseModel):
    mes: Mes
    bioma: Bioma
    precipitacao: float
    dias_sem_chuva: int