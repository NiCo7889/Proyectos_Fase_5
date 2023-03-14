from fastapi import FastAPI, HTTPException # instalo e importon fastapi 
from fastapi.responses import JSONResponse  # importo JSONResponse para poder devolver un diccionario como respuesta    
from pydantic import BaseModel, constr, validator # importo BaseModel para poder crear modelos de datos y constr para validar los datos que recibo y validator para validar los datos que recibo
import database as db # importo la base de datos que cree en database.py 
import helpers # importo helpers para poder usar la funcion dni_valido que cree en helpers.py 


headers = {"content-type": "charset=utf-8"} # creo un diccionario con los headers que quiero que tenga la respuesta de la API 


class ModeloCliente(BaseModel): # creo la clase ModeloCliente que hereda de BaseModel para validar los datos que recibo
    dni: constr(min_length=3, max_length=3)
    nombre: constr(min_length=2, max_length=30)
    apellido: constr(min_length=2, max_length=30)


class ModeloCrearCliente(ModeloCliente): # creo la clase ModeloCrearCliente que hereda de ModeloCliente para validar los datos que recibo y ademas creo un validador para validar el dni 
    @validator("dni")
    def validar_dni(cls, dni):
        if not helpers.dni_valido(dni, db.Clientes.lista):
            raise ValueError("Cliente ya existente o DNI incorrecto")
        return dni

# creo la para instanciar la clase FastAPI y le paso los parametros que quiero que tenga la API
app = FastAPI( # creo la app para instanciar la clase FastAPI
    title="API del Gestor de clientes",
    description="Ofrece diferentes funciones para gestionar los clientes.")

# creo las rutas para cada funcion que cree en database.py, le paso los parametros que quiero que tenga la ruta y le paso la funcion que quiero que ejecute
@app.get("/clientes/", tags=["Clientes"]) # creo la ruta para la funcion clientes
async def clientes():
    content = [cliente.to_dict() for cliente in db.Clientes.lista]
    return JSONResponse(content=content, headers=headers)


@app.get("/clientes/buscar/{dni}/", tags=["Clientes"]) 
async def clientes_buscar(dni: str):
    cliente = db.Clientes.buscar(dni=dni)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return JSONResponse(content=cliente.to_dict(), headers=headers)


@app.post("/clientes/crear/", tags=["Clientes"])
async def clientes_crear(datos: ModeloCrearCliente):
    cliente = db.Clientes.crear(datos.dni, datos.nombre, datos.apellido)
    if cliente:
        return JSONResponse(content=cliente.to_dict(), headers=headers)
    raise HTTPException(status_code=404)


@ app.put("/clientes/actualizar/", tags=["Clientes"])
async def clientes_actualizar(datos: ModeloCliente):
    if db.Clientes.buscar(datos.dni):
        cliente = db.Clientes.modificar(datos.dni, datos.nombre, datos.apellido)
        if cliente:
            return JSONResponse(content=cliente.to_dict(), headers=headers)
    raise HTTPException(status_code=404)


@app.delete("/clientes/borrar/{dni}/", tags=["Clientes"])
async def clientes_borrar(dni: str):
    if db.Clientes.buscar(dni=dni):
        cliente = db.Clientes.borrar(dni=dni)
        return JSONResponse(content=cliente.to_dict(), headers=headers)
    raise HTTPException(status_code=404)

print("Servidor de la API...")