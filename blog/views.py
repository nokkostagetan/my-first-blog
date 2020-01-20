from django.shortcuts import render
#models の前にあるドットは カレントディレクトリ 、もしくは カレントアプリケーション のことです。 views.pyと models.pyは、同じディレクトリに置いてあります。 だから、こんな風に.とファイル名だけを使って、簡単に記述することが出来る
from .models import Post
from django.utils import timezone
# Create your views here.
def post_list(request):
    posts = Post.objects.published().order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts': posts})
