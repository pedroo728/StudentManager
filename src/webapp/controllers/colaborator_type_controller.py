from fastapi import APIRouter, status, Response
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from src.infra.repositories.implementation.colaborator_type_repository import ColaboratorTypeRepository
from src.infra.adapters.db_config.db_config import DbConfig
from src.webapp.controllers.base_controller import BaseController

colaborator_type_route = APIRouter()
colaborator_type_router = InferringRouter()

@cbv(colaborator_type_router)
class ColaboratorTypeController(BaseController):
    def __init__(self):
        super().__init__(DbConfig())
        self.default_repo = ColaboratorTypeRepository(self.db)

    @colaborator_type_router.get("/{id}/", status_code=status.HTTP_200_OK)
    async def get(self, id: int):
        result = self.default_repo.get(id=id)
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result

    @colaborator_type_router.get("/", status_code=status.HTTP_200_OK)
    async def list(self):
        result = self.default_repo.get_all()
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result

colaborator_type_route.include_router(colaborator_type_router)
