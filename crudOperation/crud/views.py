from django.shortcuts import render, redirect
from .models import crudOperation
# Create your views here.
def home(request):
    list=crudOperation.objects.all()

    return render(request, "crud/home.html", {'list':list})


def add(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        phone=request.POST.get('phone')

        obj = crudOperation()
        obj.name = name
        obj.address = address
        obj.email = email
        obj.phone = phone

        obj.save()
        return redirect("/crud/")
    return render(request, "crud/add.html")


def delete(request, id):
    delete = crudOperation.objects.get(pk=id)
    delete.delete()

    return redirect('/crud/')

def update(request, id):
    getData = crudOperation.objects.get(pk=id)
    return render(request, 'crud/update.html', {'data':getData})

def updateFunc(request, id):
    name=request.POST.get('name')
    address=request.POST.get('address')
    email=request.POST.get('email')
    phone=request.POST.get('phone')

    getData = crudOperation.objects.get(pk=id)
    getData.name = name
    getData.address = address
    getData.email = email
    getData.phone = phone

    getData.save()
    return redirect('/crud/')