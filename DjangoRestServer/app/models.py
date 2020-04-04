from django.db import models


class App(models.Model):
    aId = models.CharField(max_length=5, primary_key=True)
    aName = models.CharField(max_length=20)
    aDetail = models.TextField()
    aCreatedOn = models.DateTimeField(auto_now_add=True)
    aUpdatedOn = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'app'
