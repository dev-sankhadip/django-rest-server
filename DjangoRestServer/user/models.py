from django.db import models


class User(models.Model):
    uid = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "test"
