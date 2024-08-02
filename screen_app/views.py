from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .models import Screen, PDFFile, VideoFile
from .forms import ScreenForm, PDFFileForm, VideoFileForm
from django.core.paginator import Paginator
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


def home(request):
    return render(request, 'screen_app/home.html')

staff_member_required_cbv = method_decorator(staff_member_required, name='dispatch')

# Screen views
@staff_member_required_cbv
class ScreenListView(ListView):
    model = Screen
    template_name = 'CRUD/screen_list.html'
    context_object_name = 'screens'

@staff_member_required_cbv
class ScreenDetailView(DetailView):
    model = Screen
    template_name = 'CRUD/screen_detail.html'

@staff_member_required_cbv
class ScreenCreateView(CreateView):
    model = Screen
    form_class = ScreenForm
    template_name = 'CRUD/screen_form.html'
    success_url = reverse_lazy('screen_list')

@staff_member_required_cbv
class ScreenUpdateView(UpdateView):
    model = Screen
    form_class = ScreenForm
    template_name = 'CRUD/screen_form.html'
    success_url = reverse_lazy('screen_list')

@staff_member_required_cbv
class ScreenDeleteView(DeleteView):
    model = Screen
    template_name = 'CRUD/screen_confirm_delete.html'
    success_url = reverse_lazy('screen_list')

@staff_member_required
def add_content_to_screen(request, screen_id):
    screen = get_object_or_404(Screen, pk=screen_id)
    
    if request.method == 'POST':
        pdf_form = PDFFileForm(request.POST, request.FILES, prefix='pdf')
        video_form = VideoFileForm(request.POST, request.FILES, prefix='video')
        
        if 'pdf_submit' in request.POST and pdf_form.is_valid():
            pdf = pdf_form.save()
            screen.upload_pdf.add(pdf)
            return redirect('screen_detail', pk=screen_id)
        
        if 'video_submit' in request.POST and video_form.is_valid():
            video = video_form.save()
            screen.upload_video.add(video)
            return redirect('screen_detail', pk=screen_id)
    else:
        pdf_form = PDFFileForm(prefix='pdf')
        video_form = VideoFileForm(prefix='video')
    
    return render(request, 'CRUD/add_content_to_screen.html', {
        'screen': screen,
        'pdf_form': pdf_form,
        'video_form': video_form
    })

# PDF Views
@staff_member_required_cbv
class PDFFileListView(ListView):
    model = PDFFile
    template_name = 'pdfs/pdf_list.html'
    context_object_name = 'pdfs'

@staff_member_required_cbv
class PDFFileDetailView(DetailView):
    model = PDFFile
    template_name = 'pdfs/pdf_detail.html'

@staff_member_required_cbv
class PDFFileCreateView(CreateView):
    model = PDFFile
    form_class = PDFFileForm
    template_name = 'pdfs/pdf_form.html'
    success_url = reverse_lazy('pdf_list')

@staff_member_required_cbv
class PDFFileUpdateView(UpdateView):
    model = PDFFile
    form_class = PDFFileForm
    template_name = 'pdfs/pdf_form.html'
    success_url = reverse_lazy('pdf_list')

@staff_member_required_cbv
class PDFFileDeleteView(DeleteView):
    model = PDFFile
    template_name = 'pdfs/pdf_confirm_delete.html'
    success_url = reverse_lazy('pdf_list')

# Video Views
@staff_member_required_cbv
class VideoFileListView(ListView):
    model = VideoFile
    template_name = 'videos/video_list.html'
    context_object_name = 'videos'
    paginate_by = 10  # Number of items per page

@staff_member_required_cbv
class VideoFileDetailView(DetailView):
    model = VideoFile
    template_name = 'videos/video_detail.html'

@staff_member_required_cbv
class VideoFileCreateView(CreateView):
    model = VideoFile
    form_class = VideoFileForm
    template_name = 'videos/video_form.html'
    success_url = reverse_lazy('video_list')

@staff_member_required_cbv
class VideoFileUpdateView(UpdateView):
    model = VideoFile
    form_class = VideoFileForm
    template_name = 'videos/video_form.html'
    success_url = reverse_lazy('video_list')

@staff_member_required_cbv
class VideoFileDeleteView(DeleteView):
    model = VideoFile
    template_name = 'videos/video_confirm_delete.html'
    success_url = reverse_lazy('video_list')


#  sliders

def screen_slider(request, screen_id):
    screen = get_object_or_404(Screen, screen_id=screen_id)
    videos = screen.upload_video.all()
    context = {
        'screen': screen,
        'videos': videos,
    }
    return render(request, 'screen_app/screen_slider.html', context)


def pdf_slider(request, screen_id):
    screen = get_object_or_404(Screen, screen_id=screen_id)
    pdfs = screen.upload_pdf.all()
    context = {
        'screen': screen,
        'pdfs': pdfs,
    }
    return render(request, 'screen_app/pdf_slider.html', context)

