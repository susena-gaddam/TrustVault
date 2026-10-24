from django.contrib import admin
from .models import Document, DocumentPermission, AuditLog

admin.site.register(Document)
admin.site.register(DocumentPermission)
admin.site.register(AuditLog)
