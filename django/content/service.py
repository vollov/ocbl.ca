from content.models import SystemSetting

class SettingService:
    def __init__(self):
        print 'initial setting service'
        
    setting_dict = {};
    
    @classmethod
    def get(self, key):
        if not self.setting_dict:
            self.load_setting()
            
        return self.setting_dict[key]
    
    def get_value(self, data_type, value):
        """convert boolean and string"""
        if data_type == 'b':
            if value.lower()=='true':
                return True
            else:
                return False
        elif data_type == 's':
            return value
        else:
            return int(value)
        
    def load_setting(self):
        settings = SystemSetting.objects.all()
        for item in settings:
            self.setting_dict[item.name] = self.getValue(item.data_type, item.value)
        