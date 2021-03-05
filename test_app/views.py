from django.shortcuts import render, redirect
from .models import botwTest
from .forms import botwTestForm
from django.shortcuts import get_object_or_404

def home_view(request):
    data = botwTest.objects.all()
    context={
        'data': data,
    }
    return render(request,'home.html', context)


def edit_view(request, pk):
    context = {}
    data = get_object_or_404(botwTest, pk = pk)
    form = botwTestForm(request.POST or None, instance = data)
    if form.is_valid(): 
        form.save()
        return redirect('home')
    context = {
        # 'form': form,
        'data': data,
    }
    return render(request,'form.html', context)


def preview_view(request, pk):
    data = botwTest.objects.get(pk=pk)
    context = {
        'data': data,
    }
    return render(request,'output.html', context)


def form_view(request):
    form = botwTestForm(request.POST)
    context = {}
    # def store_results(everything):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    # store_results(form)

    newsletter_campaign_id = request.POST.get('newsletter_campaign_id')

    context["output"] = newsletter_campaign_id



            
    
    return render(request, 'form.html', context)



