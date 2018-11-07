from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from users.views import UserViewSet, UserPlayerViewSet, GroupViewSet, PlayerEvolveView
from itens.views import ItenViewSet, PlayerInvetoryViewSet
from avatar.views import AvatarViewSet, getAvatarImageView
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'players', UserPlayerViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'itens', ItenViewSet)
router.register(r'inventory', PlayerInvetoryViewSet)
router.register(r'avatar', AvatarViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^playerevolve/', PlayerEvolveView.as_view(), name='PlayerEvolve'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('static/', getAvatarImageView.as_view(), name='avatar_images')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
