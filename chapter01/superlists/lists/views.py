from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item,List

# Create your views here.
#home_page =None
def home_page(request):
    return render(request,'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request,'list.html',{'items':items})

def new_list(request):
        list_=List.objects.create()
        #new_item_text = request.POST.get('item_text','')
        #new_item_text = request.POST['item_text']
        #Item.objects.create(text=new_item_text)
        Item.objects.create(text=request.POST['item_text'],list=list_)
        return redirect('/lists/the-only-list-in-the-world/')