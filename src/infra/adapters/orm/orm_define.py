from src.domain.entities import LevelType,ColaboratorType, Colaborator, Student, Group, GroupSchedule, GroupStudent, GroupColaborator 
# from src.domain.entities import ColaboratorType, ClassType, Colaborator, ClassBT, ClassSchedule
from .database_schema import mapper_registry, level_type_schema, colaborator_type_schema, colaborator_schema, student_schema, group_schema, group_schedule_schema, group_student_schema, group_colaborator_schema 

def start_mappers():
    mapper_registry.map_imperatively(LevelType, level_type_schema)
    mapper_registry.map_imperatively(ColaboratorType, colaborator_type_schema)
    mapper_registry.map_imperatively(Colaborator, colaborator_schema)
    mapper_registry.map_imperatively(Student, student_schema)
    mapper_registry.map_imperatively(Group, group_schema)
    mapper_registry.map_imperatively(GroupSchedule, group_schedule_schema)
    mapper_registry.map_imperatively(GroupStudent, group_student_schema)
    mapper_registry.map_imperatively(GroupColaborator, group_colaborator_schema)
