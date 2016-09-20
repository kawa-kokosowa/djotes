from djotes.rest import views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'notes', views.NoteViewSet, base_name='note')
router.register(r'user', views.UserViewSet, base_name='user')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
