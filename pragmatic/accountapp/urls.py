from django.urls import path
from accountapp.views import hello_werld

app_name = "accountapp"


urlpatterns = [
        path('hello_world/', hello_werld, name='hello_world')
]