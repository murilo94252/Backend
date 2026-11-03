from fastapi import APIRouter
from model.participante import Participante
from service import inscricao_service

router = APIRouter(tags=["Inscrições"])


@router.post("/eventos/{evento_id}/inscricoes/{participante_id}", status_code=201)
def inscrever_participante(evento_id: int, participante_id: int):
    return inscricao_service.inscrever(evento_id, participante_id)


@router.get("/eventos/{evento_id}/inscricoes", response_model=list[Participante])
def listar_inscritos(evento_id: int):
    return inscricao_service.listar_inscritos(evento_id)
