from rest_framework.permissions import DjangoModelPermissions
from copy import deepcopy
# Permisos listos para usar


# class CustomDjangoModelPermissions(DjangoModelPermissions):
#     view_permissions = ['%(app_label)s.view_%(model_name)s']

#     perms_map = {
#         'GET': view_permissions,
#         'OPTIONS': view_permissions,
#         'HEAD': view_permissions,
#         'POST': DjangoModelPermissions.perms_map['POST'],
#         'PUT': DjangoModelPermissions.perms_map['PUT'],
#         'PATCH': DjangoModelPermissions.perms_map['PATCH'],
#         'DELETE': DjangoModelPermissions.perms_map['DELETE'],
#     }


class CustomDjangoModelPermissions(DjangoModelPermissions):

    def __init__(self):
        self.perms_map = deepcopy(self.perms_map)
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']

