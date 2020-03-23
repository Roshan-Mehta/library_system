from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from blog.forms import RegistrationForm
from django.contrib.auth.models import User

def home(request):
	numbers=[1,2,3,4,5]
	name='Max Goodridge'

	args={'myName':name,'numbers':numbers}
	return render(request,'blog/home.html',args)


def register(request):
	if request.method=='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else :
		form=RegistrationForm()

	args={'form':form}
	return render(request,'blog/reg_form.html',args)

def profile(request):
	args={'user':request.user}
	return render(request,'blog/profile.html',args)

def search(request):
	args={'user': request.method}
	for k,v in request.POST.items():
		print("Key: ", k)
		print("Value: ", v)
		search_results = {'first': [1,2,3], 'second':['a','b','c']}
		context = {
		'search_results' : search_results
		}
	# print(args)
	return render(request,'blog/search.html',context)
