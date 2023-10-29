from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Post
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())

def showpost(request,slug):#request浏览器向服务器发送的请求对象，包含用户信息、请求内容和请求方式等
    post = Post.objects.get(slug=slug)#是從數據庫取得一個匹配的結果 返回一個對象 如果紀錄不存在的話 會回復錯誤
    if post!= None:
        return render(request,'post.html',locals())#前兩個是必要的
    else:
        return redirect("/")
    return redirect("/")#redirect轉網址