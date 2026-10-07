"""Datos persistentes del sistema de terminal, almacenados en MongoDB Atlas."""

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django_mongodb_backend.fields import ObjectIdAutoField


class Participante(models.Model):
    id = ObjectIdAutoField(primary_key=True)
    codigo = models.CharField(max_length=32, unique=True)
    nombre = models.CharField(max_length=200)

    class Meta:
        db_table = "participantes"
        ordering = ["codigo"]

    def clean(self):
        super().clean()
        self.codigo = self.codigo.strip()
        self.nombre = self.nombre.strip()
        errores = {}
        if not self.codigo:
            errores["codigo"] = "El código del participante es obligatorio."
        if not self.nombre:
            errores["nombre"] = "El nombre del participante es obligatorio."
        if errores:
            raise ValidationError(errores)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Taller(models.Model):
    id = ObjectIdAutoField(primary_key=True)
    codigo = models.CharField(max_length=32, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, default="")
    cupos = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    revision = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        db_table = "talleres"
        ordering = ["fecha_inicio", "codigo"]

    def clean(self):
        super().clean()
        self.codigo = self.codigo.strip()
        self.nombre = self.nombre.strip()
        errores = {}
        if not self.codigo:
            errores["codigo"] = "El código del taller es obligatorio."
        if not self.nombre:
            errores["nombre"] = "El nombre del taller es obligatorio."
        if self.fecha_inicio and self.fecha_fin and self.fecha_fin <= self.fecha_inicio:
            errores["fecha_fin"] = "El fin debe ser posterior al inicio del taller."
        if errores:
            raise ValidationError(errores)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Inscripcion(models.Model):
    class Estado(models.TextChoices):
        CONFIRMADA = "confirmada", "Confirmada"

    id = ObjectIdAutoField(primary_key=True)
    participante = models.ForeignKey(
        Participante, on_delete=models.PROTECT, related_name="inscripciones"
    )
    taller = models.ForeignKey(
        Taller, on_delete=models.PROTECT, related_name="inscripciones"
    )
    estado = models.CharField(
        max_length=20, choices=Estado.choices, default=Estado.CONFIRMADA
    )
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "inscripciones"
        ordering = ["fecha_solicitud", "id"]
        constraints = [
            models.UniqueConstraint(
                fields=["participante", "taller"],
                name="inscripcion_participante_taller_unica",
            )
        ]

    def __str__(self):
        return f"{self.participante_id} -> {self.taller_id} ({self.estado})"


class Contador(models.Model):
    """Secuencias compartidas para los códigos visibles P-001 y T-001."""

    id = ObjectIdAutoField(primary_key=True)
    nombre = models.CharField(max_length=32, unique=True)
    valor = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "contadores"
