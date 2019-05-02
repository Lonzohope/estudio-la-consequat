import os
class Config:
        '''
        General configuration parent class
        '''
        # PHOTO_BASE_URL ="https://api.pexels.com/v1/curated?per_page=15&page=1"
        # SOURCE_API="https://api.pexels.com/v1/search?query=example+query&per_page=15&page=1"
        # PEXELS_URL="https://api.pexels.com/v1/curated?per_page=15&page=1"
        # PHOTO_API_KEY  = os.environ.get('PHOTO_API_KEY')

class ProdConfig(Config):
        '''
        Production  configuration child class

        Args:
            Config: The parent configuration class with General configuration settings
        '''
        pass


class DevConfig(Config):
        '''
        Development  configuration child class

        Args:
            Config: The parent configuration class with General configuration settings
        '''

        DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}