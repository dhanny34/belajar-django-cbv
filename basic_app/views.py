from django.shortcuts import render
from django.views.generic import (View, 
                                    TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from .models import Sekolah, Murid
from django.urls import reverse_lazy


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


class SekolahListView(ListView):
    model = Sekolah
    context_object_name = 'daftar_sekolah'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Selamat datang di Halaman Daftar Sekolah'
        return context


class SekolahDetailView(DetailView):
    model = Sekolah
    context_object_name = 'detail_sekolah'
    template_name = 'basic_app/sekolah_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Selamat datang di Halaman Detail Sekolah'
        return context


class SekolahCreateView(CreateView):
    fields = ('nama', 'kepsek', 'lokasi')
    model = Sekolah

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Form Data Sekolah'
        return context


class SekolahUpdateView(UpdateView):
    fields = ('nama', 'kepsek')
    model = Sekolah

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Form Data Sekolah'
        return context


class SekolahHapusView(DeleteView):
    model = Sekolah

    success_url = reverse_lazy('basic_app:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Hapus Sekolah'
        return context
