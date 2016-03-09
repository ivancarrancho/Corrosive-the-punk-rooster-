from django.shortcuts import render, redirect
from User.forms import ExpensesForm

def create_data(request):
    if request.method == 'POST':
        myForm = ExpensesForm(request.POST)
        if myForm.is_valid():
            return redirect('/home')
    else:
        myForm = ExpensesForm()
    return render(request, 'create_data.html', {'myForm': myForm})
