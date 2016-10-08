import logging
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required

from django.core import serializers
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

def home(request):
    logger.debug('calling app.views.home()')

    context = {
        'page_title': 'Home',
    }
    return render(request,'home.html', context)

@login_required
def profile(request):
    """
    show user profile [GET /profile]
    """
    logger.debug('calling team.views.profile()')
    user_id = request.session['user_id']
    
    user = User.objects.get(id = user_id)
    context = {
        'page_title': 'User profile',
        'user': user,
    }
    return render(request,'profile.html', context)