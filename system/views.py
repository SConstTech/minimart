from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def is_low_staff(user):
    return user.groups.filter(name='low_staff').exists()

@login_required()
def home_redirect(request):
    if is_low_staff(request.user):
        return redirect('staff:home')
    elif request.user.is_superuser:
        return redirect('/admin')
    elif request.user.is_staff:
        return redirect('/admin')


@login_required()
def logout_view(request):
    logout(request)
    return redirect('system:login')
