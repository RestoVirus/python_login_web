from django.contrib.auth.models import User
from main_web.apps.accounts.forms import customerInputForm
from django import template
from django.http import request, response
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from .models import Customer
from .forms import customerInputForm, employeeInputForm, employeeEditForm


register = template.Library()

# ------------------------------------------------------------------------------------    CUSTOMER VIEW
@login_required
def CustomerView(request):
    #DELETE
    if request.GET.get('delete-id') :
        Customer.objects.filter(pk= request.GET.get('delete-id')).delete()
        customersObject = Customer.objects.all()
        context = {
            'customersObjects': customersObject,
        }
        return render(request,'accounts/customers.html', context)
    
        
    customersObject = Customer.objects.all()
    context = {
        'customersObjects': customersObject,

    }
    return render(request,'accounts/customers.html', context)



# ------------------------------------------------------------------------------------    CUSTOMER EDIT
@login_required
def costumerViewEdit(request, pk):   
    postobj= get_object_or_404(Customer,pk=pk)

    if request.method == 'POST':
        form = customerInputForm(request.POST or None, instance=postobj)
        if form.is_valid():
            form.save()
        return response.HttpResponseRedirect('/accounts/customers')
    else:    
        e = Customer.objects.get(pk=int(pk))
        form = customerInputForm(instance=e)
        print(form)
    return render(request, 'accounts/customersEdit.html',{'form':form, 'pk':pk})    

# ------------------------------------------------------------------------------------    CUSTOMER ADD
@login_required
def customerViewAdd(request): 
    if request.method == 'POST':
        form = customerInputForm(request.POST)
        if form.is_valid():
            form.save()
        return response.HttpResponseRedirect('customers')
    else:
        form = customerInputForm()
    
    return render(request, 'accounts/customersAdd.html',{'form':form})
        

# ------------------------------------------------------------------------------------    EMPLOYEE VIEW
@user_passes_test(lambda u: u.is_superuser)
def employeeView(request):
    #DELETE
    if request.GET.get('delete-id') :
        User.objects.filter(pk= request.GET.get('delete-id')).delete()

        EmployeeObject = User.objects.all()
        context = {
            'EmployeeObject': EmployeeObject,
        }
        return render(request,'accounts/employee.html', context)
   
        
    EmployeeObject = User.objects.all()
    context = {
        'EmployeeObject': EmployeeObject,
    }   
    return render(request,'accounts/employee.html', context)

# ------------------------------------------------------------------------------------    EMPLOYEE ADD
@user_passes_test(lambda u: u.is_superuser)
def employeeViewAdd(request): 
    if request.method == 'POST':
        form = employeeInputForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            user.set_password(user.password)
            form.save()
            return response.HttpResponseRedirect('employee')
        else:
            print(form.errors)
        #return response.HttpResponseRedirect('employee')
    else:
        form = employeeInputForm()
    
    return render(request, 'accounts/employeeAdd.html',{'form':form})


    # ------------------------------------------------------------------------------------    EMPLOYEE EDIT
@user_passes_test(lambda u: u.is_superuser)
def employeeViewEdit(request, pk):   
    postobj= get_object_or_404(User,pk=pk)
    print("*************************************************")
    if request.method == 'POST':
        form = employeeEditForm(request.POST or None, instance=postobj)
        if form.is_valid():
            user = form.save(commit=False)            
            user.set_password(user.password)
            form.save()
            print("-------------------------------------------------------------------------------------------------------------")
            return response.HttpResponseRedirect('/accounts/employee')
        else:
            print(form.errors)
    else:    
        e = User.objects.get(pk=int(pk))
        form = employeeEditForm(instance=e)
        print(form)
    return render(request, 'accounts/employeeEdit.html',{'form':form, 'pk':pk})    