from django.urls import path,r_path
from blog import views

urlpatterns =[
    path(' ',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    r_path(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    r_path(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
    r_path(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
    r_path(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
    r_path(r'^drafts/$',views.DraftListView.as_view(),name='post_draft_list'),
    r_path(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    r_path(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    r_path(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    r_path(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),
]
