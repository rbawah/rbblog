from django.urls import path, reverse_lazy
from django.conf.urls import url
from . import views
from blog.models import Post, Topic
from blog.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


app_name='blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='all'),

    path('post/create',
        OwnerCreateView.as_view(
            success_url=reverse_lazy(app_name+':all'),
            model = Post,
            template_name = app_name+"/form.html",
            fields = ['title', 'preview_image', 'text']
         ), name='post_create'),

    path('post/<slug:slug>/',
         OwnerDetailView.as_view(
             model= Post,
             template_name=app_name + "/detail.html"),
         name='post-detail'),

    path('post/<slug:slug>/update',
        OwnerUpdateView.as_view(
            success_url=reverse_lazy(app_name+':all'),
            model = Post,
            fields = ['title', 'slug', 'preview_image', 'text'],
            template_name = app_name+"/form.html"
        ), name='post_update'),

    path('post/<slug:slug>/delete',
        OwnerDeleteView.as_view(
            success_url=reverse_lazy(app_name+':all'),
            model = Post,
            template_name = app_name+"/delete.html"
        ), name='post_delete'),



]



urlpatterns += [
    #path('topics/', views.get_topic, name='topic-list'),

    path('<slug:slug>/topic', views.get_posts_by_topic, name='topic-articles'),
    path('<slug:slug>/category', views.get_posts_by_category, name='category-posts'),
    #path('<slug:slug>/tutorial', views.get_tuts_posts, name='tuts-posts'),
    path('<slug:slug>/tutorial', views.TutsListView.as_view(), name='tuts-posts'),
    #path('topics/', views.TopicListView.as_view(), name='topic-list'),


]
