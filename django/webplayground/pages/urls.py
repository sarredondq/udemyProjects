from django.urls import path
from .views import PageListView,PageDetailDetailView,PageCreate,PageUpdate,PageDelete,PruebaView

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>', PageUpdate.as_view(), name='update'),
    path('delete/<int:pk>', PageDelete.as_view(), name='delete'),
    path('prueba/', PruebaView.as_view(), name='prueba'),
], 'pages')