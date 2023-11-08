from django.db import models


class Curso(models.Model):
    name = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    dias = models.CharField(max_length=100)
    fechaInicio = models.DateField()
    fechaFinalizacion = models.DateField()
    instructor = models.ForeignKey(
        "Instructor", on_delete=models.CASCADE, blank=True, null=True
    )
    alumnos = models.ManyToManyField(
        "Alumno", blank=True, null=True, related_name="alumnos"
    )

    def __str__(self):
        return self.name


class Alumno(models.Model):
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    fechaNacimiento = models.DateField()
    sexo = models.CharField(max_length=1)
    documento = models.IntegerField()
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    # cursosInscritos = models.ManyToManyField("Curso")

    def __str__(self):
        return f"{self.name} {self.apellido}"


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1)
    documento = models.IntegerField()
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    # cursos = models.ManyToManyField("Curso")

    def __str__(self):
        return f"{self.name} {self.apellido}"


# Create your models here.
