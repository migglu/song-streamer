from rest_framework import routers

from .views import ArtistsViewSet
from .views import AlbumsViewSet
from .views import SongsViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'artists', ArtistsViewSet)
router.register(r'artists/(?P<artist_id>[0-9]+)/albums', AlbumsViewSet,
                base_name='albums')
router.register(r'artists/(?P<artist_id>[0-9]+)/'
                r'albums/(?P<album_id>[0-9]+)/songs', SongsViewSet,
                base_name='songs')

urlpatterns = router.urls
