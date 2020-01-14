from django.core import serializers
from django.shortcuts import render
import requests
from django.http import *
from urllib import parse


from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from backend import utils
from .models import *
from .serializer import *


# Create your views here.
def index(request):
    return get_code(request)


def get_code(request):
    url = 'https://agency.ucallclub.com/wechart/Oauth2?'
    redirect_url = 'http://m2851085w2.wicp.vip/openid'
    a = {'redirect_uri': redirect_url}
    encode_url = parse.urlencode(a)
    # print("url:" + encode_url)
    # print("all_url:" + url+encode_url)
    return HttpResponseRedirect(url + encode_url)


def get_open_id(request):
    request_openid_url = 'https://agency.ucallclub.com/wechart/Access_token?code='
    # print("----openid-----" + request.GET['code'])
    code = request.GET['code']
    if code is None:
        return HttpResponse('请先获取code')
    if code == '':
        return HttpResponse('请先获取code')
    resp = requests.get(request_openid_url + code)
    if resp.status_code == 200:
        # 获取到openid
        openid = resp.json()['openid']
        request.session['openid'] = openid
        # print("openid:" + openid)
    # print("openid----------" + request.session['openid'])
    # return HttpResponse(resp.content)
    return render(request, 'index.html')


def get_openid_from_session(request):
    return HttpResponse(request.session['openid'])


def scan(request):
    url = 'http://sao315.com/w/api/saoyisao?'
    scan_redirect_url = 'http://m2851085w2.wicp.vip/scan_result'
    a = {'redirect_uri': scan_redirect_url}
    encode_url = parse.urlencode(a)
    return HttpResponseRedirect(url + encode_url)


def scan_result(request):
    print('scan_result:' + request.GET['qrresult'])





@csrf_exempt
def qr_code_info(request):
    response = {
        'status_code': 0,
        'data': {},
        'message': ''
    }
    if request.method == 'GET':
        qrcodeid = request.GET['qrcodeid']
        try:
            qrCode = QrCode.objects.filter(qr_code_id=qrcodeid)[0]
            q = QrCodeSerialize(qrCode)
            # phone_numbers = serializers.serialize('json',qrCode.get_phone_numbers())
            # oldManInfo = serializers.serialize('json',qrCode.old_man_info)
            response['status_code'] = 0
            response['data'] = q.data
            response['message'] = '获取信息成功'
            return JsonResponse(response)
        except Exception as e:
            print('获取绑定信息失败', e)
            response['status_code'] = -1
            response['data'] = None
            response['message'] = '未找到相应的绑定信息'
            return JsonResponse(response)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        # phoneNumberData={}
        # phoneNumberData['qr_code_id']=data['qr_code_id']
        # phoneNumberData['phone_number']=data['phone_number']
        #
        # try:
        #     qrCode = QrCode.objects.get(qr_code_id=data['qr_code_id'])
        #     qrCodeSerializer = QrCodeSerialize(qrCode,data)
        #     if qrCodeSerializer.is_valid():
        #         qrCodeSerializer.save()
        #         return JsonResponse(qrCodeSerializer.data)
        #     return JsonResponse(qrCodeSerializer.errors)
        # except QrCode.DoesNotExist:
        #     qrCodeSerializer = QrCodeSerialize(data=data)
        #     if qrCodeSerializer.is_valid():
        #         qrCodeSerializer.save()
        #         return JsonResponse(qrCodeSerializer.data)
        #     return JsonResponse(qrCodeSerializer.errors)

        qrcodeid = data['qr_code_id']
        old_man_info = data['old_man_info']
        phone_numbers = data['phone_number']
        print(qrcodeid, old_man_info, phone_numbers)
        try:
            qrCode = QrCode.objects.get(qr_code_id=qrcodeid)
            # 更新数据
            OldManInfo.objects.filter(pk=qrCode.old_man_info.pk)\
                .update(
                name=old_man_info['name'],
                address=old_man_info['address'],
                age=old_man_info['age'],
                medical_history=old_man_info['medical_history'],
                allergy=old_man_info['allergy'],
                blood_type=old_man_info['blood_type'],
                drugs=old_man_info['drugs'],
                treatment=old_man_info['treatment']
            )

            # o= OldManInfo.objects.filter(pk=qrCode.old_man_info.pk)
            # o.name = old_man_info['name'],
            # print('name:',old_man_info['name'])
            # o.address = old_man_info['address'],
            # o.age = old_man_info['age'],
            # o.medical_history = old_man_info['medical_history'],
            # o.allergy = old_man_info['allergy'],
            # o.blood_type = old_man_info['blood_type'],
            # o.drugs = old_man_info['drugs'],
            # o.treatment = old_man_info['treatment']
            # o.save()
            # print("更新数据", qrCode.old_man_info)
        except QrCode.DoesNotExist:
            # 创建数据
            try:
                # 创建OldManInfo对象,因为QrCode和OldManInfo是一对一的关系，所以不需要检测OldManInfo是否存在
                # oldManInfo = OldManInfo()
                # oldManInfo.name = old_man_info.name
                # oldManInfo.address = old_man_info.address
                # oldManInfo.age = old_man_info.age
                # oldManInfo.medical_history = old_man_info.medical_history
                # oldManInfo.allergy = old_man_info.allergy
                # oldManInfo.blood_type = old_man_info.blood_type
                # oldManInfo.drugs = old_man_info.drugs
                # oldManInfo.treatment = old_man_info.treatment
                # 创建QrCode对象
                oldManInfo = OldManInfo.objects.create(name=old_man_info['name'],
                                                       address=old_man_info['address'],
                                                       age=old_man_info['age'],
                                                       medical_history=old_man_info['medical_history'],
                                                       allergy=old_man_info['allergy'],
                                                       blood_type=old_man_info['blood_type'],
                                                       drugs=old_man_info['drugs'],
                                                       treatment=old_man_info['treatment'])
                qrCode = QrCode(qr_code_id=qrcodeid, old_man_info=oldManInfo)
                oldManInfo.save()
                qrCode.save()
            except Exception as e:
                print("创建QrCode失败：", e)
                response['status_code'] = -1
                response['message'] = '绑定信息失败'
                return JsonResponse(response)
        try:
            # 创建PhoneNumber对象
            # phoneNumbers = phone_numbers.split(',')
            # 对比数据库里的和传进来的电话号码，数据库里多余的要删除，参数里面有不一样的要添加
            oldNumbers = qrCode.get_phone_numbers()
            delete, add = utils.compareArrays(oldNumbers, phone_numbers)
            for d in delete:
                ct = ContentType.objects.get(model='qrcode')
                PhoneNumber.objects.get(phone_number=d, content_type=ct, object_id=qrCode.qr_code_id).delete()
            for a in add:
                ct = ContentType.objects.get(model='qrcode')
                PhoneNumber.objects.create(phone_number=a, content_type=ct, object_id=qrCode.qr_code_id)
            response['status_code'] = 0
            response['message'] = '保存信息成功'
            return JsonResponse(response)
        except Exception as e:
            print("创建PhoneNumber失败:", e)
            response['status_code'] = -1
            response['message'] = '保存信息失败'
            return JsonResponse(response)
