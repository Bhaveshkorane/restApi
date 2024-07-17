from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [

    path('student/',views.studentAPI.as_view()),
    
    # path('',views.home,name='firstView_url'),
    # path('post_student',views.post_student,name='postStudent_url'),
    # path('update_student/<id>',views.update_student,name='updateStudent_url'),
    # path('delete_student/<id>',views.delete_student,name='deleteStudent_url'),
    path('viewBook',views.viewBook,name='viewBook_url')
]