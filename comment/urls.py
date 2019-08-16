from . import views
from django.urls import path

urlpatterns = [

    path('', views.CommentList.as_view(), name='home'),
    path('<int:pk>/', views.info_comment, name='info_comment'),
    path('comment/', views.add_comment, name='add_comment_to_post'),



]
