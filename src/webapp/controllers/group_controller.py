from fastapi import APIRouter, status, Response
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from src.domain.enums.status_enum import StatusEnum
from src.domain.entities.group import Group
from src.infra.repositories.implementation.group_repository import GroupRepository
from src.infra.adapters.db_config.db_config import DbConfig
from src.webapp.controllers.base_controller import BaseController
from src.webapp.models.group_request_insert_update import GroupRequestInsertUpdate

group_route = APIRouter()
group_router = InferringRouter()

@cbv(group_router)
class GroupController(BaseController):
    def __init__(self):
        super().__init__(DbConfig())
        self.default_repo = GroupRepository(self.db)

    @group_router.get("/{id}/", status_code=status.HTTP_200_OK)
    async def get(self, id: int):
        result = self.default_repo.get(id=id)
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result

    @group_router.get("/", status_code=status.HTTP_200_OK)
    async def list(self):
        result = self.default_repo.get_all()
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result
    
    
    @group_router.post("/", status_code=status.HTTP_200_OK)
    async def add(self, data: GroupRequestInsertUpdate):
        group = self.default_repo.get_by_group_id(data.group_id)
        if (group):
            return Response(f'Ja existe Turma com essa ID.[name={data.group_id}]')
        
        group = self.default_repo.get_by_colaborador_id(data.colaborator_id)
        if (group):
            return Response(f'Ja existe Turma com esse Colaborador.[name={data.colaborator_id}]')

        group = self.default_repo.get_by_level(data.level)
        if (group):
            return Response(f'Ja existe Turma com essa Nivel.[name={data.level}]')

        new_obj = Group(id=1, status=StatusEnum.ATIVO, group_id=data.group_id, colaborator_id=data.colaborator_id, level=data.level, max_size=data.max_size)
        new_obj.validate()
        self.default_repo.add(new_obj)
        self.db.commit()
        return new_obj
    

    @group_router.put("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
    async def update(self, id: int, data: GroupRequestInsertUpdate):
        group = self.default_repo.get_by_goup_id(data.group_id)
        if group:
            if group.id != id:
                return Response(f'Ja existe Turma com essa ID.[name={data.group_id}]')
            
        group = self.default_repo.get_by_colaborador_id(data.colaborator_id)
        if (group):
            if group.id != id:
                return Response(f'Ja existe Turma com esse Colaborador.[name={data.colaborator_id}]')
            
        group_to_update = self.default_repo.get(id=id)
        if (group_to_update is None):
            return Response(f'Grupo não encontrado.[id={id}]', status_code=status.HTTP_404_NOT_FOUND)
        
        group_to_update.group_id = data.group_id
        group_to_update.colaborator_id = data.colaborator_id
        group_to_update.level = data.level
        group_to_update.max_size = data.max_size
        group_to_update.validate()
        self.db.commit()
        return
    
    @group_router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
    async def delete(self, id: int):
        group = self.default_repo.get(id=id)
        if (group is None):
            return Response(f'Grupo não encontrado.[id={id}]', status_code=status.HTTP_404_NOT_FOUND)
        
        group.status = StatusEnum.LOGICAMENTE_DELETADO
        self.db.commit()
        return
                
group_route.include_router(group_router)
