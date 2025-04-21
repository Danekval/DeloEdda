from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view  # Исправлено: drf_yasg
from drf_yasg import openapi
from furniture.views import HomePageView , CatalogView, ContactsView, ApplicationView , SuccessView# Раскомментируйте импорт

schema_view = get_schema_view(
    openapi.Info(  # Исправлено: Info с заглавной буквы
        title="Furniture API",
        default_version='v1',
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),  # Исправлено: with_ui
    path('api/', include('api.urls')),  # Запятая добавлена
    path('', HomePageView.as_view(), name='index'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('application/', ApplicationView.as_view(), name='application'),
    path('application/success/', SuccessView.as_view(), name='application_success'),
]