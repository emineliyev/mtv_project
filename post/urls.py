from django.urls import path
from .views import IndexView, post_detail, get_category, slider_detail, get_tag

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:post_pk>/', post_detail, name='detail'),
    path('slider_detail/<int:slider_pk>/', slider_detail, name='slider_detail'),
    path('category/<int:category_pk>', get_category, name='category'),
    path('tag/<int:tag_pk>', get_tag, name='tag')
]