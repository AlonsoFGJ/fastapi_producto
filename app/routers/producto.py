from fastapi import APIRouter, HTTPException, Query
from app.database import get_conexion
from typing import List
from pydantic import BaseModel

#vamos a crear la variable para las rutas:
router = APIRouter(
    prefix="/producto",
    tags=["producto"]
)

class ProductoModel(BaseModel):
    id_producto: int
    titulo: str
    descripcion: str
    stock: int
    precio: float
    tipo: str

    class Config:
        from_attributes = True

#endpoints: GET, GET, POST, PUT, DELETE, PATCH
@router.get("/")
def obtener_productos():
    try:
        cone = get_conexion()
        cursor = cone.cursor()
        cursor.execute("SELECT id_producto,titulo,descripcion,stock,precio,tipo FROM producto")
        productos = []
        for id_producto,titulo,descripcion,stock,precio,tipo in cursor:
            productos.append({
                "id_producto": id_producto,
                "titulo": titulo,
                "descripcion": descripcion,
                "stock": stock,
                "precio": precio,
                "tipo": tipo
            })
        cursor.close()
        cone.close()
        return productos
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@router.get("/{id_buscar}")
def obtener_producto(id_buscar: int):
    try:
        cone = get_conexion()
        cursor = cone.cursor()
        cursor.execute("SELECT id_producto,titulo,descripcion,stock,precio,tipo FROM producto WHERE id_producto = :id_producto"
                       ,{"id_producto": id_buscar})
        productoESP = cursor.fetchone()
        cursor.close()
        cone.close()
        if not productoESP:
            raise HTTPException(status_code=404, detail="producto no encontrado")
        return {
            "id_producto": id_buscar,
            "titulo": productoESP[1],
            "descripcion": productoESP[2],
            "stock": productoESP[3],
            "precio": productoESP[4],
            "tipo": productoESP[5]
        }
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    

@router.post("/")
def agregar_producto(id_producto:int, titulo:str, descripcion:str,stock:int, precio:int, tipo:str):
    try:
        cone = get_conexion()
        cursor = cone.cursor()
        cursor.execute("""
            INSERT INTO producto
            VALUES(:id_producto, :titulo, :descripcion,:stock, :precio, :tipo)
        """,{"id_producto":id_producto,"titulo":titulo,"descripcion":descripcion,"stock":stock,"precio":precio,"tipo":tipo})
        cone.commit()
        cursor.close()
        cone.close()
        return {"mensaje": "producto agregado con éxito"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    

@router.put("/{id_actualizar}")
def actualizar_producto(id_producto:int, titulo:str, descripcion:str,stock:int, precio:int, tipo:str):
    try:
        cone = get_conexion()
        cursor = cone.cursor()
        cursor.execute("""
                UPDATE producto
                SET titulo = :titulo,descripcion = :descripcion,stock = :stock,precio = :precio,tipo = :tipo
                WHERE id_producto = :id_producto
        """, {"id_producto":id_producto,"titulo":titulo,"descripcion":descripcion,"stock":stock,"precio":precio,"tipo":tipo})
        if cursor.rowcount==0:
            cursor.close()
            cone.close()
            raise HTTPException(status_code=404, detail="producto no encontrado")
        cone.commit()
        cursor.close()
        cone.close()
        return {"mensaje": "producto actualizado con éxito"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@router.delete("/{id_eliminar}")
def eliminar_producto(id_eliminar: int):
    try:
        cone = get_conexion()
        cursor = cone.cursor()
        cursor.execute("DELETE FROM producto WHERE id_producto = :id_producto"
                       ,{"id_producto": id_eliminar})
        if cursor.rowcount==0:
            cursor.close()
            cone.close()
            raise HTTPException(status_code=404, detail="producto no encontrado")
        cone.commit()
        cursor.close()
        cone.close()
        return {"mensaje": "producto eliminado con éxito"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


from typing import Optional

@router.patch("/{id_actualizar}")
def actualizar_parcial(id_actualizar:int, titulo:Optional[str]=None, descripcion:Optional[str]=None,stock:Optional[int]=None, precio:Optional[int]=None, tipo:Optional[str]=None):
    try:
        if not titulo and not descripcion and not stock and not precio and not tipo:
            raise HTTPException(status_code=400, detail="Debe enviar al menos 1 dato")
        cone = get_conexion()
        cursor = cone.cursor()

        campos = []
        valores = {"id_producto": id_actualizar}
        if titulo:
            campos.append("titulo = :titulo")
            valores["titulo"] = titulo
        if descripcion:
            campos.append("descripcion = :descripcion")
            valores["descripcion"] = descripcion
        if stock:
            campos.append("stock = :stock")
            valores["stock"] = stock
        if precio:
            campos.append("precio = :precio")
            valores["precio"] = precio
        if tipo:
            campos.append("tipo = :tipo")
            valores["tipo"] = tipo

        cursor.execute(f"UPDATE producto SET {', '.join(campos)} WHERE id_producto = :id_producto"
                       ,valores)
        if cursor.rowcount==0:
            cursor.close()
            cone.close()
            raise HTTPException(status_code=404, detail="producto no encontrado")
        cone.commit()
        cursor.close()
        cone.close()
        return {"mensaje": "producto actualizado con éxito"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
