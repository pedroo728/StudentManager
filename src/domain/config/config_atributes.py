from collections import namedtuple
FieldLen = namedtuple('FieldLen', 'min max exact')

DESCRIPTION_FIELD = FieldLen(5, 100, 0)
EMAIL_FIELD = FieldLen(0, 100, 0)
NAME_FIELD = FieldLen(5, 100, 0)
CELLPHONE_FIELD = FieldLen(0, 0, 11)
CPF_FIELD = FieldLen(0, 0, 11)
