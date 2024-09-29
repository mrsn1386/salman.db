from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import TemplateView, ListView
from account.forms import RegisterForm, LoginForm, ForgetPasswordForm, ResetPasswordForm
from posts import urls


# Create your views here.
class Welcome(TemplateView):
    template_name = 'account/welcome_page.html'


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {'register_form': register_form}
        return render(request, 'account/register_page.html', context)

    def post(self, request: HttpRequest):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=email).first()
            if user is None:
                user: User = User.objects.filter(username__iexact=username).first()
                if user is None:
                    user: User = User.objects.create_user(username=username, email=email)
                    user.set_password(password)
                    user.save()
                    return redirect(reverse('login_page'))
                else:
                    register_form.add_error('email', 'اطلاعات نادرست می باشد')
            else:
                register_form.add_error('email', 'اطلاعات نادرست می باشد')
        context = {'register_form': register_form}
        return render(request, 'account/register_page.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {'login_form': login_form}
        return render(request, 'account/login_page.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(username__iexact=username).first()
            if user is not None:
                if user.check_password(password):
                    login(request, user)
                    return redirect(reverse('all_posts'))
                else:
                    login_form.add_error("email", 'اطلاعات وارد شده نادرست می باشد')
            else:
                login_form.add_error("email", 'اطلاعات وارد شده نادرست می باشد')

        context = {'login_form': login_form}
        return render(request, 'account/login_page.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('index_page'))


class ForgetPasswordView(View):
    def get(self, request):
        forget_pass_form = ForgetPasswordForm()
        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'account/forgot_pass_page.html', context)

    def post(self, request):
        forget_pass_form = ForgetPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            email = forget_pass_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=email).first()
            if user is not None:
                return redirect(email)
            else:
                forget_pass_form.add_error('email', 'ایمیل وارد شده ثبت نشده است')

        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'account/forgot_pass_page.html', context)


class ResetPasswordView(View):
    def get(self, request, email):
        reset_pass_form = ResetPasswordForm()
        user: User = User.objects.filter(email__iexact=email).first()
        if user is None:
            return redirect(reverse('login_page'))
        context = {'reset_pass_form': reset_pass_form}
        return render(request, 'account/reset_pass_page.html', context)

    def post(self, request, email):
        reset_pass_form = ResetPasswordForm(request.POST)
        if reset_pass_form.is_valid():
            password = reset_pass_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=email).first()
            user.set_password(password)
            user.save()
            return redirect(reverse('login_page'))
        context = {'reset_pass_form': reset_pass_form}
        return render(request, 'account/reset_pass_page.html', context)
