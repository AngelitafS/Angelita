from django.contrib import admin
from django.urls import path
from FKIP.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('MathEdu/', Index),
 path('fkip/', Index),
 path('faperta/', Index),
path('FEB/', Index),
path('FH/', Index),
path('FISIP/', Index),
path('FK/', Index),
path('FT/', Index),
path('PascaSarjana/', Index),
]
