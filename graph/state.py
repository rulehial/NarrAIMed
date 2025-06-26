from typing import Optional
from typing_extensions import TypedDict
from datetime import datetime

class NarrativeState(TypedDict):
    patient_id: int
    fuente: str
    historial: str
    eventos: Optional[str]
    medicacion: Optional[str]
    diagnostico_cie10: Optional[str]
    progresion: Optional[str]
    contenido: Optional[str]
    narrativa: Optional[str]
    laboratorio: Optional[str]
    cie10_ingreso: Optional[str]
    cie10_urgencia: Optional[str]