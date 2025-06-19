
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)
def home(request):
    html_content = """
    <html>
        <head><title>TASK TRACKER API</title></head>
        <body style="font-family: Arial; background-color: #f2f2f2; padding: 50px;">
            <h1 style="color: #2c3e50;">Welcome to <span style="color: #3498db;">TASK TRACKER API</span>!</h1>
            <p style="font-size: 18px;">TASK TRACKER</p>
            <p><a href="/swagger/" style="color: #2980b9;">Swagger документациясына өтүү</a></p>
        </body>
    </html>
    """
    return HttpResponse(html_content)

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
