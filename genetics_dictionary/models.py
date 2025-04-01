from django.db import models

class Term(models. Model):
    term_id = models.AutoField(db_column='term_id', primary_key=True)
    term_ru = models.CharField(max_length=255)
    term_en = models.CharField(max_length=255)
    term_definition = models.TextField()

    def __str__(self):
        return self.term_ru