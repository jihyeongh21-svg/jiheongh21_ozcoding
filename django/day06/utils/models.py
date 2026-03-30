from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField('생성일자',auto_now_add=True)
    updated = models.DateTimeField('수정일자',auto_now=True)

    class Meta:
        abstract = True