from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework import viewsets, filters

from .forms import LoginForm

from .models import User, Brassiere
from .serializer import UserSerializer, BrassiereSerializer

from rest_framework.decorators import api_view



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
            return redirect('apps:sign_up_done')  # POST 後のリダイレクト
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

def bra_admin(request):
    all_bra = Brassiere.objects.all()
    d = {
        'bra' : all_bra,
    }
    return render(request, 'bra_admin.html', d)

#APIから受け取ったデータをBrassiereテーブルを更新する
#
# @api_view(['GET', 'POST'])
# def bra_data(request):
#     if request.method == 'POST':
#         b = Brassiere.objects.get(pk='1')
#         serializedData =





