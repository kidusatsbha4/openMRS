from django.urls import path
from . import views
urlpatterns=[
    path('show/',views.show,name='show'),
    path('show/delete/<int:id>/',views.delete,name='delete'),
    path('show/update/<int:id>/',views.update,name='update'),
    path('show/update/<int:id>/up',views.up,name='up'),
    path('members/',views.members,name='members'),
    path('',views.register,name='register'),

]