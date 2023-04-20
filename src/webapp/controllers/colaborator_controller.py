from fastapi import APIRouter, status, Response
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from src.infra.repositories.implementation import ColaboratorRepository, ColaboratorTypeRepository
from src.infra.adapters.db_config.db_config import DbConfig
from src.webapp.controllers.base_controller import BaseController
from src.webapp.models.colaborator_requests import ColaboratorRequestInsert, ColaboratorRequestUpdate
from src.domain.entities import Colaborator
from src.domain.enums import StatusEnum

colaborator_route = APIRouter()
colaborator_router = InferringRouter()

@cbv(colaborator_router)
class ColaboratorController(BaseController):
    def __init__(self):
        super().__init__(DbConfig())
        self.default_repo = ColaboratorRepository(self.db)

    @colaborator_router.get("/{id}/", status_code=status.HTTP_200_OK)
    async def get(self, id: int):
        result = self.default_repo.get(id=id)
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result

    @colaborator_router.get("/", status_code=status.HTTP_200_OK)
    async def list(self):
        result = self.default_repo.get_all()
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result

    @colaborator_router.post("/", status_code=status.HTTP_201_CREATED)
    async def add(self, data: ColaboratorRequestInsert):
        repo = ColaboratorTypeRepository(self.db)
        if (repo.get(data.colaborator_type_id) is None):
            return Response(f'Tipo de colaborador näo encontrado. [id={data.colaborator_type_id}]', status_code=status.HTTP_400_BAD_REQUEST)

        str_default = 'Já existe colaborador com'
        colaborator = self.default_repo.get_by_name(data.name)
        if (colaborator):
            return Response(f'{str_default} essa nome.[name={data.name}]', status_code=status.HTTP_400_BAD_REQUEST)

        colaborator = self.default_repo.get_by_cpf(data.cpf)
        if (colaborator):
            return Response(f'{str_default} com esse CPF.[cpf={data.cpf}]', status_code=status.HTTP_400_BAD_REQUEST)

        colaborator = self.default_repo.get_by_email(data.email)
        if (colaborator):
            return Response(f'{str_default} esse email.[email={data.email}]', status_code=status.HTTP_400_BAD_REQUEST)

        new_obj = Colaborator(id=1, cpf=data.cpf, email=data.email, name=data.name, cell_phone=data.cell_phone, cell_phone2=data.cell_phone2, colaborator_type_id=data.colaborator_type_id)
        new_obj.validate()
        self.default_repo.add(new_obj)
        self.db.commit()
        return new_obj

    @colaborator_router.put("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
    async def update(self, id: int, data: ColaboratorRequestUpdate):
        repo = ColaboratorTypeRepository(self.db)
        if (repo.get(data.colaborator_type_id) is None):
            return Response(f'Tipo de colaborador näo encontrado. [id={data.colaborator_type_id}]', status_code=status.HTTP_400_BAD_REQUEST)

        colaborator = self.default_repo.get_by_name(data.name)
        if colaborator:
            if colaborator.id != id:
                return Response(f'Ja existe Colaborador com esse nome.[name={data.name}]')

        colaborator = self.default_repo.get_by_email(data.email)
        if (colaborator):
            if colaborator.id != id:
                return Response(f'Ja existe Colaborador com essa email.[email={data.email}]')

        colaborator_to_update = self.default_repo.get(id)
        if (colaborator_to_update is None):
            return Response(f'Colaborador não encontrado. [id={id}]', status_code=status.HTTP_404_NOT_FOUND)

        colaborator_to_update.email=data.email
        colaborator_to_update.name=data.name
        colaborator_to_update.cell_phone=data.cell_phone
        colaborator_to_update.cell_phone2=data.cell_phone2
        colaborator_to_update.validate()
        self.db.commit()
        return

    @colaborator_router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
    async def delete(self, id: int):
        colaborator =  self.default_repo.get(id)
        if (colaborator is None):
            return Response(f'Colaborador não encontrado. [id={id}]', status_code=status.HTTP_404_NOT_FOUND)

        colaborator.status = StatusEnum.LOGICAMENTE_DELETADO
        self.db.commit()
        return

colaborator_route.include_router(colaborator_router)
