from rest_framework import serializers

from .models import *


class OldManInfoSerialize(serializers.ModelSerializer):
    class Meta:
        model = OldManInfo
        fields = '__all__'


class PhoneNumberSerialize(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ('phone_number',)

    def to_representation(self, instance):
        return instance.phone_number

    def create(self, validated_data):
        qr_code_id=validated_data['qr_code_id']
        phone_number=validated_data['phone_number']
        print('qrcodeid:'+qr_code_id)
        print('phone_number'+phone_number)
        pass


class PhoneNumberRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.phone_number


class QrCodeSerialize(serializers.ModelSerializer):
    old_man_info = OldManInfoSerialize()  # 这里的info是model外键的related_name
    # phone_number = PhoneNumberRelatedField(read_only=True, many=True)
    phone_number = PhoneNumberSerialize(read_only=True, many=True)

    class Meta:
        model = QrCode
        fields = '__all__'

    # def create(self, validated_data):
    #     # print(validated_data)
    #     old_man_info = validated_data['old_man_info']
    #     # oldManInfo = OldManInfo()
    #     # oldManInfo.name = old_man_info.name
    #     # oldManInfo.address = old_man_info.address
    #     # oldManInfo.age = old_man_info.age
    #     # oldManInfo.medical_history = old_man_info.medical_history
    #     # oldManInfo.allergy = old_man_info.allergy
    #     # oldManInfo.blood_type = old_man_info.blood_type
    #     # oldManInfo.drugs = old_man_info.drugs
    #     # oldManInfo.treatment = old_man_info.treatment
    #     # oldManInfo.save()
    #     oldManInfo = OldManInfo.objects.create(name=old_man_info['name'],
    #                                            address=old_man_info['address'],
    #                                            age=old_man_info['age'],
    #                                            medical_history=old_man_info['medical_history'],
    #                                            allergy=old_man_info['allergy'],
    #                                            blood_type=old_man_info['blood_type'],
    #                                            drugs=old_man_info['drugs'],
    #                                            treatment=old_man_info['treatment'])
    #     oldManInfo.save()
    #     qrCode = QrCode.objects.create(qr_code_id=validated_data['qr_code_id'], old_man_info=oldManInfo)
    #     # phone_number = validated_data['phone_number']
    #     # for pn in phone_number:
    #     #     PhoneNumber(phone_number=pn, content_object=qrCode).save()
    #     qrCode.save()
    #     return qrCode
    #
    # def update(self, instance, validated_data):
    #     instance.old_man_info=validated_data['old_man_info']
    #     return instance
