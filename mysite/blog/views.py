from django.shortcuts import render
from django.http import HttpResponse,request
from .models import Post,PostTeste
from django.utils import timezone

# Create your views here.
def index(request):
    return HttpResponse("TESTANDO INDEX")


def post_list0(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
     p = Post.objects.all()
     return render(request,'blog/post_list0.html',{'posts': p})
    # return render(request,'blog/post_list0.html')

def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request,'blog/post_list.html',{'posts': posts})

def post_list2(request,id):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print("valor do id  = %s"%id)
    posts = Post.objects.all()

    return render(request,'blog/post_list2.html',{'posts': posts, 'id': id})

def post_list00(request,id1):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print("valor do id  = %s"%id1)
    try:
        #p=Post.objects.get(id=id1)
        #print("em p o valor do title=",p.title)
        posts=Post.objects.get(id=id1)
        #p=PostTeste()
        #if id1 == '1':
        #    p = PostTeste("o pequeno principe de id 1 TESTE","o autor","dasdlasdjasdlkas dlasjdlaskdjaslkdj asada")
       #else:
       #    p=PostTeste()
       # posts = Post.objects.all()

        return render(request,'blog/post_list00.html',{'p': posts})
       # p1=0
        #return render(request,'blog/post_list00.html',{'p': p,'p1':p1})

    except:
        p=PostTeste("Id não cadastrado!!!")

        return render(request,'blog/post_list00.html',{'p': p})


def amanda(request):
    return render(request,'blog/amanda.html')

