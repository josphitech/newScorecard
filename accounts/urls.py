from django.conf.urls import url
from .views import SignUpView

urlpatterns = [
    url('signup/', SignUpView.as_view(), name='signup')
]
