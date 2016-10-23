from django.shortcuts import render
from django.http import HttpResponse,Http404
from accounts.forms import UserProfileForm, UserForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

import logging
logger = logging.getLogger(__name__)

def register(request):
    """
    user registration form: GET/POST /registration
    """
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            human = True
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            # save user in session
            login(request, user)
            
            logger.info('user {0} registered successfully'.format(user.username))
            
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('profile'))

        else:
            print user_form.errors
#             raise Http404("Your registration is failed.")
        
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    context = {'user_form': user_form, 'profile_form': profile_form};
    return render(request, 'register.html', context);

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                # save user in session
                request.session['user_id'] = user.id
                return HttpResponseRedirect(reverse('profile'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            logger.error("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})

from django.contrib.auth import logout

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logger.debug('user_logout() {0}'.format(request))
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/accounts/login')