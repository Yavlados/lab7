from django.conf.urls import url
from my_app.views import OrderView

urlpatterns = [
    url(r'^orders(?P<id>\d+)', OrderView.as_view(), name='order_url'),
]
