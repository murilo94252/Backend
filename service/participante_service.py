from fastapi import HTTPException
from model.participante import Participante, ParticipanteCreate, ParticipanteUpdate

participantes: list[Participante] = []
proximo_id = 1


def criar_participante(dados: ParticipanteCreate) -> Participante:
    global proximo_id
    participante = Participante(id=proximo_id, **dados.model_dump())
    participantes.append(participante)
    proximo_id += 1
    return participante


def listar_participantes() -> list[Participante]:
    return participantes


def buscar_participante(participante_id: int) -> Participante:
    for participante in participantes:
        if participante.id == participante_id:
            return participante
    raise HTTPException(status_code=404, detail="Participante não encontrado.")


def atualizar_participante(participante_id: int, dados: ParticipanteUpdate) -> Participante:
    participante = buscar_participante(participante_id)
    participante.nome = dados.nome
    participante.email = dados.email
    participante.curso = dados.curso
    return participante


def excluir_participante(participante_id: int) -> None:
    participante = buscar_participante(participante_id)
    participantes.remove(participante)
