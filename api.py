from fastapi import FastAPI, HTTPException # instalo e importon fastapi 
from fastapi.responses import JSONResponse  # importo JSONResponse para poder devolver un diccionario como respuesta    
from pydantic import BaseModel, constr, validator # importo BaseModel para poder crear modelos de datos y constr para validar los datos que recibo y validator para validar los datos que recibo
import database as db # importo la base de datos que cree en database.py 
import helpers # importo helpers para poder usar la funcion dni_valido que cree en helpers.py 


headers = {"content-type": "charset=utf-8"} # creo un diccionario con los headers que quiero que tenga la respuesta de la API 


class ModeloCliente(BaseModel): # creo la clase ModeloCliente que hereda de BaseModel para validar los datos que recibo
    dni: constr(min_length=3, max_length=3)
    Producto: constr(min_length=2, max_length=30)
    apellido: constr(min_length=2, max_length=30)


class ModeloCrearCliente(ModeloCliente): # creo la clase ModeloCrearCliente que hereda de ModeloCliente para validar los datos que recibo y ademas creo un validador para validar el dni 
    @validator("CD")
    def validar_CD(cls, CD):
        if not helpers.CD_valido(CD, db.Inventario.lista):
            raise ValueError("Producto ya existente o CD incorrecto")
        return CD

# creo la para instanciar la clase FastAPI y le paso los parametros que quiero que tenga la API
app = FastAPI( # creo la app para instanciar la clase FastAPI
    title="API del Gestor de Inventario",
    description="Ofrece diferentes funciones para gestionar el Inventario.")

# creo las rutas para cada funcion que cree en database.py, le paso los parametros que quiero que tenga la ruta y le paso la funcion que quiero que ejecute
@app.get("/Inventario/", tags=["Inventario"]) # creo la ruta para la funcion Inventario
async def Inventario():
    content = [db.Producto.to_dict() for producto in db.Inventario.lista]
    return JSONResponse(content=content, headers=headers)


@app.get("/Inventario/buscar/{CD}/", tags=["Inventario"]) 
async def Inventario_buscar(CD: str):
    producto = db.Inventario.buscar(CD=CD)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return JSONResponse(content=db.Producto.to_dict(), headers=headers)


@app.post("/Inventario/crear/", tags=["Inventario"])
async def Inventario_crear(datos: ModeloCrearCliente):
    producto = db.Inventario.crear(datos.CD, datos.producto, datos.categoria)
    if producto:
        return JSONResponse(content=db.Producto.to_dict(), headers=headers)
    raise HTTPException(status_code=404)


@ app.put("/Inventario/actualizar/", tags=["Inventario"])
async def Inventario_actualizar(datos: ModeloCliente):
    if db.Inventario.buscar(datos.CD):
        producto = db.Inventario.modificar(datos.CD, datos.producto, datos.categoria)
        if producto:
            return JSONResponse(content=db.Producto.to_dict(), headers=headers)
    raise HTTPException(status_code=404)


@app.delete("/Inventario/borrar/{CD}/", tags=["Inventario"])
async def Inventario_borrar(CD: str):
    if db.Inventario.buscar(CD=CD):
        producto = db.Inventario.borrar(CD=CD)
        return JSONResponse(content=db.Producto.to_dict(), headers=headers)
    raise HTTPException(status_code=404)

print("Servidor de la API...")