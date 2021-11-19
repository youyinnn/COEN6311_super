import os
from django.apps import AppConfig

class ResearcherConfig(AppConfig):
    name = 'researcher'
    
    def ready(self):
        if os.environ.get('RUN_MAIN') == 'true':
            print('Django start up code')
            # asyncio.run(ws.start_up())
