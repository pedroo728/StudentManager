from fastapi import APIRouter, status, Response
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from src.infra.repositories.implementation.group_schedule_repository import GroupScheduleRepository
from src.infra.adapters.db_config.db_config import DbConfig
from src.webapp.controllers.base_controller import BaseController

group_schedule_route = APIRouter()
group_schedule_router = InferringRouter()

@cbv(group_schedule_router)
class GroupScheduleController(BaseController):
    def __init__(self):
        super().__init__(DbConfig())
        self.default_repo = GroupScheduleRepository(self.db)

    @group_schedule_router.get("/{id}/", status_code=status.HTTP_200_OK)
    async def get(self, id: int):
        result = self.default_repo.get(id=id)
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result

    @group_schedule_router.get("/", status_code=status.HTTP_200_OK)
    async def list(self):
        result = self.default_repo.get_all()
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result

group_schedule_route.include_router(group_schedule_router)
