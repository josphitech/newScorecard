from evaluation.decorators import unauthenticated_user
from django.forms.forms import Form
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
# from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, SupervisorCharacteristics
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .decorators import *
from django.contrib.auth.models import Group

@login_required(login_url=('login'))
# @admin_only
@allowed_users(allowed_roles="coordinators")
def dashboard(request):
    students = Student.objects.all()
    supervisors = Supervisor.objects.all()
    coordinators = Coordinator.objects.all()
    no_students = students.count()
    no_of_supervisors = supervisors.count()
    no_of_coordinators = coordinators.count()
    content = {'students':students, 'supervisors':supervisors, 'coordinators': coordinators, 'n_students':no_students, 'n_supervisors': no_of_supervisors, 'n_coordinators':no_of_coordinators}
    
    return render(request, 'all_templates/dashboard.html', content)

@unauthenticated_user
def loginPage(request):
        if request.method == 'POST':
            username =request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username= username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')
            
        context = {}
        return render(request, 'all_templates/registration/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')
   
@unauthenticated_user
def registerPage(request): 
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method =='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user =  form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get( name = "students")
                user.groups.add(group)
                messages.success(request, 'Account was created for ' + username)
                return redirect('login')
        context = {'form': form}
        return render(request, 'all_templates/registration/signup.html', context)

def studentsPage(request):
    supervisors = Supervisor.objects.all()

    context = {'supervisors': supervisors}
    return render(request, 'all_templates/students.html', context)

def supervisor(request,my_id):
    supervisor = Supervisor.objects.filter(id=my_id)
    mform = SupervisorCharacteristicsForm()
    sform = StudentCharacteristicsForm()
    if request.method == 'POST' and 'supervisorC' in request.POST:
        mform = SupervisorCharacteristicsForm(request.POST)
        if mform.is_valid():
            instance = mform.save(commit=False)
            instance.save()
            print('Successful')
            return HttpResponseRedirect('/supervisors?submitted=True')
 
        else:
            print("Failed!!")
            return HttpResponseRedirect('/supervisors?submitted=False')

    if request.method == 'POST' and 'studentC' in request.POST:
        sform = StudentCharacteristicsForm(request.POST)
        if sform.is_valid():
            instance = sform.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/supervisors?submitted=Truee')
            print('Successful')
        else:
            print("Failed!!")
            return HttpResponseRedirect('/supervisors?submitted=False')
            
    context = {'supervisors': supervisor,'mform':mform, 'sform':sform}
    return render(request, 'all_templates/supervisors.html', context)

def secondForm(request):

    sform = StudentCharacteristicsForm()
    if request.method == 'POST':
        sform = StudentCharacteristicsForm(request.POST)
        if sform.is_valid():
            instance = sform.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/supervisors?submitted=Truee')
            print('Successful')
        else:
            print("Failed!!")
            return HttpResponseRedirect('/supervisors?submitted=False')
    context = {'sform':sform}
    return render(request, 'all_templates/supervisors.html', context)


def rating(request,my_id):
    supervisor = Supervisor.objects.filter(id=my_id)
    supervisorcharacteristics = SupervisorCharacteristics.objects.all()
    studentcharacteristics = StudentCharacteristics.objects.all()
    number_of_rates = supervisorcharacteristics.count()
    context = {'supervisors': supervisor, 'supervisorcharacteristics': supervisorcharacteristics, 'studentcharacteristics':studentcharacteristics, 'number_of_rates':number_of_rates}
    return render(request, 'all_templates/ratings.html', context)

def codRating(request,my_id):
    supervisor = Supervisor.objects.filter(id=my_id)
    codrating = CoordinatorRateLearning.objects.all() 
    number_of_rates = codrating.count()     
    codrating2 = CoordinatorRateSupervisor.objects.all()
    context = {'supervisors': supervisor, 'codrating':codrating,"codrating2":codrating2, 'number_of_rates':number_of_rates}
    return render(request, 'all_templates/codRating.html', context)



def coordinatorRating(request,my_id):
    supervisor = Supervisor.objects.filter(id= my_id)
    form = CoordinatorRating()
    mform = CoordinatorRateSupervisorForm()
    if request.method == 'POST' and 'learning' in request.POST:
        form = CoordinatorRating(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            print('Successful')
            return HttpResponseRedirect('/supervisors?submitted=Truee')
            
        else:
            print("Failed!!")
            return HttpResponseRedirect('/supervisors?submitted=False')
    if request.method == 'POST' and 'coordinatorR' in request.POST:
        mform = CoordinatorRateSupervisorForm(request.POST)
        if mform.is_valid():
            instance = mform.save(commit=False)
            instance.save()
            print('Successful')
            return HttpResponseRedirect('/supervisors?submitted=True')
            
        else:
            print("Failed!!")
            return HttpResponseRedirect('/supervisors?submitted=False')


    context = {'form':form, 'supervisors': supervisor, 'mform':mform, 'supervisor':supervisor}
    return render(request, 'all_templates/coordinators.html', context)
        



def contact(request, my_id):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            print('successful')
            # assert False
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    supervisor = Supervisor.objects.filter(id=my_id)
   
    return render(request, 'all_templates/contacts.html')