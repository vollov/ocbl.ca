from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from team.models import Player
from team.views import ProfileService
from content.models import Block

from django.utils.translation import ugettext as _
from django.utils.translation import get_language
from django.urls import resolve

import logging
logger = logging.getLogger(__name__)

def home(request):

    # Translators: This message appears on the home page only
    context = {
        'page_title': _('Home'),
    }
    return render(request,'home.html', context)

def privacy(request):

    context = {
        'page_title': _('privacy_policy'),
    }
    return render(request,'privacy.html', context)

def terms(request):

    context = {
        'page_title': _('terms'),
    }
    return render(request,'terms.html', context)

from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    
    #logger.debug('current dict={0}'.format(dictionary))
    
    return dictionary.get(key)

def rules(request):
    locale = get_language()
    #current_url = resolve(request.path_info).namespace#url_name
    
    logger.debug('current locale={0}'.format(locale))
    blocks = Block.objects.filter(locale=locale, page__name='rules')
    
    block_dict = {}
    for block in blocks:
        content = block.content.encode('utf-8').strip()
        #logger.debug('getting block code = {0}, content={1}'.format(block.code, content))
        block_dict[block.code] = content

    #logger.debug('content = {0}'.format(block_dict['GAME_RULES']))
    context = {
        'page_title': _('rules'),
        'block_geame_rules': block_dict['GAME_RULES'],
    }
    return render(request,'rules.html', context)

def contacts(request):
    context = {
        'page_title': _('contacts'),
        'contact_email': 'dike.zhang@gmail.com',
    }
    return render(request,'contacts.html', context)



@login_required
def profile(request):
    """
    show user profile [GET /profile]
    """
    logger.debug('calling team.views.profile()')
    user_id = request.session['user_id']
    service = ProfileService(user_id)
    return HttpResponseRedirect(service.getProfile())
