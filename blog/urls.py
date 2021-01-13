from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import home, post_single, categories_archive, category_single, like_comment, PostArchive, PostDetails, \
    CategoryDetails, create_comment
from .api import comment_detail,\
    comment_list, PostList,\
    PostDetail, PostDetailMixin, PostListMixin,\
    PostListGeneric, PostDetailGeneric, PostViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet)


# post_list = PostViewSet.as_view({'get': 'list', 'post': 'create'})
# post_detail = PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})

urlpatterns = [
    path('', home, name='home'),
    path('posts/', PostArchive.as_view(), name='posts_archive'),
    path('post/<slug:slug>/', post_single, name='post_single'),
    path('categories/', categories_archive, name='categories_archive'),
    # path('categories/<slug:pk>/', category_single, name='category_single'),
    path('categories/<slug:slug>/', CategoryDetails.as_view(), name='category_single'),
    path('like_comment/', like_comment, name='like_comment'),
    path('comments/', create_comment, name='add_comment'),
    # path('json/posts/', post_list, name='post_list'),
    # path('json/posts/<int:pk>', post_detail, name='post_detail'),
    path('json/comments/', comment_list, name='comment_list'),
    path('json/comments/<int:pk>', comment_detail, name='comment_detail'),
    path('json/', include(router.urls)),
]
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])

