from django.conf.urls import include, url
from django.contrib import admin
from biblioteca import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'misitio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^buscar/$', views.buscar, name='buscar'),
    url(r'^libro/(?P<id_libro>\d+)/$', views.LibroDetail.as_view(), name='detail'),

    #Home
    url(r'^$',views.HomeView.as_view(), name ='Home'),

    #Registrar
    url(r'^registrar/libro/$',views.LibroCreate.as_view(), name='registrar_libro'),
    url(r'^registrar/libro/def/$',views.registrar_libro, name='registrar_libro_def'),

    #Actualizar
    url(r'^actualizar/clase/libro/(?P<id_libro>\d+)/$', views.LibroUpdate.as_view(), name='actualizar_libro'),
    url(r'^actualizar/libro/(?P<id_libro>\d+)/$', views.actualizar_libro, name='actualizar_libro_def'),

    #Eliminar
    url(r'^eliminar/libro/(?P<id_libro>\d+)/$',views.LibroDelete.as_view(), name='eliminar_libro'),
    url(r'^eliminar/libro/def/(?P<id_libro>\d+)/$',views.eliminar_libro, name='eliminar_libro_def'),

    #Listar
    url(r'^listar/libros/$', views.LibroList.as_view(), name='listar_libro'),
    url(r'^listar/libros/def/$', views.lista_libros, name='listar_libro_def'),
]

