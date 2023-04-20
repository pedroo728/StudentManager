from fastapi import APIRouter, status, Response
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from src.infra.repositories.implementation.group_student_repository import GroupStudentRepository
from src.infra.adapters.db_config.db_config import DbConfig
from src.webapp.controllers.base_controller import BaseController

group_student_route = APIRouter()
group_student_router = InferringRouter()

@cbv(group_student_router)
class GroupStudentController(BaseController):
    def __init__(self):
        super().__init__(DbConfig())
        self.default_repo = GroupStudentRepository(self.db)

    @group_student_router.get("/{id}/", status_code=status.HTTP_200_OK)
    async def get(self, id: int):
        result = self.default_repo.get(id=id)
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result

    @group_student_router.get("/", status_code=status.HTTP_200_OK)
    async def list(self):
        result = self.default_repo.get_all()
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result

group_student_route.include_router(group_student_router)
