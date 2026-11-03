from fastapi import APIRouter
from model.evento import Evento, EventoCreate, EventoUpdate
from service import evento_service

router = APIRouter(prefix="/eventos", tags=["Eventos"])


@router.post("", response_model=Evento, status_code=201)
def cadastrar_evento(evento: EventoCreate):
    return evento_service.criar_evento(evento)


@router.get("", response_model=list[Evento])
def listar_eventos():
    return evento_service.listar_eventos()


@router.get("/{evento_id}", response_model=Evento)
def consultar_evento(evento_id: int):
    return evento_service.buscar_evento(evento_id)


@router.put("/{evento_id}", response_model=Evento)
def atualizar_evento(evento_id: int, evento: EventoUpdate):
    return evento_service.atualizar_evento(evento_id, evento)


@router.delete("/{evento_id}", status_code=204)
def excluir_evento(evento_id: int):
    evento_service.excluir_evento(evento_id)
