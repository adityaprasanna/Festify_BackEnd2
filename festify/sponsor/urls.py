from rest_framework_mongoengine.routers import DefaultRouter

from festify.sponsor import views

router = DefaultRouter()
router.register(r'^v1', views.SponsorViewSet, basename='coordinator')
urlpatterns = router.urls