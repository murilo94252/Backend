from pydantic import BaseModel, EmailStr, Field


class ParticipanteBase(BaseModel):
    nome: str = Field(..., min_length=1)
    email: EmailStr
    curso: str = Field(..., min_length=1)


class ParticipanteCreate(ParticipanteBase):
    pass


class ParticipanteUpdate(ParticipanteBase):
    pass


class Participante(ParticipanteBase):
    id: int
