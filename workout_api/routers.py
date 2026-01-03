from fastapi import APIRouter
from workout_api.atleta.controller import router as atleta_router
from workout_api.categorias.controller import router as categorias_router
from workout_api.centro_treinamento.controller import (
    router as centro_treinamento_router,
)

api_router = APIRouter()


api_router.include_router(atleta_router)
api_router.include_router(categorias_router)
api_router.include_router(centro_treinamento_router)
