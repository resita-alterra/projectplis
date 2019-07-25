
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('ATA.urls'))
=======
    path('',include('ATA.urls'))
>>>>>>> dev
]
