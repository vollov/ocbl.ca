from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from team.models import Player
from team.views import ProfileService

from django.utils.translation import ugettext as _

import logging
logger = logging.getLogger(__name__)

def home(request):
    logger.debug('calling app.views.home()')

    # Translators: This message appears on the home page only
    context = {
        'page_title': _('Home'),
    }
    return render(request,'home.html', context)

@login_required
def profile(request):
    """
    show user profile [GET /profile]
    """
    logger.debug('calling team.views.profile()')
    user_id = request.session['user_id']
    service = ProfileService(user_id)
    return HttpResponseRedirect(service.getProfile())
