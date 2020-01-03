from django.shortcuts import render
import requests
from django.http import *
from urllib import parse


# Create your views here.
def index(request):
    get_code(request)
    return render(request, 'index.html')


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
    print("----openid-----" + request.GET['code'])
    code = request.GET['code']
    if code == '':
        return HttpResponseForbidden('请先获取code')
    resp = requests.get(request_openid_url + code)
    if resp.status_code == 200:
        # 获取到openid
        openid = resp.json()['openid']
        print("openid:" + openid)
    return HttpResponse(resp.content)
