from django.conf.urls import url
from . import views

app_name = 'companies'

urlpatterns = [
    # /stocks/
    url(r'^$', views.StockList.as_view(), name='index'),
]
