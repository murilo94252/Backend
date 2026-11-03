from pydantic import BaseModel, Field
from datetime import date


class EventoBase(BaseModel):
    titulo: str = Field(..., min_length=1)
    descricao: str
    data: date
    horario: str
    local: str
    capacidade: int = Field(..., gt=0)
    categoria: str


class EventoCreate(EventoBase):
    pass


class EventoUpdate(EventoBase):
    pass


class Evento(EventoBase):
    id: int
