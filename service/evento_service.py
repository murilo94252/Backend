from fastapi import HTTPException
from model.evento import Evento, EventoCreate, EventoUpdate

eventos: list[Evento] = []
proximo_id = 1


def criar_evento(dados: EventoCreate) -> Evento:
    global proximo_id
    evento = Evento(id=proximo_id, **dados.model_dump())
    eventos.append(evento)
    proximo_id += 1
    return evento


def listar_eventos() -> list[Evento]:
    return eventos


def buscar_evento(evento_id: int) -> Evento:
    for evento in eventos:
        if evento.id == evento_id:
            return evento
    raise HTTPException(status_code=404, detail="Evento não encontrado.")


def atualizar_evento(evento_id: int, dados: EventoUpdate) -> Evento:
    evento = buscar_evento(evento_id)
    evento.titulo = dados.titulo
    evento.descricao = dados.descricao
    evento.data = dados.data
    evento.horario = dados.horario
    evento.local = dados.local
    evento.capacidade = dados.capacidade
    evento.categoria = dados.categoria
    return evento


def excluir_evento(evento_id: int) -> None:
    evento = buscar_evento(evento_id)
    eventos.remove(evento)
