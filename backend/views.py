from django.shortcuts import render
import requests
from django.http import *
from urllib import parse


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
