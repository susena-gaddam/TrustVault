from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Document


@login_required
def home(request):
    documents = Document.objects.filter(owner=request.user)

    message = "Welcome to TrustVault!\n"
    message += f"Your documents: {documents.count()}\n"

    for document in documents:
        message += f"- {document.title}\n"

    return HttpResponse(message, content_type="text/plain")