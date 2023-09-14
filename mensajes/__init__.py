from mensajes.models import UserProfile


class MessageDetailView(DetailView):
    model = UserProfile
    template_name = 'message_detail.html'