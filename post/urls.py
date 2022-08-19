from django.urls import path
from .views import IndexView, post_detail, GetCategory, slider_detail, GetTag, Search, Contact

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:post_pk>/', post_detail, name='detail'),
    path('slider_detail/<int:slider_pk>/', slider_detail, name='slider_detail'),
    # path('category/<int:category_pk>/', get_category, name='category'),
    path('category/<int:category_pk>/', GetCategory.as_view(), name='category'),
    path('tag/<int:tag_pk>', GetTag.as_view(), name='tag'),
    path('search/', Search.as_view(), name='search'),
    path('contact/', Contact.as_view(), name='contact')
]