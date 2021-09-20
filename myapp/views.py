from django.shortcuts import render
from .models import *
from .forms import *

from django.contrib import messages

# Create your views here.

def home(request):
	return render(request, "index.html")

def view(request):
	l = Users.objects.all()
	return render(request, "customers.html", {'users': l})

def transfer(request):
	l = Users.objects.all()
	if request.method=='POST':
		if(not 'name1' in request.POST):
			messages.error(request,"Select sender")
			return render(request,"transfer.html",{'users':l})
		sender = request.POST['name1']

		if(not 'name2' in request.POST):
			messages.error(request,"Select receiver")
			return render(request,"transfer.html",{'users':l})
		receiver = request.POST['name2']

		amount = request.POST['amount']
		if(sender==receiver):
			messages.error(request,"Sender & receiver can't be same")
			return render(request,"transfer.html",{'users':l})
		elif not amount.isdigit():
			messages.error(request,"Enter valid amount")
			return render(request,"transfer.html",{'users':l})
		else:
			amount = int(amount)
			for i in l:
				if i.name == sender:
					if i.balance<amount:
						messages.error(request,"Not suffieicent balance")
						return render(request,"transfer.html",{'users': l})
					i.balance -= amount
					i.save()
				elif(i.name== receiver):
					i.balance+=amount
					i.save()
			d = data(request.POST)
			d.save()
		return render(request,"index.html")
	else:
		return render(request,"transfer.html",{'users':l})


def tran(request):
	t = transactions.objects.all()
	return render(request, "transactions.html",{'transactions': t})