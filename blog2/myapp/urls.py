from django.urls import path
from . import views
urlpatterns = [
    path('',views.Start),
    path('login/',views.login ),
    path('register/',views.register),
    path("clear/<int:post_id>",views.clear),
    #path('resave/<int:post_id>',views.resave),
    #path('comment/post/', views.comment_post, name='comment_post'),

]
