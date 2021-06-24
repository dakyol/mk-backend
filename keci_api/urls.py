from django.urls import path
from .views import ProjectList, ProjectDetail

app_name = 'keci_api'

urlpatterns = [
    path('<uuid:id>/', ProjectDetail.as_view(), name='detailcreate'),
    path('', ProjectList.as_view(), name='listcreate'),
]