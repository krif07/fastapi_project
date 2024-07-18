import uvicorn
from fastapi import FastAPI
from app.routers import products
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(products.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)