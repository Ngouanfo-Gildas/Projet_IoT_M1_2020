from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'network', views.ReseauViewSet)
router.register(r'sink', views.PuitsViewSet)
router.register(r'sensors', views.CapteurViewSet)
router.register(r'services', views.ServiceViewSet)
"""router.register(r'souscription', views.PuitsViewSet)
router.register(r'data_app', views.CapteurViewSet)
router.register(r'data_ctrl', views.ReseauViewSet)
router.register(r'state_sensor', views.PuitsViewSet)"""

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [ 
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('addapp-data/', views.api_new_DAPP, name='api_new_DAPP'),
    path('addctrl-data/', views.api_new_DCTRL, name='api_new_DCTRL'),
    path('add-data/', views.add_data, name='add_data'),
    
    #path('docs/', include('rest_framework_swagger.urls')),
]

