from django.http import HttpResponse
from django.shortcuts import render
from money.models import Transaction

def index(request):
	context = {}
	return render(request, 'money/index.html', context) 

def all(request):
	transaction_list = Transaction.objects.all();
	context={'transaction_list' : transaction_list}
	return render(request, 'money/all.html', context)

