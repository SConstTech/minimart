from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from system.models import *
# Create your views here.


def is_low_staff(user):
    return user.groups.filter(name='low_staff').exists()


@login_required
@user_passes_test(is_low_staff)
def home(request):
    front_data = InventoryItems.objects.all()
    return render(request, 'home.html', locals())
