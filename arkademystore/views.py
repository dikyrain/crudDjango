from django.shortcuts import render, redirect  
from .forms import ArkademyStoreForm  
from .models import ArkademyStore  


    # Create your views here.  


def inputProduk(request):  
    if request.method == "POST":  
        form = ArkademyStoreForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ArkademyStoreForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    arkademystores = ArkademyStore.objects.all()  
    return render(request,"show.html",{'arkademystores':arkademystores})  
def edit(request, id):  
    arkademystore = ArkademyStore.objects.get(id=id)  
    return render(request,'edit.html', {'arkademystore':arkademystore})  
def update(request, id):  
    arkademystore = ArkademyStore.objects.get(id=id)  
    form = ArkademyStoreForm(request.POST, instance = arkademystore)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'arkademystore': arkademystore})  
def destroy(request, id):  
    arkademystore = ArkademyStore.objects.get(id=id)  
    arkademystore.delete()  
    return redirect("/show")  