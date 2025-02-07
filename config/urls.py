from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.main.urls'), name='main'),
    path('emailer/', include('app.emailer.urls'), name='emailer'),
]
