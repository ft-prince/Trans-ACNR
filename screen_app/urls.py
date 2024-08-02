from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

   # Screen URLs   
    path('screens/', views.ScreenListView.as_view(), name='screen_list'),
    path('screens/<int:pk>/', views.ScreenDetailView.as_view(), name='screen_detail'),
    path('screens/create/', views.ScreenCreateView.as_view(), name='screen_create'),
    path('screens/<int:pk>/update/', views.ScreenUpdateView.as_view(), name='screen_update'),
    path('screens/<int:pk>/delete/', views.ScreenDeleteView.as_view(), name='screen_delete'),
    path('screens/<int:screen_id>/add_content/', views.add_content_to_screen, name='add_content_to_screen'),
    # PDF URLs
    path('pdfs/', views.PDFFileListView.as_view(), name='pdf_list'),
    path('pdfs/<int:pk>/', views.PDFFileDetailView.as_view(), name='pdf_detail'),
    path('pdfs/create/', views.PDFFileCreateView.as_view(), name='pdf_create'),
    path('pdfs/<int:pk>/update/', views.PDFFileUpdateView.as_view(), name='pdf_update'),
    path('pdfs/<int:pk>/delete/', views.PDFFileDeleteView.as_view(), name='pdf_delete'),

    # Video URLs
    path('videos/', views.VideoFileListView.as_view(), name='video_list'),
    path('videos/<int:pk>/', views.VideoFileDetailView.as_view(), name='video_detail'),
    path('videos/create/', views.VideoFileCreateView.as_view(), name='video_create'),
    path('videos/<int:pk>/update/', views.VideoFileUpdateView.as_view(), name='video_update'),
    path('videos/<int:pk>/delete/', views.VideoFileDeleteView.as_view(), name='video_delete'),

    #  Sliders
    path('video/<int:screen_id>/', views.screen_slider, name='screen_slider'),
    path('pdf/<int:screen_id>/', views.pdf_slider, name='pdf_slider'),

]