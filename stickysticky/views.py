from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.


def index(request):
	a = Sticky.objects.all()

	b = Sticky2.objects.all()

	# StickyStickyForm is the class created under forms.py
	form = StickyStickyForm()

	if request.method =='POST' and 'Create StickBombs2' in request.POST:
		form = StickyStickyForm2(request.POST)
		if form.is_valid():
			form.save()
	if request.method =='POST' and 'Create StickBombs' in request.POST:
		form = StickyStickyForm(request.POST)
		if form.is_valid():
			form.save()

		return redirect('/')
	context = {'stickys':a, 'sticky2s':b, 'form': form}
	return render(request, 'stickysticky/list.html', context)


def updateSticky(request, pk):
	# pk is primary key
	b = Sticky.objects.get(id=pk)

	form = StickyStickyForm(instance=b)

	if request.method =='POST':
		form = StickyStickyForm(request.POST, instance=b)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'stickysticky/update_sticky.html', context)


def deleteSticky(request, pk):
	item = Sticky.objects.get(id=pk)

	if request.method =='POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'stickysticky/delete.html', context)







def index2(request):
	a = Sticky2.objects.all()

	# StickyStickyForm is the class created under forms.py
	form = StickyStickyForm2()

	if request.method =='POST':
		form = StickyStickyForm2(request.POST)
		if form.is_valid():
			form.save()

		return redirect('/')
	context = {'sticky2s':a, 'form': form}
	return render(request, 'stickysticky/list.html', context)


def updateSticky2(request, pk):
	# pk is primary key
	b = Sticky2.objects.get(id=pk)

	form = StickyStickyForm2(instance=b)

	if request.method =='POST':
		form = StickyStickyForm2(request.POST, instance=b)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'stickysticky/update_sticky2.html', context)


def deleteSticky2(request, pk):
	item = Sticky2.objects.get(id=pk)

	if request.method =='POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'stickysticky/delete2.html', context)