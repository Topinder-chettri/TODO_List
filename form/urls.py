from django.urls import path
from form import views
from .views  import *
urlpatterns = [
    path('home/',views.home,name='home'),
    path('autherized',views.autherized,name="autherized"),
   #path('list/',views.list,name='list'),
    path('list/',NoteListView.as_view(), name='list'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('detail/<int:pk>/edit',NotesUpdateView.as_view(),name='update'),
    path('detail/<int:pk>/delete',NotesDeletView.as_view(),name='delete'),
    path('create/',NotesCreateView.as_view(), name='create'),
    path('thanks/',ThanksTemplateview.as_view(), name='thanks'),
    path('signup/',views.SignupView.as_view(), name='signup'),
    path('login/',views.LoginInterfaceView.as_view(), name='login'),
    path('logout/',views.LogoutInterfaceView.as_view(), name='logout'),
    
]