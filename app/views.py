from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Abonent, News
from django.db.models import Q
from django.contrib import messages


def base(request):
    news = News.objects.all()
    context = {
        "post":news
    }
    return render(request, "Mega/index.html", context)

# Create your views here.
def number(request):
    if request.method == "POST":
        if 'search_button' in request.POST:
            print('Search button')
            searched = request.POST['search']
            print(searched)
            try:
                abonent = Abonent.objects.get(Q(number__icontains=searched))
                print(abonent)
            except:
                messages.error(request, 'Абонент не найдено!')
                print("Абонент не найдено!")        
            context = {
                "abonent": abonent,
            }
            return render(request, "Mega/younumber.html", context=context)
        elif 'delete_button' in request.POST:
            print('Delete button')
            try:
                abonent = Abonent.objects.get(number=request.POST['search'])
                abonent.delete()
                messages.info(request, 'Абонент успешно удалено!')
                print('Абонент успешно удалено!')
                return redirect('number')
            except:
                messages.error(request, 'Абонент не найдено!')
                print('Абонент не найдено!')
                return redirect('number')
    else:
        return render(request, "Mega/younumber.html")
 
    

def tarif(request):
    return render(request, "Mega/tarif.html")

def kyzmat(request):
    return render(request, "Mega/uslugi.html")


def about(request):
    return render(request, "Mega/onas.html")