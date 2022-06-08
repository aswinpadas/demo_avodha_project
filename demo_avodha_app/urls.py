from django.urls import path
from  demo_avodha_app import views

urlpatterns = [
    path('',views.demo,name='demo'),
    path('shop/<int:product_id>',views.details,name='details'),
    path('add/',views.add_product,name='add_product'),
    path('update/<int:id>',views.update_product,name='update_product'),
    path('delete/<int:id>',views.delete_product,name='delete_product')
    ]