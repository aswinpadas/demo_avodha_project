from django.urls import path
from  demo_avodha_app import views

urlpatterns = [
    path('',views.demo,name='demo'),
    path('shop/<int:product_id>',views.details,name='details')
    ]