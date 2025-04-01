# quick-test
prueba tecnica para la empresa Quick

### requerimientos:
tener instalado Docker compose e iniciar docker

ejecutar el siguiente comando para iniciar los servidores de base de datos, servidor web de Django y servidor de Redis

```bash
  sudo docker compose up
```

abrir el navegador e ir a la direccion [http://0.0.0.0:8000/apiV1/token/](http://0.0.0.0:8000/apiV1/token/) para obtener token de autenticacion

el usuario admin tiene contraseña admin124

en Settings Debug debe estar en True para que se pueda ver los css de la pagina de administrador
```bash
DEBUG = True
```

se puede ir a http://0.0.0.0:8000/admin/ para agregar elementos a la base de datos pero se deben agregar los modelos 
```bash
admin.site.register(Restaurant)
admin.site.register(Place)
admin.site.register(Menu_item)
admin.site.register(Order)
admin.site.register(Order_item)
admin.site.register(Delivery)
admin.site.register(Profile)
```

se pueden apagar los servidores presionando  CONTROL-C
