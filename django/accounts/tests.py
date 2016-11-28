from django.test import TestCase

# from unittest.TestCase import assertFalse, assertTrue
import logging
logger = logging.getLogger(__name__)

###############################################
## test user forms 
###############################################
from accounts.forms import UserForm 
class TestUserForm(TestCase):
    
#     @classmethod
#     def setUpClass(cls):
#         logger.debug('### TestUserForm')

    def test_user_forms(self):
        form_data = {'username': 'martin',
                     'first_name': 'Martin',
                     'last_name': 'Bright',
                     'email':'martin@abc.com',
                     'password':'pwd123',
                     'password_confirm':'pwd123',
                     'captcha_0':'dummy-value',
                     'captcha_1':'PASSED'}
        user_form = UserForm(data=form_data)
        
        if not user_form.is_valid():
            print user_form.errors
        else:
            self.assertTrue(user_form.is_valid())
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

###############################################
## test user profile forms 
###############################################
from accounts.forms import UserProfileForm 
class TestUserprofileForm(TestCase):
    
    def test_profile_forms(self):
        user_form_data = {'username': 'dave',
                     'first_name': 'dave',
                     'last_name': 'Bright',
                     'email':'dave@abc.com',
                     'password':'pwd123',
                     'password_confirm':'pwd123',
                     }
        user_form = UserForm(data=user_form_data)
        
        if not user_form.is_valid():
            print user_form.errors
        else:
            self.assertTrue(user_form.is_valid())
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            
            profile_form_data = {
                'birth_year':1983,
                'captcha_0':'dummy-value',
                'captcha_1':'PASSED'
            }
            profile_form = UserProfileForm(data=profile_form_data)
            
            if not profile_form.is_valid():
                print profile_form.errors
            else:
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

###############################################
## test registration form
###############################################
class TestRegistrationForm(TestCase):
    
    fixtures = ['auth_all.json', 'accounts_all.json',]
        
    def test_password_no_match(self):
        user_form_data = {'username': 'martin',
             'first_name': 'martin',
             'last_name': 'Bright',
             'email':'dave@abc.com',
             'password':'pwd123',
             'password_confirm':'pwd123x',
             }
        
        user_form = UserForm(data=user_form_data)
        
        if not user_form.is_valid():
            pass
#             print user_form.errors
        else:
            self.assertTrue(user_form.is_valid())
            user = user_form.save(commit=False)
            user.set_password(user.password)
            
            profile_form_data = {
                'birth_year':1983,
                'captcha_0':'dummy-value',
                'captcha_1':'PASSED'
            }
            profile_form = UserProfileForm(data=profile_form_data)
            
            self.assertFalse(profile_form.is_valid(), "test_password_no_match not success")
#             if not profile_form.is_valid():
#                 print 'test_password_no_match form error ={0}'.format(profile_form.errors)
#             else:
#                 profile = profile_form.save(commit=False)
#                 print 'test_password_no_match profile form is good'
    
    def test_username_duplicate(self):
        form_data = {'username': 'dave',
                     'first_name': 'dave',
                     'last_name': 'Bright',
                     'email':'martin@abc.com',
                     'password':'pwd123',
                     'password_confirm':'pwd123',
                     'captcha_0':'dummy-value',
                     'captcha_1':'PASSED'}
        user_form = UserForm(data=form_data)
        
        self.assertFalse(user_form.is_valid(), "test_username_duplicate not success")
#         if not user_form.is_valid():
#             print 'test_username_duplicate form error ={0}'.format(user_form.errors)
    
    