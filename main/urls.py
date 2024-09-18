from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('add_car/', views.add_car, name='add_car'),
    path('delete_car/<int:id>/', views.delete_car, name='delete_car'),
    # path('update_car/<int:id>', views.update_car, name='update_car'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/',views.register, name='register'),
    path('edit/<int:id>',views.edit, name='edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
