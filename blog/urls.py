from django.urls import path

from . import views

urlpatterns = [
    path("", view=views.Index.as_view(), name='index-page'),
    path("posts", views.Posts.as_view(), name='posts-page'),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name='post-detail-page'),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("admin",view=views.AdminPageView.as_view(),name="admin")
]
