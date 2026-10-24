
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import Document


User = get_user_model()


class DocumentAccessTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(
            username="owner",
            password="TestPassword123!",
        )
        self.other_user = User.objects.create_user(
            username="other",
            password="TestPassword456!",
        )

        test_file = SimpleUploadedFile(
            "test.txt",
            b"Private test content",
            content_type="text/plain",
        )

        self.document = Document.objects.create(
            title="Private document",
            description="Access control test",
            category="test",
            file=test_file,
            owner=self.owner,
        )

    def test_owner_can_download_document(self):
        self.client.force_login(self.owner)

        response = self.client.get(
            reverse(
                "download_document",
                args=[self.document.pk],
            )
        )

        self.assertEqual(response.status_code, 200)
        response.close()

    def test_other_user_cannot_download_document(self):
        self.client.force_login(self.other_user)

        response = self.client.get(
            reverse(
                "download_document",
                args=[self.document.pk],
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_other_user_cannot_see_document_on_dashboard(self):
        self.client.force_login(self.other_user)

        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Private document")
