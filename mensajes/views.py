from msilib.schema import ListView
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .models import UserProfile, Message
from .forms import MessageForm
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .models import UserProfile, Message
from .forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

class MessageDetailView(DetailView):
    model = UserProfile
    template_name = 'message_detail.html'

class MessageCreateView(FormView):
    form_class = MessageForm
    template_name = 'message_form.html'
    
    def form_valid(self, form):
        sender = UserProfile.objects.get(user=self.request.user)
        recipient = UserProfile.objects.get(pk=self.kwargs['pk'])
        content = form.cleaned_data['content']
        Message.objects.create(sender=sender, recipient=recipient, content=content)
        return redirect('message_detail', pk=recipient.pk)

class MessageDetailView(DetailView):
    model = UserProfile
    template_name = 'message_detail.html'

class MessageCreateView(FormView):
    form_class = MessageForm
    template_name = 'message_form.html'
    
    def form_valid(self, form):
        sender = UserProfile.objects.get(user=self.request.user)
        recipient = UserProfile.objects.get(pk=self.kwargs['pk'])
        content = form.cleaned_data['content']
        Message.objects.create(sender=sender, recipient=recipient, content=content)
        return redirect('message_detail', pk=recipient.pk)  
     
@method_decorator(login_required, name='dispatch')
   
class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'
    
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_list')  # Redirige a la página deseada después del registro
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
    
