from django.test import TestCase

###############################################
## test enroll forms 
###############################################
from team.forms import EnrollForm
from team.models import Team
from django.contrib.auth.models import User
from accounts.models import UserProfile

class TestEnrollForm(TestCase):
    fixtures = ['auth_all.json', 'accounts_all.json','team_all.json']
    
    def test_enroll_forms(self):
        form_data = {'team': 'a3256bc3-af94-4b7d-b547-3ac4630cd8b7',
                     }
        enroll_form = EnrollForm(data=form_data)
        
        if not enroll_form.is_valid():
            print enroll_form.errors
        else:
            self.assertTrue(enroll_form.is_valid())
            player = enroll_form.save(commit=False)
            
            user_profile = UserProfile.objects.get(user__username='dave')
            player.user_profile=user_profile
            
            # get team
            team_id = enroll_form.cleaned_data['team']
            #team = Team.objects.get(id=team_id)
            #player.team = team
            player.save()

###############################################
## test profile views 
###############################################
from team.views import ProfileService
from team.models import Player
class TestProfileService(TestCase):
    fixtures = ['auth_all.json', 'accounts_all.json','team_all.json']
    
    def test_captain_profile(self):
        captain = User.objects.get(username='dustin')
        service = ProfileService(captain.id)
        url = service.getProfile()
#         print url
        self.assertEqual(url, '/team/captain/9')
        
    def test_is_approved_player(self):
        captain = User.objects.get(username='dustin')
        service = ProfileService(captain.id)
        result = service.is_approved_player()
#         print result
#         print Player.objects.filter(user_profile__user__id = captain.id, active=True).query
        self.assertTrue(result)
        
    def test_is_captain(self):
        captain = User.objects.get(username='dustin')
        service = ProfileService(captain.id)
        result = service.is_captain()
        self.assertTrue(result)
        
    def test_is_not_captain(self):
        captain = User.objects.get(username='rogan')
        service = ProfileService(captain.id)
        result = service.is_captain()
        self.assertFalse(result)
    
    def test_is_not_approved_player(self):
        captain = User.objects.get(username='rogan')
        service = ProfileService(captain.id)
        result = service.is_approved_player()
        self.assertFalse(result)
    
# from django.test import Client
# 
# client=Client()
# context = {'username':'dustin', 'password':'Fgbhu89o'}
# response = client.post('/accounts/login/', context)
# print "login returns {0}".format(response.status_code)