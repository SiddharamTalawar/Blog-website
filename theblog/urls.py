#from django.contrib import admin
from django.urls import path,include

from .views import commentview, homeview,artical_detailview,add_postview,upadte_post_view,delete_post_view,UserRegisterView,LikeView,commentview,edit_user_settings,Password_change_view,Create_ProfilePage_View,Show_ProfilePage_View,upadte_profile_view,categoryview

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',homeview.as_view() , name='home'),
    path('artical/<int:pk>',artical_detailview.as_view(),name='detail_view'),
    path('delete/<int:pk>',delete_post_view.as_view(),name='delete_post'),
    path('add_post/',add_postview.as_view(), name='add_post'),
    path('artical/edit/<int:pk>',upadte_post_view.as_view(),name='update_post'),
    path('like/likes/<int:pk>/', LikeView, name='like_post'),
    path('comment/<int:pk>',commentview.as_view(), name='add_comment'),
    path('edit_settings',edit_user_settings.as_view(),name='user_settings'),
    path('password/',Password_change_view.as_view(),name='password_change'),
    path('create_profile',Create_ProfilePage_View.as_view(),name='create_profile'),
    path('user_profile/<int:pk>',Show_ProfilePage_View.as_view(),name='user_profile'),
    path('edit_profile/<int:pk>',upadte_profile_view.as_view(),name='edit_profile'),
    path('categorylist/<str:cat>',categoryview,name='category_sort'),
    path('registrations',UserRegisterView.as_view(),name='register')

]