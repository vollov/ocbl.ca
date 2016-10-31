class GamePhotoHelper:
    """Helper classs to prepare Game photo view data"""
    
    def __init__(self):
        pass
    
    def get_albums(self):
        """Get album for a view"""
    
    def get_games(self, games):
        """Prepare games object for display photos"""
        game_dict = {}
        
        i = 1
        for game in games:
            g = {}
            
            g['id'] = game.id
            g['name'] = game.name()
            # album with slug: /album/album-slug
            g['album_slug'] = game.album.slug
            
            game_dict[i] = g
            i+=1
        
        return game_dict
        
