"""
URL configuration for CancerPresentation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name = 'home'),
    path("causes_prevention", views.CausesPreventionView.as_view(), name = 'causes_prevention'),
    path("symptoms", views.SymptomsView.as_view(), name = 'symptoms'),
    path("treamtment", views.TreamtmentView.as_view(), name = 'treamtment'),
    path("cad_prediction", views.CadPredictionView.as_view(), name = 'cad_prediction'),
    path('predict_cad', views.predict_cad),
    path("cad_stage_prediction", views.CadStagePredictionView.as_view(), name = 'cad_stage_prediction'),
    path('predict_cad_stage', views.predict_cad_stage),
]
