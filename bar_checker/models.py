from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class PressureRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pressure_records')
    systolic = models.PositiveSmallIntegerField()  # верхнее давление
    diastolic = models.PositiveSmallIntegerField()  # нижнее давление
    pulse = models.PositiveSmallIntegerField(null=True, blank=True)  # пульс
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)  # доп заметки

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['user', '-timestamp']),
        ]
        db_table = 'pressure_records'

    def __str__(self):
        return f"{self.user}: {self.systolic}/{self.diastolic} ({self.timestamp})"

    def clean(self):
        if self.systolic < self.diastolic:
            raise ValidationError("Верхнее давление не может быть меньше нижнего!")
        if self.systolic > 250 or self.diastolic > 150:
            raise ValidationError("Проверьте значения давления — они выходят за пределы нормы!")