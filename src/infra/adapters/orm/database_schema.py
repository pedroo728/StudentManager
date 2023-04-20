from sqlalchemy import MetaData, Column, ForeignKey, Integer, Table, BigInteger, VARCHAR, TypeDecorator, Time, Date
from sqlalchemy.orm import registry
from src.domain.enums import StatusEnum, SituationStudentEnum
from src.domain.config.config_atributes import NAME_FIELD, DESCRIPTION_FIELD, EMAIL_FIELD, CELLPHONE_FIELD, CPF_FIELD

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

class StudentSituationType(TypeDecorator):
    impl = Integer

    def __init__(self, intflagtype, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._intflagtype = intflagtype

    def process_bind_param(self, value, dialect):
        return value.value

    def process_result_value(self, value, dialect):
        return self._intflagtype(value)

class StatusType(TypeDecorator):
    impl = Integer
    cache_ok = True

    def __init__(self, intflagtype, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._intflagtype = intflagtype

    def process_bind_param(self, value, dialect):
        return value.value

    def process_result_value(self, value, dialect):
        return self._intflagtype(value)

class CpfType(TypeDecorator):
    impl = VARCHAR(CPF_FIELD.exact)

class CellPhoneType(TypeDecorator):
    impl = VARCHAR(CELLPHONE_FIELD.exact)

class DescriptionType(TypeDecorator):
    impl = VARCHAR(DESCRIPTION_FIELD.max)

class NameType(DescriptionType):
    impl = VARCHAR(NAME_FIELD.max)

class EmailType(TypeDecorator):
    impl = VARCHAR(EMAIL_FIELD.max)

list_base_schema = [
    Column('id', Integer, nullable = False, primary_key = True),
    Column('status', StatusType(StatusEnum), nullable = False)
]

list_level_type_schema = [x.copy() for x in list_base_schema] + [Column('description', DescriptionType, nullable = False)]
list_colaborator_type_schema = [x.copy() for x in list_level_type_schema]

level_type_schema = Table(
    'LevelType', 
    mapper_registry.metadata,
    *list_level_type_schema
)

colaborator_type_schema = Table(
    'ColaboratorType', 
    mapper_registry.metadata,
    *list_colaborator_type_schema
)

colaborator_schema = Table(
    'Colaborator',
    mapper_registry.metadata,
    Column('id', Integer, nullable = False, primary_key = True),
    Column('status', StatusType(StatusEnum), nullable = False),
    Column('cpf', CpfType, nullable = False),
    Column('email', EmailType, nullable = False),
    Column('name', NameType, nullable = False),
    Column('cell_phone', CellPhoneType, nullable = False),
    Column('cell_phone2', CellPhoneType, nullable = True),
    Column('colaborator_type_id', ForeignKey("ColaboratorType.id"), nullable=False),
)

student_schema = Table(
    'Student',
    mapper_registry.metadata,
    Column('id', Integer, nullable = False, primary_key = True),
    Column('status', StatusType(StatusEnum), nullable = False),
    Column('cpf', CpfType, nullable = False),
    Column('email', EmailType, nullable = False),
    Column('name', NameType, nullable = False),
    Column('cell_phone', CellPhoneType, nullable = False),
    Column('cell_phone2', CellPhoneType, nullable = True),
    Column('situation', StudentSituationType(SituationStudentEnum), nullable = False)
)

group_schema = Table(
    'Group',
    mapper_registry.metadata,
    Column('id', BigInteger,  nullable = False, primary_key = True),
    Column('status', StatusType(StatusEnum), nullable = False),
    Column('max_students', Integer, nullable = False),
    Column('level_type_id', ForeignKey("LevelType.id"), nullable=False),
)

group_schedule_schema = Table(
    'GroupSchedule',
    mapper_registry.metadata,
    Column('id', BigInteger,  nullable = False, primary_key = True),
    Column('status', StatusType(StatusEnum), nullable = False),
    Column('team_id', ForeignKey("Group.id"), nullable=False),
    Column('day_week', Integer, nullable=False),
    Column('hour_day', Time, nullable=False),
)

group_student_schema = Table(
    'GroupStudent',
    mapper_registry.metadata,
    Column('id', BigInteger,  nullable = False, primary_key = True),
    Column('status', StatusType(StatusEnum), nullable = False),
    Column('group_id', ForeignKey("Group.id"), nullable=False),
    Column('student_id', ForeignKey("Student.id"), nullable=False),
    Column('start_date', Date, nullable = False)
)

group_colaborator_schema = Table(
    'GroupColaborator',
    mapper_registry.metadata,
    Column('id', BigInteger,  nullable = False, primary_key = True),
    Column('status', StatusType(StatusEnum), nullable = False),
    Column('group_id', ForeignKey("Group.id"), nullable=False),
    Column('colaborator_id', ForeignKey("Colaborator.id"), nullable=False),
    Column('start_date', Date, nullable = False)
)
