import json
from django.shortcuts import render
from customer.controller import *

# Create your views here.
def index(request):
    context = {}
    context['categoryes'] = get_categoryes()
    return render(request,'index.html', context)

def faq(request):
    context = {}
    print(json(request))
    # context['categoryes'] = get_categoryes_by_name(request)
    # for i in context['categoryes']:
    #     pass
    return render(request,'faq.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')