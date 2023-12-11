from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accountapp/', include('accountapp.urls')),
    path('', include('userapp.urls')),
    path('adminapp/', include('adminapp.urls')),
    path('blogapp/', include('blogapp.urls')),
    path('courseapp/', include('courseapp.urls')),
    path('projectapp/', include('projectapp.urls')),
    path('practiceapp/', include('practiceapp.urls')),
    path('tutorialapp/', include('tutorialapp.urls')),
    path('studentapp/', include('studentapp.urls')),

    path('paymentapp/', include('paymentapp.urls')),
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




