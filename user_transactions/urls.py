from rest_framework import routers
from .views import ApiCategorySet, ApiTransactionSet

router = routers.SimpleRouter()
router.register('category_list', ApiCategorySet,  basename='category')
router.register('transaction_list', ApiTransactionSet, basename='transaction')
urlpatterns = router.urls
