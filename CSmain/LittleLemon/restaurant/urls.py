#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/',views.MenuModelView.as_view()),
    path('menu/<int:pk>',views.SingleMenuModelView.as_view()),
    path('tables/',views.BookingModelView.as_view({'get':'list','post':'create'})),
    path('api-token-auth/',obtain_auth_token),


]
