# import json
# import os
# from django.conf import settings
# from .errors import DjLdException


# def load(path):
#     ld_files_path = getattr(
#         settings, 'LD_JSON_PATH',
#         os.path.join(settings.BASE_DIR, 'ldjson')
#     )
#     if not ld_files_path:
#         raise DjLdException('No LD_JSON_PATH configured in settings.py')
#     with open(path) as ld_file:
#         try:
#             context = json.loads(ld_file.read())
#         except:
#             raise DjLdException('Error parsing {0}'.format(path))
#     return context
