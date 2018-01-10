from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View,ListView
from datetime import datetime
from .models import *
from .registration import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required



class OrdersView(View):
    def get(self, request):
        variable = 'Django'
        today_date = datetime.now()
        data = {
            'orders': [
                {'title': 'Первый заказ', 'id': 1},
                {'title': 'Второй заказ', 'id': 2},
                {'title': 'Третий заказ', 'id': 3}
            ]
        }
        return render(request, 'orders.html', locals())


class OrderView(View):
    def get(self, request, id):
        variable = 'Django'
        today_date = datetime.now()
        data = {
            'order': {
                'id': id
            }
        }
        return render(request,'order.html', locals())


def main(request):
    return render(request, 'main.html', locals())
def bd(request):
    return render(request, 'bd.html', locals())

class TovarList(ListView):
    model = Tovar
    template_name = "tovar.html"

class ShopList(ListView):
    model = Shop
    template_name = "shop.html"

class ShopList1(ListView):
    model = Shop
    template_name = "assort.html"


    def get(self, request, *args, **kwargs):
        self.id = request.GET.get('id')
        return super(ShopList1, self).get(request, *args, **kwargs)
    def get_queryset(self):
        if self.id:
            return Shop.objects.filter(id=self.id)

class WorkerList(ListView):
    model = Worker
    template_name = "workers.html"


def registration(request):
    errors = {'username': '', 'password': '', 'password2': '', 'email': '', 'firstname': '', 'surname': ''}
    error_flag = False
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['username'] = 'Введите логин'
            error_flag = True
        elif len(username) < 5:
            errors['username'] = 'Логин должен превышать 5 символов'
            error_flag = True
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Такой логин уже существует'
            error_flag = True
        password = request.POST.get('password')
        if not password:
            errors['password'] = 'Введите пароль'
            error_flag = True
        elif len(password) < 8:
            errors['password'] = 'Длина пароля должна превышать 8 символов'
        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors['password2'] = 'Пароли должны совпадать'
            error_flag = True
        email = request.POST.get('email')
        if not email:
            errors['email'] = 'Введите e-mail'
        firstname = request.POST.get('firstname')
        if not firstname:
            errors['firstname'] = 'Введите имя'
        surname = request.POST.get('surname')
        if not surname:
            errors['surname'] = 'Введите фамилию'
        if not error_flag:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=surname)
            return HttpResponseRedirect('/login')
    return render(request, 'registration.html', locals())


def registration2(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'),
                                            email=request.POST.get('email'),
                                            password=request.POST.get('password'),
                                            first_name=request.POST.get('firstname'),
                                            last_name=request.POST.get('surname'))
            return HttpResponseRedirect('/login')
    return render(request, 'registration2.html', {'form': form})


def login(request):
    error = ""
    username = None
    password = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/success')
        else:
            error = "Попробуй ещё раз"
    return render(request, 'login.html', locals())


@login_required()
def success(request):
    return render(request,'success.html', locals())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/main/')



