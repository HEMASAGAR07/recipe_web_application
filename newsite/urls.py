from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from home.views import *

urlpatterns = [
    path("", home, name='home'),
    path("delete-recipe/<int:id>/" , delete_recipe , name="delete_recipe"),
    path('update-recipe/<int:id>/', update_recipe, name='update_recipe'),
    path('recipe/', recipe_view, name='recipe_view'),
    path('login/',login_page,name='login_page'),
    path('register/',register_page,name='register_page'),
    path("admin/", admin.site.urls),
    path('logout/' ,logout_page , name='logout_page' )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
