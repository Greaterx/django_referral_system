from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Referral
import random
import string


def home(request):
    return render(request, 'referral/home.html')


def login_with_phone(request):
    if request.method == 'GET':
        return render(request, 'referral/login_with_phone.html')
    else:
        if 'code' in request.POST:
            code = request.POST['code']
            phone = request.POST['phone']

            user = authenticate(request, username=phone, password=code)
            if user is None:
                return render(request, 'referral/login_with_phone.html')
            login(request, user)
            if Referral.objects.filter(user_id=user.id):
                return redirect('current_user')
            random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            Referral.objects.create(user=user, my_referral=random_str, phone_number=phone)
            return redirect('current_user')

        else:
            code = list('0123456789')
            lenght = int(request.GET.get('lenght', 4))
            the_code = ''
            for x in range(lenght):
                the_code += random.choice(code)
            if User.objects.filter(username=request.POST['phone']):
                user = User.objects.get(username=request.POST['phone'])
                user.set_password(the_code)
            else:
                user = User.objects.create_user(request.POST['phone'], password=the_code)
            user.save()
            return render(request, 'referral/login_with_phone.html', {'phoneWrite': request.POST['phone'], 'codeWrite': the_code})


def current_user(request):
    referrals = Referral.objects.get(user_id=request.user.id)
    if 'invite_code' in request.POST:
        referrals.another_referral = request.POST['invite_code']
        referrals.save()
    alien_referrals = Referral.objects.filter(another_referral=referrals.my_referral)
    return render(request, 'referral/current_user.html', {'referrals': referrals, 'alien_referrals': alien_referrals})
