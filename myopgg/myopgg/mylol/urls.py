from django.conf.urls import url
from . import views
app_name = "mylol"
urlpatterns = [
        url(
        regex=r'^tier/$',
        view=views.getTier.as_view(),
        name='getTier'
    ), url(
        regex=r'^rate/$',
        view=views.getRate.as_view(),
        name='getRate'
    ), url(
        regex=r'^ingame/$',
        view=views.getIngame.as_view(),
        name='getIngame'
    ),
]