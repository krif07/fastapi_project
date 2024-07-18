# Ejecutar la aplicación sin docker
uvicorn app.main:app --reload

# Construir el proyecto en docker y ejecutar
docker build -t fastapi_project .
docker run -d --name fastapi_container -p 8000:80 fastapi_project


# Probar en postman
Crear producto
POST
http://127.0.0.1:8000/products/
{
    "name": "Laptop",
    "price": 1200.00,
    "quantity": 10,
    "category": "Electronics"
}

# Consultar un producto
GET
http://127.0.0.1:8000/products/1

# Eliminar un producto
DELETE
http://127.0.0.1:8000/products/1