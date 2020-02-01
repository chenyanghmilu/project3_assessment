from django.shortcuts import render, redirect
from .forms import WidgetForm
from .models import Widget
from django.db.models import Sum

def home(request):
    if request.method == "POST":
        form = WidgetForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        return render(request, 'index.html', {
            "widget_list": Widget.objects.all(),
            "form": WidgetForm(),
            "total": Widget.objects.all().aggregate(Sum('quantity'))['quantity__sum']
        })

def delete(request, pk):
    Widget.objects.get(pk=pk).delete()
    return redirect("home")