from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('stock-list/', views.StockListView.as_view(), name='stock-list'),
    path('bio/', views.BioView.as_view(), name='bio-view'),
    path('create/', views.CreateView.as_view(), name='stock-create'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='stock-update'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='stock-delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)