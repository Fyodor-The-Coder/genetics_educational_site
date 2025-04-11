from django.db import models

class Term(models. Model):
    term_id = models.AutoField(db_column='term_id', primary_key=True)
    term_ru = models.CharField(max_length=255)
    term_en = models.CharField(max_length=255, blank=True)
    term_definition = models.TextField()

    def __str__(self):
        return self.term_ru

    def save(self, *args, **kwargs):

        self.term_ru = self.capitalize_first(self.term_ru)
        self.term_definition = self.capitalize_first(self.term_definition)
        super().save(*args, **kwargs)

    @staticmethod
    def capitalize_first(text):
        if not text:
            return text
        return text[0].upper() + text[1:].lower()