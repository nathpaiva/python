from django.conf.urls import url, include
from . import views
from .models import Question
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)


app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
] + router.urls
