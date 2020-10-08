from django.shortcuts import render,HttpResponse,redirect
import random

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter']=0
    return render(request,"index.html")

def process_gold(request):
    #logic: do something...find gold
    print(request.POST['which_gold'])
    if request.POST['which_gold'] == 'farm':
        request.session['which_gold']=request.POST['which_gold']
        gold_won = random.randint(10,20)
        request.session['counter'] += gold_won       
        request.session['activities'] = f'you WON {gold_won}'
        
    if request.POST['which_gold'] == 'cave':  
        request.session['which_gold']=request.POST['which_gold']
        gold_won = random.randint(5,10)
        request.session['counter'] += gold_won
        request.session['activities'] = f'YAYAYAYYAYAYAYAYYA {gold_won}'

    if request.POST['which_gold'] == 'house':  
        request.session['which_gold']=request.POST['which_gold']
        gold_won = random.randint(2,5)
        request.session['counter'] += gold_won
        request.session['activities'] = f'better then nothing {gold_won}'

    if request.POST['which_gold'] == 'casino':
        request.session['which_gold']=request.POST['which_gold']
        gold_won = random.randint(0,50)  
        request.session['counter'] += gold_won
        request.session['activities'] = f'WAY TO GOOOOO!!!{gold_won}'            
        #add the random number to my session variable
    return redirect("/") 

def recet(request):
    request.session.flush()
    return redirect('/')