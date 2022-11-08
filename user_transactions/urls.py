from django.urls import path
from .views import ApiCategoryList

urlpatterns = [
    path('category_list/', ApiCategoryList.as_view()),

]
