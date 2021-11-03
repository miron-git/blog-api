from django.urls import path, include
from rest_framework.authtoken import views
from .views import APIPost, APIPostDetail, APIComment, APIGroup, APIFollow, APICommentDetail, APIGroupDetail, PostViewSet
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    #JWT токен
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('post/<int:pk>/', APIPostDetail.as_view()),
    #path('post/', APIPost.as_view()),
    path('post/<int:id>/comment/', APIComment.as_view()),
    path('post/<int:post_id>/comment/<int:pk>/', APICommentDetail.as_view()),
    path('group/<int:pk>/', APIGroupDetail.as_view()),
    path('group/', APIGroup.as_view()),
    path('follow/', APIFollow.as_view()),
]