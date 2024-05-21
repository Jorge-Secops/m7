from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('nueva_vivienda/', views.agregar_vivienda, name='agregar_vivienda'),
    path('editar_inmueble/', views.editar_inmueble, name='editar_inmueble'),
    path('oferta/', views.ver_oferta, name='ver_oferta'),
    
]


#path('editar-inmueble/<int:inmueble_id>/', views.editar_inmueble, name='editar_inmueble'),