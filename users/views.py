from users.models import User
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, reverse, HttpResponse

# Create your views here.


def render_register_user_form(request):
    template = 'users/register_user_form.html'
    return render(request, template)


def process_register_user_form(request):
    if request.method == 'POST':
        new_user = User(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        new_user.save()

        return HttpResponseRedirect(reverse('users:login'))
    return HttpResponse('Error: method not allowed.')


def render_login_user_form(request):
    template = 'users/login_user_form.html'
    return render(request, template)


def process_login_user_form(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'], password=request.POST['password'])
        except User.DoesNotExist:
            return HttpResponse('User does not exist.')

        return HttpResponseRedirect(reverse('books:catalogue', kwargs={'user_pk': user.pk}))
    return HttpResponse('Error: method not allowed.')
