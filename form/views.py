from dataclasses import field
from pyexpat import model
from re import template
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notes
from django.http import Http404
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from django.views.generic.base import TemplateView
from django.contrib.admin.widgets import AdminDateWidget,AdminSplitDateTime,AdminTimeWidget
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

from .models import Notes
from .forms import NotesModelForm

# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'temp/register.html'
    success_url = '/list/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes_list')
        return super().get(request, *args, **kwargs)

class LoginInterfaceView(LoginView):
    template_name = 'temp/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'temp/logout.html'

class NotesCreateView(LoginRequiredMixin,CreateView):
    model = Notes
    fields = ['title','text','date','time']
    success_url = '/create/'
    template_name = 'temp/note_form.html'
    login_url ="/login"

    def get_queryset(self):
        return self.request.user.notes.all()


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NoteListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'temp/note_list.html'
    login_url ="/login"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDeletView(DeleteView):
    model = Notes
    fields = ['title','text','date','time']
    success_url = '/list/'
    template_name = 'temp/note_form.html'

class ThanksTemplateview(TemplateView):
    template_name = 'temp/thanks.html'

    
class NotesUpdateView(UpdateView):
    model = Notes
    fields = ['title','text','date','time']
    success_url = '/list/'
    template_name = 'temp/note_form.html'

    

#def new(request):
    #return render(request,'temp/note_form.html')
    


def drop(request):
    return render(request,'temp/drop.html')


def  home(request):
    return render(request,"temp/index.html",{'today':datetime.today()})

@login_required(login_url='/admin')
def autherized(request):
    return render(request,"temp/autherized.html")

#def list(request):
   # all_notes = Notes.objects.all()
  #  return render(request,'temp/note_list.html',{'notes':all_notes})


def detail(request,pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note Doesn't exist!")
    return render(request,'temp/note_detail.html',{'note':note})