from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import FAQ

class FAQModelTest(APITestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is your name?",
            answer="<p>My name is ChatGPT.</p>",
            question_hi="आपका नाम क्या है?",
            answer_hi="<p>मेरा नाम चैटजीपीटी है।</p>",
            question_bn="তোমার নাম কী?",
            answer_bn="<p>আমার নাম ChatGPT।</p>",
        )

    def test_get_translation_default(self):
        translation = self.faq.get_translation('en')
        self.assertEqual(translation['question'], "What is your name?")
        self.assertIn("<p>", translation['answer'])

    def test_get_translation_hindi(self):
        translation = self.faq.get_translation('hi')
        self.assertEqual(translation['question'], "आपका नाम क्या है?")
        self.assertIn("<p>", translation['answer'])

    def test_get_translation_bengali(self):
        translation = self.faq.get_translation('bn')
        self.assertEqual(translation['question'], "তোমার নাম কী?")
        self.assertIn("<p>", translation['answer'])


class FAQAPITest(APITestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is your name?",
            answer="<p>My name is Asish.</p>",
            question_hi="आपका नाम क्या है?",
            answer_hi="<p>मेरा नाम असीश है।</p>",
            question_bn="তোমার নাম কী?",
            answer_bn="<p>আমার নাম Asish।</p>",
        )

    def test_api_get_default(self):
        url = reverse('faq-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['question'], "What is your name?")

    def test_api_get_hindi(self):
        url = reverse('faq-list')
        response = self.client.get(url + '?lang=hi')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['question'], "आपका नाम क्या है?")

    def test_api_get_bengali(self):
        url = reverse('faq-list')
        response = self.client.get(url + '?lang=bn')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['question'], "তোমার নাম কী?")
