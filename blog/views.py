from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .form import PostForm
# Create your views here.
def post_list(request):
    qs=Post.objects.all()
    qs=qs.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request,'blog/post_list.html',{
        'post_lists':qs,
    })

# 동적 데이터를 뷰단에서 준비해서 템플릿에 넘기는 코드

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    # post  = Post.objects.get(pk=pk)  #프라이머리 키가 1인것을 가져오겠다.
    return render(request,'blog/post_detail.html',{
        'post': post,
    })


def post_new(request):
    if request.method =="POST":
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user # 인증된 유저만 받아온다. 인증된 유저가 아니면 오류가 발생
            post.published_date=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm()
    return render(request,'blog/post_edit.html',{'form':form,})

def post_edit(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method =="POST":
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user # 인증된 유저만 받아온다. 인증된 유저가 아니면 오류가 발생
            post.published_date=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm(instance=post)

    return render(request,'blog/post_edit.html',{'form':form,})