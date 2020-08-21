from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'network', views.ReseauViewSet)
router.register(r'sink', views.PuitsViewSet)
router.register(r'sensors', views.CapteurViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [ 
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    #path('docs/', include('rest_framework_swagger.urls')),
]

