from django.conf.urls import url
from . import views

urlpatterns=[
 url(r'^$',views.post_list,name="post_list"),
 url(r'^post/(?P<pk>\d+)/$',views.post_detail,name="post_detail"), #pk변수에 모든 값을 넣어 뷰로 전송하겠다는 뜻입니다.
 url(r'^post/new/$',views.post_new,name='post_new'),
 url(r'^post/(?P<pk>\d+)/edit/$',views.post_edit,name="post_edit"),
]

