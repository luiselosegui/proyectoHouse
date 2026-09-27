from fastapi import FastAPI

app = FastAPI()

eventos = [
    {"id": 1, "titulo": "Jam session", "lugar": "Gràcia", "fecha": "2026-10-02"},
    {"id": 2, "titulo": "Quiz night", "lugar": "Poblenou", "fecha": "2026-10-03"},
]


@app.get("/eventos")
def listar_eventos():
    return eventos