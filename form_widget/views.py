from django.shortcuts import render
from .forms import Widget_form
from .models import Widget_model
from django.http import HttpResponseRedirect

# Create your views here.
def demo(request):
	print(request.POST)
	if request.method == 'POST':
		form = Widget_form(request.POST)

		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			class1 = form.cleaned_data['class1']
			phone = form.cleaned_data['phone']
			category = form.cleaned_data['category']
			address = form.cleaned_data['address']

			e = Widget_model(name=name,email=email,class1=class1,phone=phone,category=category,address=address)
			e.save()
			return HttpResponseRedirect('/show/')

			# data = Widget_model.objects.all()
			# details = list(data)

			# return render(request,'show.html',{'details':details})

	
	form = Widget_form()

	return render(request,'form.html',{'form':form})


def show(request):
	data = Widget_model.objects.all()
	details = list(data)

	return render(request,'show.html',{'details':details})


def delete(request,id):
	dele = Widget_model.objects.get(id=id).delete()
	return HttpResponseRedirect('/show/')

def edit(request, id):
	edit =  Widget_model.objects.get(id=id)
	

	if request.method == 'POST':
		form = Widget_form(request.POST)

		if form.is_valid():
			edit.name = form.cleaned_data['name']
			edit.email = form.cleaned_data['email']
			edit.class1 = form.cleaned_data['class1']
			edit.phone = form.cleaned_data['phone']
			edit.category = form.cleaned_data['category']
			edit.address = form.cleaned_data['address']
			edit.save()
			return HttpResponseRedirect('/show/')

	else:
		data = {'name':edit.name,'email':edit.email,'class1':edit.class1,'phone':edit.phone,'category':edit.category,
		'address':edit.address}
		form = Widget_form(initial=data)
		form.id = edit.id

	return render(request,'edit.html',{'form':form})
			

