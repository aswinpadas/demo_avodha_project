from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import shop
from . forms import ModelForm
# Create your views here.
def demo(req):
    obj_product=shop.objects.all()

    return  render(req,'home.html',{'products':obj_product})
def details(req,product_id):
    product1=shop.objects.get(id=product_id)
    return render(req,'details.html',{'product':product1})
def add_product(req):
    if req.method=='POST':
        product_name=req.POST.get('product_name')
        product_desc=req.POST.get('product_desc')
        product_price=req.POST.get('product_price')
        product_img=req.FILES['product_img']
        obj_shop=shop(name=product_name,desc=product_desc,price=product_price,img=product_img)
        obj_shop.save()
    return render(req,"add_product.html")
def update_product(req,id):
    obj_shop=shop.objects.get(id=id)
    form=ModelForm(req.POST or None,req.FILES,instance=obj_shop)
    if form.is_valid():
        form.save()
        return redirect('/')
    return  render(req,"product_edit.html",{'form':form,'obj_shop':obj_shop})
def delete_product(req,id):
    if req.method=='POST':
        obj_shop=shop.objects.get(id=id)
        obj_shop.delete()
        return redirect('/')
    return render(req,"product_delete.html")

