from django.contrib.auth.models import Group
from rest_framework.permissions import BasePermission
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.request import Request
from rest_framework.views import APIView
from copy import deepcopy
from typing import List

class EsGrupoBase(BasePermission):
	nombre_grupo: str  = ''
	def has_permission(self, request: Request , view: APIView)-> bool:
		return request.user.groups.filter(name=self.nombre_grupo).exists()

class EsGrupoAdministrador(EsGrupoBase):
    nombre_grupo: str ='Administrador'

class EsGrupoRevisor(EsGrupoBase):
    message: str = 'No perteneces al grupo de Revisores'
    nombre_grupo: str ='Revisor'

class EsIpPermitida(BasePermission):
    message: str = 'Ip no permitida'
    ip_bloqueadas: List[str] = ['127.0.0.1','192.168.01']

    def has_permission(self, request: Request, view: APIView) -> bool:
        return request.META['REMOTE_ADDR'] not in self.ip_bloqueadas


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
        self.perms_map: dict[str,List[str]] = deepcopy(self.perms_map)
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']

