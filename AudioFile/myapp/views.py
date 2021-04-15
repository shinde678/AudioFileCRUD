from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import *
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, RedirectView
from myapp.forms import *
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q

class HomeView(TemplateView):
    template_name = 'index.html'

# Manage Song
class ManageSongListView(ListView):
    model = Song
    template_name = 'manage_song.html'
    ordering = ['-upload_time']
    paginate_by = 10
    paginate_orphans = 1

    queryset = Song.objects.all()

    def get_context_data(self, *args, **kwargs):
        try:
            return super(ManageSongListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(ManageSongListView, self).get_context_data(*args, **kwargs)  

# Create new Song
class CreateSong(SuccessMessageMixin, CreateView):
	model = Song
	template_name = 'add_song.html'
	form_class = SongForm 
	success_url = reverse_lazy('manageSong')
	success_message = "%(song_name)s Was Created Successfully"
	
	def form_valid(self,form):
		return super().form_valid(form)

	def form_invalid(self, form):
		return self.render_to_response(self.get_context_data(form=form))         


# Update Song View
class EditSong(SuccessMessageMixin, UpdateView):
    model = Song
    template_name  = 'edit_song.html'
    form_class = SongForm	
    success_url = reverse_lazy('manageSong')
    success_message = "%(song_name)s Was Update Successfully"

    def form_valid(self,form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form)) 

# Search Song
class SearchSong(ListView):
    def get(self, request):
        search = request.GET['search']
        if search:
            object_list = Song.objects.filter(Q(song_name__icontains=search) | Q(duration__icontains=search) | Q(upload_time__icontains=search))
            return render(request,'manage_song.html',{'object_list':object_list})            

# Delete Song
class DeleteSong(DeleteView):
    model = Song
    success_url = reverse_lazy('manageSong')
    template_name = 'delete_confirm.html'                     


# Podcast content
class ManagePodcastListView(ListView):
    model = Podcast
    template_name = 'manage_podcast.html'
    ordering = ['-upload_time']
    paginate_by = 10
    paginate_orphans = 1

    queryset = Podcast.objects.all()

    def get_context_data(self, *args, **kwargs):
        try:
            return super(ManagePodcastListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(ManagePodcastListView, self).get_context_data(*args, **kwargs)      


# Create new podcast
class CreatePodcast(SuccessMessageMixin, CreateView):
	model = Podcast
	template_name = 'add_podcast.html'
	form_class = PodcastForm 
	success_url = reverse_lazy('managePodCast')
	success_message = "%(podcast_name)s Was Created Successfully"
	
	def form_valid(self,form):
		return super().form_valid(form)

	def form_invalid(self, form):
		return self.render_to_response(self.get_context_data(form=form))                 


# Update Podcast View
class EditPodcast(SuccessMessageMixin, UpdateView):
    model = Podcast
    template_name  = 'edit_podcast.html'
    form_class = PodcastForm	
    success_url = reverse_lazy('managePodCast')
    success_message = "%(podcast_name)s Was Update Successfully"

    def form_valid(self,form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

# Search Podcast
class SearchPodcast(ListView):
    def get(self, request):
        search = request.GET['search']
        if search:
            object_list = Podcast.objects.filter(Q(podcast_name__icontains=search) | Q(duration__icontains=search) | Q(upload_time__icontains=search) | Q(host__icontains=search) | Q(participants__icontains=search))
            return render(request,'manage_podcast.html',{'object_list':object_list})                    

# Delete Podcast
class DeletePodcast(DeleteView):
    model = Podcast
    success_url = reverse_lazy('managePodCast')
    template_name = 'delete_confirm.html'               


# Podcast AudioBook
class ManageAudioBookListView(ListView):
    model = AudioBook
    template_name = 'manage_audiobook.html'
    ordering = ['-upload_time']
    paginate_by = 10
    paginate_orphans = 1

    queryset = AudioBook.objects.all()

    def get_context_data(self, *args, **kwargs):
        try:
            return super(ManageAudioBookListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(ManageAudioBookListView, self).get_context_data(*args, **kwargs)       

# Create new AudioBook
class CreateAudioBookView(SuccessMessageMixin, CreateView):
	model = AudioBook
	template_name = 'add_audiobook.html'
	form_class = AudioBookForm 
	success_url = reverse_lazy('manageAudioBook')
	success_message = "%(title)s Was Created Successfully"
	
	def form_valid(self,form):
		return super().form_valid(form)

	def form_invalid(self, form):
		return self.render_to_response(self.get_context_data(form=form))                 

# Update Audiobook View
class EditAudioBook(SuccessMessageMixin, UpdateView):
    model = AudioBook
    template_name  = 'edit_audiobook.html'
    form_class = AudioBookForm
    success_url = reverse_lazy('manageAudioBook')
    success_message = "%(title)s Was Update Successfully"

    def form_valid(self,form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))  

# Search Audiobook
class SearchAudioBook(ListView):
    def get(self, request):
        search = request.GET['search']
        if search:
            object_list = AudioBook.objects.filter(Q(title__icontains=search) | Q(author__icontains=search) | Q(narrator__icontains=search))
            return render(request,'manage_audiobook.html',{'object_list':object_list})        

# Delete Podcast
class DeleteAudioBookView(DeleteView):
    model = AudioBook
    success_url = reverse_lazy('manageAudioBook')
    template_name = 'delete_confirm.html'             