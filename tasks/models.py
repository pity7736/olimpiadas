from django.db import models
from tasks.choices import TaskStatus


class NameModel(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=100, db_index=True)
    description = models.TextField(verbose_name='Descripción')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(NameModel):
    pass


class Task(NameModel):
    statuses = TaskStatus
    owner = models.ForeignKey(to='accounts.User', verbose_name='Dueño')
    categoty = models.ForeignKey(to=Category, verbose_name='Categoría')
    deadline = models.DateTimeField(verbose_name='Fecha límite', null=True, blank=True)
    status = models.CharField(
        verbose_name='Estado',
        max_length=50,
        choices=statuses.choices(),
        default=statuses.CREATED,
        db_index=True,
    )
