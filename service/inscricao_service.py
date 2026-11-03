from fastapi import HTTPException
from service.evento_service import buscar_evento
from service.participante_service import buscar_participante, participantes

inscricoes: list[dict] = []


def inscrever(evento_id: int, participante_id: int) -> dict:
    evento = buscar_evento(evento_id)
    participante = buscar_participante(participante_id)

    ja_inscrito = any(
        i["evento_id"] == evento_id and i["participante_id"] == participante_id
        for i in inscricoes
    )
    if ja_inscrito:
        raise HTTPException(status_code=400, detail="Participante já está inscrito neste evento.")

    total_inscritos = len([i for i in inscricoes if i["evento_id"] == evento_id])
    if total_inscritos >= evento.capacidade:
        raise HTTPException(status_code=400, detail="Não existem vagas disponíveis para este evento.")

    inscricoes.append({"evento_id": evento_id, "participante_id": participante_id})
    return {"evento": evento, "participante": participante}


def listar_inscritos(evento_id: int) -> list:
    buscar_evento(evento_id)
    ids = [i["participante_id"] for i in inscricoes if i["evento_id"] == evento_id]
    return [p for p in participantes if p.id in ids]
