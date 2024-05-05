from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

id_contador = 1

class Articulo(BaseModel):
    id: int
    autor: str
    contenido: str
    categoria: str


Articulos: List[Articulo] = []

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la gestión de articulos"}



@app.post("/articulos/")
def crear_articulo(autor: str, contenido: str, categoria: str):
    global id_contador
    articulo = Articulo(id=id_contador, autor=autor, contenido=contenido, categoria=categoria)
    Articulos.append(articulo)
    id_contador += 1
    return articulo



@app.delete("/articulos/{articulo_id}")
def borrar_articulo(articulo_id: int):
    global Articulos
    for index, articulo in enumerate(Articulos):
        if articulo.id == articulo_id:
            Articulos.pop(index)
            return {"mensaje": "Articulo borrado"}
    return {"mensaje": "Error"}



@app.put("/articulos/{articulo_id}")
def modificar_articulo(articulo_id: int, articulo: Articulo):
    global Articulos
    for index, existing_articulo in enumerate(Articulos):
        if existing_articulo.id == articulo_id:
            if articulo.autor:
                Articulos[index].autor = articulo.autor
            if articulo.contenido:
                Articulos[index].contenido = articulo.contenido
            if articulo.categoria:
                Articulos[index].categoria = articulo.categoria
            return Articulos[index]
    return {"mensaje": "Error"}




@app.get("/articulos/{articulo_id}")
def leer_articulo(articulo_id: int):
    global Articulos
    for articulo in Articulos:
        if articulo.id == articulo_id:
            return articulo
    return {"mensaje": "Error"}
