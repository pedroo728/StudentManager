from fastapi import APIRouter, status, Response
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from src.domain.entities.student import Student
from src.infra.repositories.implementation.student_repository import StudentRepository
from src.infra.adapters.db_config.db_config import DbConfig
from src.webapp.controllers.base_controller import BaseController
from src.domain.enums.status_enum import StatusEnum
from src.webapp.models.student_request_insert_update import StudentRequestInsertUpdate

student_route = APIRouter()
student_router = InferringRouter()

@cbv(student_router)
class StudentController(BaseController):
    def __init__(self):
        super().__init__(DbConfig())
        self.default_repo = StudentRepository(self.db)

    @student_router.get("/{id}/", status_code=status.HTTP_200_OK)
    async def get(self, id: int):
        result = self.default_repo.get(id=id)
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result

    @student_router.get("/", status_code=status.HTTP_200_OK)
    async def list(self):
        result = self.default_repo.get_all()
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result

    @student_router.post("/", status_code=status.HTTP_200_OK)
    async def add(self, data: StudentRequestInsertUpdate):
        student = self.default_repo.get_by_name(data.name)
        if (student):
            return Response(f'Ja existe aluno com esse nome.[name={data.name}]')

        student = self.default_repo.get_by_name(data.name)
        if (student):
            return Response(f'Ja existe Aluno com essa nome.[name={data.name}]')

        student = self.default_repo.get_by_name(data.cpf)
        if (student):
            return Response(f'Ja existe Aluno com essa nome.[name={data.name}]')

        new_obj = Student(id=1, cpf=data.cpf, email=data.email, name=data.email, cell_phone=data.cell_phone, cell_phone2=data.cell_phone2)
        new_obj.validate()
        self.default_repo.add(new_obj)
        self.db.commit()
        return new_obj

    @student_router.put("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
    async def update(self, id: int, data: StudentRequestInsertUpdate):
        student = self.default_repo.get_by_name(data.name)
        if (student):
            if student.id != id:
                return Response(f'Ja existe Aluno com esse nome.[name={data.name}]')

        student_to_update = self.default_repo.get(id)
        if (student_to_update is None):
            return Response(f'Aluno não encontrado. [id={id}]', status_code=status.HTTP_404_NOT_FOUND)

        student_to_update.email=data.email
        student_to_update.name=data.name
        student_to_update.cell_phone=data.cell_phone
        student_to_update.cell_phone2=data.cell_phone2
        student_to_update.situation=data.situation
        student_to_update.validate()
        self.db.commit()
        return

    @student_router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
    async def delete(self, id: int):
        student =  self.default_repo.get(id)
        if (student):
            return Response(f'Aluno não encontrado. [id={id}]', status_code=status.HTTP_404_NOT_FOUND)

        student.status = StatusEnum.LOGICAMENTE_DELETADO
        self.db.commit()
        return

student_route.include_router(student_router)
