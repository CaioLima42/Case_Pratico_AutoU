from django.db import models

from django.db import models

class CheckedEmail(models.Model):
    clientName = models.CharField(max_length=100, verbose_name="User Name")
    emailMesage = models.TextField(verbose_name="Email Mensage")
    relevence = models.BooleanField(default=False, verbose_name="Its Relevant?")
    response = models.TextField(verbose_name="Respose for email")

    class Meta:
        verbose_name = "CheckedEmail"
        verbose_name_plural = "CheckedEmail"
        ordering = ['-clientName']

    def __str__(self):
        return f"The email of {self.nome_usuario} ({'Is relevant' if self.relevancia else 'is not relevant'})"