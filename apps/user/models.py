from django.db import models

class User(models.Model):
    givenName = models.CharField(max_length=250)
    familyName = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=20)
    photo = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False, null=True)

    @property
    def name(self):
        return f"{self.givenName} {self.familyName }"

    @classmethod
    def post(cls, request):
        data = cls(**request.data)
        data.save()
        return data
