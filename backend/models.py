from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.

class OldManInfo(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    medical_history = models.CharField(max_length=30)
    allergy = models.CharField(max_length=30)
    blood_type = models.CharField(max_length=10)
    drugs = models.CharField(max_length=30)
    treatment = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# 一个二维码id对应多个电话号码
class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=50)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.phone_number


class QrCode(models.Model):
    qrCodeId = models.CharField(max_length=50)
    phone_numbers = GenericRelation(PhoneNumber)
    old_man_info = models.ForeignKey(OldManInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.qrCodeId
