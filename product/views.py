from django.shortcuts import render

# Create your views here.
def shop(request):
    return render(request,'product/shop.html')
def accessories(request,slug):
    return render(request,'product/accessories.html')
def apparel(request):
    return render(request,'product/apparel.html')
def perfume(request):
    return render(request,'product/perfume.html')
def shoes(request):
    return render(request,'product/shoes.html')