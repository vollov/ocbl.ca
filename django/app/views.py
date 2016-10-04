import logging
from django.shortcuts import render_to_response
from datetime import datetime

logger = logging.getLogger(__name__)

def home(request):
    logger.debug('calling app.views.home()')

    context = {
        'page_title': 'Home',
    }
    return render_to_response('home.html', context)