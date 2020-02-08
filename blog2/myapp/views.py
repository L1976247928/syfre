from . import models
#from django.http import HttpResponse
#from django.Http import HttpResponseRedirect
from django.shortcuts import render,redirect




def Start(request):
    post_obj = models.Post.objects.all()
    return render(request,'index.html',{'nickname':"游客",
                                        'post_obj':post_obj
                                        })

#登陆
def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    if request.method == "POST":
        nickname = request.POST.get("nickname")
        password = request.POST.get("password")
        message = '账号或密码错误，或者已经登陆'
        use_obj = models.User.objects.filter(username = nickname,userpasswd = password)
        if use_obj and request.session.get("nickname") != nickname:
            #存储session
            request.session["nickname"] = nickname
            #设置session的过期时间
            request.session.set_expiry(10)
            list = []
            for i in use_obj:
                list.append(i.username)
            request.session["nickname"] = list[0]
            post_obj = models.Post.objects.all()
            return render(request,"index.html",{"message1":list[0],
                                                'post_obj':post_obj,
                                                "nickname":nickname,

                                                })
        else:
            return render(request,"index.html",{"message":message,})

#注册
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    if request.method == "POST":
        nickname = request.POST.get("nickname")
        passwd = request.POST.get("passwd")
        repasswd = request.POST.get("repasswd")
        email = request.POST.get("email")
        nick_obj = models.User.objects.filter(username = nickname)
        message1 = "昵称已经存在,请重新输入!"
        message2 = "密码为空,请输入!"
        message3 = "邮箱为空,请输入!"
        message4 = "两次密码不同!"
        if nick_obj:
            return render(request,"register.html",{"message":message1})
        elif passwd == None:
            return render(request,"register.html",{"message":message2})
        elif email == None:
            return render(request,"register.html",{"message":message3})
        elif passwd != repasswd:
            return render(request,"register.html",{"message":message4})
        else:
            post_obj = models.Post.objects.all()
            models.User.objects.create(username = nickname,userpasswd = passwd)
            return render(request,"index.html",{"post_obj":post_obj,
                                                "nickname":nickname,
                                                })


def clear(request,post_id):
    post_obj = models.Post.objects.filter(pk = post_id)
    remark = models.Remark.objects.filter(posttitle_id = post_id)
    return render(request,"clear.html",{'post_obj':post_obj,
                                        'remark':remark,
                                        })





















