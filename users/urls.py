from django.urls import path
from .views import userlistview, usercreateview, userupdateview, userdeleteview, location_view, signin, signout

app_name = 'users'

urlpatterns = [
    path('', userlistview.as_view(), name='user_list'),
    path('create/', usercreateview.as_view(), name='user_create'),
    path('update/<int:pk>/', userupdateview.as_view(), name='user_update'),
    path('delete/<int:pk>/', userdeleteview.as_view(), name='user_delete'),
    path('location/', location_view, name='location'),  # URL para la página de ubicación
    path('login/', signin, name='login'),  # URL para la página de inicio de sesión
    path('signout/', signout, name='signout'),  # URL para la página de cierre de sesión
  
]