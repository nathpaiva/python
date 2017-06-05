# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.utils import timezone
from .models import Question


class MeuTeste(TestCase):
    def test_question(self):
        pergunta = Question.objects.create(question_text='Ola tudo bem?',pub_date=timezone.now())
        self.assertEqual(pergunta.id, 1)
