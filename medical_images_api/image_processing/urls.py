from django.urls import path
from .views import (
    MedicalImageResultListCreateAPIView,
    MedicalImageResultDetailAPIView
)

urlpatterns = [
    path('results/', MedicalImageResultListCreateAPIView.as_view(), name='list_create_results'),
    path('results/<str:id>/', MedicalImageResultDetailAPIView.as_view(), name='detail_result'),
]
