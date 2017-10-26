from utils.choices import ChoiceEnum


class TaskStatus(ChoiceEnum):
    CREATED = 'creado'
    IN_PROGESS = 'en progreso'
    COMPLETED = 'completada'
