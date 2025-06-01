from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.producto import router as producto_router


app = FastAPI(
    title= "API de gestión de producto",
    version= "1.0.0",
    description= "API para gestionar producto"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ["*"] si quieres permitir todo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Traeremos los de las rutas (routers)
app.include_router(producto_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API"}