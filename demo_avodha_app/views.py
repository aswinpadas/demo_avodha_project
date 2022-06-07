from django.http import HttpResponse
from django.shortcuts import render
from . models import shop
# Create your views here.
def demo(req):
    obj_product=shop.objects.all()

    return  render(req,'home.html',{'products':obj_product})
def details(req,product_id):
    product1=shop.objects.get(id=product_id)
    return render(req,'details.html',{'product':product1})