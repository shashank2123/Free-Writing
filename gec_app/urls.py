from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView
from gec_app import views

app_name = "gec_app"
urlpatterns = [
    path('gec',views.load_gec_page,name='gec'),
]