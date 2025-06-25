from typing import Optional
from typing_extensions import TypedDict

class NarrativeState(TypedDict):
    patient_id: int
    fuente: str
    historial: str
    eventos: Optional[str]
    progresion: Optional[str]
    contenido: Optional[str]
    narrativa: Optional[str]