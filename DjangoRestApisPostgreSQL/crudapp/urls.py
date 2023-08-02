from django.urls import re_path, path
from crudapp.views import ItemDetailView

urlpatterns = [
    re_path(r'^items/(?P<pk>[0-9]*)(/?)$', ItemDetailView.as_view()),
]
