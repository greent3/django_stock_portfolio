from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from stocks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', include('stocks.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.StockListView.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
