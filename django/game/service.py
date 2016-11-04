from content.models import Image

class GamePhotoHelper:
    """Helper classs to prepare Game photo view data"""
    
    def __init__(self):
        pass
    
    @classmethod
    def get_photos(self, albumn_slug):
        """Get photos by slug for a view"""
        photos = Image.objects.filter(active = True, albumn__slug= albumn_slug).order_by('weight')
        return photos
        
    @classmethod
    def get_games(self, games):
        """Prepare games object for display photos"""
        game_dict = {}
        
        i = 1
        for game in games:
            g = {}
            
            g['id'] = game.id
            g['name'] = game.name()
            # albumn with slug: /albumn/albumn-slug
            g['albumn_slug'] = game.albumn.slug
            
            game_dict[i] = g
            i+=1
        
        return game_dict
        
