from django.urls import path, include
from. import views
from .views import registro
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('libros/editar/<int:id>', views.editar, name='editar'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir/', views.salir, name='salir'),
    path('registro/', registro, name='registro'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)