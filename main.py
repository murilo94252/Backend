from fastapi import FastAPI
from controller import evento_controller, participante_controller, inscricao_controller

app = FastAPI(
    title="API de Gerenciamento de Eventos Acadêmicos",
    description="API REST para gerenciar eventos, participantes e inscrições",
    version="1.0.0",
)

app.include_router(evento_controller.router)
app.include_router(participante_controller.router)
app.include_router(inscricao_controller.router)


@app.get("/")
def root():
    return {"mensagem": "API de Eventos Acadêmicos no ar. Acesse /docs para ver o Swagger."}
