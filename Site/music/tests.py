from django.test import TestCase
from .forms import *
from django.core.files.uploadedfile import SimpleUploadedFile


class Articles_Form_Test(TestCase):

    def test_ArticlesForm_valid(self):
        upload_file = open('music/sel_test/test_audio.mp3', 'rb')
        file_dict = {'audio': SimpleUploadedFile(upload_file.name, upload_file.read())}
        form = ArticlesForm({'title': 'test', 'full_text': "test", 'date': "2021-12-22 10:15:20"}, file_dict)
        self.assertTrue(form.is_valid())

    def test_ArticlesForm_invalid(self):
        form = ArticlesForm({'title': "", 'full_text': "", 'date': "", 'audio': ""})
        self.assertFalse(form.is_valid())

