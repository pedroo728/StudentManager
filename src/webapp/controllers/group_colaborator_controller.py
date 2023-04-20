from fastapi import APIRouter, status, Response
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from src.infra.repositories.implementation.group_colaborator_repository import GroupColaboratorRepository
from src.infra.adapters.db_config.db_config import DbConfig
from src.webapp.controllers.base_controller import BaseController

group_colaborator_route = APIRouter()
group_colaborator_router = InferringRouter()

@cbv(group_colaborator_router)
class GroupColaboratorRepository(BaseController):
    def __init__(self):
        super().__init__(DbConfig())
        self.default_repo = GroupColaboratorRepository(self.db)

    @group_colaborator_router.get("/{id}/", status_code=status.HTTP_200_OK)
    async def get(self, id: int):
        result = self.default_repo.get(id=id)
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result

    @group_colaborator_router.get("/", status_code=status.HTTP_200_OK)
    async def list(self):
        result = self.default_repo.get_all()
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result

group_colaborator_route.include_router(group_colaborator_router)
