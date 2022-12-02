from django.shortcuts import render,redirect
from django.views.generic import TemplateView, View
from newsletters.models import NewsLetter
from newsletters.forms import NewsLetterCreationForm
from django.conf import settings
from django.core.mail import send_mail, EmailMessage


# Create your views here.
class DashboardHomeView(TemplateView):
  template_name = "dashboard/index.html"


class NewsLetterDashboardHomeView( View ):
  def get(self, request, *args, **kwargs):
    newsletters = NewsLetter.objects.all()

    context = {
      'newsletters': newsletters 
    }

    return render(request, 'dashboard/list.html', context) 

class NewsLetterCreateView( View ):
  def get( self, request, *args, **kwargs):
    form = NewsLetterCreationForm()
    context= {
      'form': form
    }
    return render(request, 'dashboard/create.html', context)

  def post( self, request, *args, **kwargs):

    if request.method=="POST":
      form = NewsLetterCreationForm(request.POST or None)
      if form.is_valid():
        instance = form.save()
        newsletter = NewsLetter.objects.get( id = instance.id )

        if newsletter.status == "Published":
          subject = newsletter.subject
          body = newsletter.body
          from_email = settings.EMAIL_HOST_USER
          for email in newsletter.email.all():
            send_mail( subject = subject, from_email = from_email, recipient_list = [email], message = body, fail_silently = True )
        return redirect('dashboard:list') 
      
    context= {

    }
    return render(request, 'dashboard/create.html', context)
   