from django.http.response import FileResponse
from evaluation.models import Supervisor
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SupervisorCharacteristicsForm(ModelForm):
    class Meta:
        model = SupervisorCharacteristics
        fields = ['superOne', 'superTwo', 'superThree', 'superFour', 'supervisor']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.marks = instance.superOne + instance.superTwo + instance.superThree + instance.superFour
        if commit:
            instance.save()
        return instance
        
        

class StudentCharacteristicsForm(ModelForm):
    class Meta:
        model = StudentCharacteristics
        fields = ['studentOne', 'studentTwo', 'studentThree', 'studentFour', 'supervisor']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.marks = instance.studentOne + instance.studentTwo + instance.studentThree + instance.studentFour
        if commit:
            instance.save()
        return instance

class CoordinatorRating(ModelForm):
    class Meta:
        model = CoordinatorRateLearning
        fields = ['learningOne', 'learningTwo','supervisor']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.marks = instance.learningOne + instance.learningTwo
        if commit:
            instance.save()
        return instance

class CoordinatorRateSupervisorForm(ModelForm):
    class Meta:
        model = CoordinatorRateSupervisor
        fields = ['superCoorOne', 'supervisor']
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.marks = instance.superCoorOne 
        if commit:
            instance.save()
        return instance
        
class ContactForm(ModelForm):
    class Meta: 
        model = testForm
        fields = ['supervisor', 'yourname', 'email', 'subject','message','totals']
       
       



