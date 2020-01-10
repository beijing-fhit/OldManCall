from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.fields import exceptions


# Create your models here.

class OldManInfo(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=30,null=True)
    age = models.PositiveIntegerField(null=True)
    medical_history = models.CharField(max_length=30,null=True)
    allergy = models.CharField(max_length=30,null=True)
    blood_type = models.CharField(max_length=10,null=True)
    drugs = models.CharField(max_length=30,null=True)
    treatment = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.name


# 一个二维码id对应多个电话号码
class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=50)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=50)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.phone_number


# 用于获取一个qrcode所对应的的所有电话号码
class PhoneNumberMethod:
    def get_phone_numbers(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            phone_numbers = PhoneNumber.objects.filter(content_type=ct, object_id=self.pk).order_by("pk")
            return phone_numbers
        except exceptions.ObjectDoesNotExist as e:
            return []


class QrCode(models.Model, PhoneNumberMethod):
    qr_code_id = models.CharField(max_length=50,primary_key=True)
    phone_number = GenericRelation(PhoneNumber)
    old_man_info = models.ForeignKey(OldManInfo, on_delete=models.CASCADE,related_name='info')

    def __str__(self):
        return self.qr_code_id
