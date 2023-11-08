from django.contrib import admin
from cursos.models import Curso, Alumno, Instructor


class filtroAlumnos(admin.ModelAdmin):
    filter_horizontal = ("alumnos",)


admin.site.register(Curso, filtroAlumnos)
admin.site.register(Alumno)
admin.site.register(Instructor)
# Register your models here.
