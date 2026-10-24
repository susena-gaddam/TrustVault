
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("upload/", views.upload_document, name="upload"),
    path(
        "documents/<int:document_id>/download/",
        views.download_document,
        name="download_document",
    ),
]


