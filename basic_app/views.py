from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from .models import Sekolah, Murid


# Create your views here.
# view cara lama pakai function
def index(request):
    return render(request, 'index.html', {'page_title':'Index dengan Function Based Views'})

# view dengan class based view
class CBView(View):
    def get(self, request):
        return HttpResponse('CBV')


class IndexCBVView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Index dengan Class Based Views'
        return context


class SekolahList(ListView):
    model = Sekolah
    context_object_name = 'daftar_sekolah'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Selamat datang di Halaman Daftar Sekolah'
        return context


class SekolahDetail(DetailView):
    model = Sekolah
    context_object_name = 'detail_sekolah'
    template_name = 'basic_app/sekolah_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Selamat datang di Halaman Detail Sekolah'
        return context