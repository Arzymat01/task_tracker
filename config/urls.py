
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import JsonResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)
def home(request):
    return JsonResponse({"message": "Welcome to Doctor Consultant API!"})

schema_view = get_schema_view(
   openapi.Info(
      title="Task Tracker API",
      default_version='v1',
      description="Жумуш башкаруу системасынын API'си",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[],  
)


urlpatterns = [
    path('', home),  
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
