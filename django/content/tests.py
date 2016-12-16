from django.test import TestCase

###############################################
## test settings service
###############################################
from service import SettingService

class TestSettingService(TestCase):
    
    fixtures = ['setting.json']
    
    def test_load_enable_registration(self):
        enabled = SettingService.get('enable_registration')
        print 'enable_registration {0}'.format(enabled)
        self.assertTrue(enabled, 'registration should be enabled')