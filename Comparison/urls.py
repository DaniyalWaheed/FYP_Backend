from .views import dmFeatureComparison, getTwoFeaturesNames, getTwoMLAlgoNames
from django.conf.urls import url, include

urlpatterns = [
    url(r'^getTwoFeaturesNames/', getTwoFeaturesNames, name='dmFeatureComparison'),
    url(r'^getTwoMLAlgoNames/', getTwoMLAlgoNames, name='mlComparison'),
]