
from pathlib import Path

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import FileResponse

from .models import Document


@login_required
def home(request):
    documents = Document.objects.filter(owner=request.user)

    return render(request, "documents/home.html", {
        "documents": documents,
    })


@login_required
def upload_document(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        category = request.POST.get("category", "").strip()
        uploaded_file = request.FILES.get("file")
        
        allowed_extensions = {".pdf", ".txt", ".doc", ".docx"}

        if uploaded_file and Path(uploaded_file.name).suffix.lower() not in allowed_extensions:
            messages.error(
                request,
                "Only PDF, TXT, DOC, and DOCX files are allowed.",
            )
            return redirect("upload")


        if not title or not uploaded_file:
            messages.error(request, "Title and file are required.")
            return redirect("upload")

        if uploaded_file.size > 5 * 1024 * 1024:
            messages.error(request, "File must be 5 MB or smaller.")
            return redirect("upload")

        Document.objects.create(
            title=title,
            description=description,
            category=category,
            file=uploaded_file,
            owner=request.user,
        )

        messages.success(request, "Document uploaded successfully.")
        return redirect("home")

    return render(request, "documents/upload.html")


@login_required
def download_document(request, document_id):
    document = get_object_or_404(
        Document,
        pk=document_id,
        owner=request.user,
    )

    response = FileResponse(
        document.file.open("rb"),
        as_attachment=True,
        filename=Path(document.file.name).name,
    )
    return response
