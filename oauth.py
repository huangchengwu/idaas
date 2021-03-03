from django.shortcuts import render,HttpResponse,redirect
import  requests
import json
def login(request):
    return render(request, "login.html")
def get_token(code):
    """
    获取access_token
    """
    params = {
        "client_id": "8db7c89f6089d8bae28b4b31fe01fe7cYtiiGht860N",
        "client_secret": "teMYkZUfL9s9OI5Q4iVav2STHHI9rhZ99hOEdRiXAM",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://172.16.0.222:9090/process"
    }
    print ("获取access_token",params)

    
    result = requests.post(url="https://cmyarmwqex.login.aliyunidaas.com/oauth/token", data=params)
    return result

def get_user_info(result):
    """
    获取用户信息
    """
    print ("获取用户信息")
    get_user_url = "https://cmyarmwqex.login.aliyunidaas.com/api/bff/v1.2/oauth2/userinfo"
    access_token = result["access_token"]
    user_info = requests.get(url=get_user_url, params={"access_token": access_token})
    print (user_info.text,user_info.status_code)
    return user_info
def process(request):
    print ("解析用户信息")

    code = request.GET.get("code")
    result = get_token(code) 
    result = result.json()  
    user_info = get_user_info(result).json()
    return redirect("/index")


def index(request):
    return render(request, "index.html")

