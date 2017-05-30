from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework import viewsets, filters

from .forms import LoginForm
from .models import User

from .models import User, Brassiere
from .serializer import UserSerializer, BrassiereSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BrassiereViewSet(viewsets.ModelViewSet):
    queryset = Brassiere.objects.all()
    serializer_class = BrassiereSerializer



def index(request):
    return render(request, 'index.html')

def sign_up(request):
    if request.method == 'POST':  # フォームが提出された
        form = LoginForm(request.POST)  # POST データの束縛フォーム
        if form.is_valid():  # バリデーションを通った
            User.objects.create(**form.cleaned_data)
            return redirect('login:sign_up_done')  # POST 後のリダイレクト
    else:
        form = LoginForm()  # 非束縛フォーム
        d = {
            'form': form,
        }
        return render(request, 'sign_up.html', d)

def sign_up_done(request):
    return render(request, 'sign_up_done.html')

def sign_in(request):
    return render(request, 'sign_in.html')



