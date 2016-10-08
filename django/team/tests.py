from django.test import TestCase

###############################################
## test player forms 
###############################################
from team.forms import PlayerForm 
class TestPlayerForm(TestCase):
    def test_player_forms(self):
        form_data = {'username': 'martin',
                     'first_name': 'Martin',
                     'last_name': 'Bright',
                     'email':'martin@abc.com',
                     'password':'pwd123',
                     'password_confirm':'pwd123',
                     'captcha_0':'dummy-value',
                     'captcha_1':'PASSED'}
        player_form = PlayerForm(data=form_data)
        
        if not user_form.is_valid():
            print user_form.errors
        else:
            self.assertTrue(user_form.is_valid())
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
