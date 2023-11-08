from django.db import models
from cursos.models import Curso, Alumno

class alumnosYcursos (models.Model):
    Curso = models.ForeignKey("cursos.Curso", on_delete=models.CASCADE)

# Create your models here.
