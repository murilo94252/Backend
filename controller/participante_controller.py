from fastapi import APIRouter
from model.participante import Participante, ParticipanteCreate, ParticipanteUpdate
from service import participante_service

router = APIRouter(prefix="/participantes", tags=["Participantes"])


@router.post("", response_model=Participante, status_code=201)
def cadastrar_participante(participante: ParticipanteCreate):
    return participante_service.criar_participante(participante)


@router.get("", response_model=list[Participante])
def listar_participantes():
    return participante_service.listar_participantes()


@router.get("/{participante_id}", response_model=Participante)
def consultar_participante(participante_id: int):
    return participante_service.buscar_participante(participante_id)


@router.put("/{participante_id}", response_model=Participante)
def atualizar_participante(participante_id: int, participante: ParticipanteUpdate):
    return participante_service.atualizar_participante(participante_id, participante)


@router.delete("/{participante_id}", status_code=204)
def excluir_participante(participante_id: int):
    participante_service.excluir_participante(participante_id)
