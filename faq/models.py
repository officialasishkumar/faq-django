from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)

    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def get_translation(self, lang_code):
        cache_key = f'faq_{self.pk}_{lang_code}'
        translation = cache.get(cache_key)
        if translation:
            return translation

        if lang_code == 'en':
            translation = {'question': self.question, 'answer': self.answer}
        elif lang_code == 'hi':
            translation = {'question': self.question_hi or self.question,
                           'answer': self.answer_hi or self.answer}
        elif lang_code == 'bn':
            translation = {'question': self.question_bn or self.question,
                           'answer': self.answer_bn or self.answer}
        else:
            translation = {'question': self.question, 'answer': self.answer}
        
        cache.set(cache_key, translation, timeout=60 * 60)  # Cache for 1 hour
        return translation

    def save(self, *args, **kwargs):
        translator = Translator()

        if not self.question_hi:
            try:
                self.question_hi = translator.translate(self.question, src='en', dest='hi').text
            except Exception as e:
                print("Hindi translation (question) failed:", e)
                self.question_hi = self.question
        if not self.answer_hi:
            try:
                self.answer_hi = translator.translate(self.answer, src='en', dest='hi').text
            except Exception as e:
                print("Hindi translation (answer) failed:", e)
                self.answer_hi = self.answer

        if not self.question_bn:
            try:
                self.question_bn = translator.translate(self.question, src='en', dest='bn').text
            except Exception as e:
                print("Bengali translation (question) failed:", e)
                self.question_bn = self.question
        if not self.answer_bn:
            try:
                self.answer_bn = translator.translate(self.answer, src='en', dest='bn').text
            except Exception as e:
                print("Bengali translation (answer) failed:", e)
                self.answer_bn = self.answer

        super().save(*args, **kwargs)

        for lang in ['en', 'hi', 'bn']:
            cache_key = f'faq_{self.pk}_{lang}'
            cache.delete(cache_key)

    def __str__(self):
        return self.question
