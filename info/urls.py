from django.conf.urls import include,url
from .views import MyView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('infoview', MyView)
urlpatterns = [
    url('^info/', include((router.urls, 'info'), namespace='info'))
]