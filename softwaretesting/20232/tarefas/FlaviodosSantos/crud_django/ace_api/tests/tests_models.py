from django.test import TestCase
from ..models import Ace

class AceTestCase(TestCase):

    def setUp(self):
        Ace.objects.create(
            nome='Antonio',
            matricula=14666,
            zona=3
        )

    def test_retorno_str_erro(self):
        ace = Ace.objects.get(nome='Antonio')
        self.assertEquals(ace.__str__(), 'Antony')

    def test_retorno_str(self):
        ace = Ace.objects.get(nome='Antonio')
        self.assertEquals(ace.__str__(), 'Antonio')

    def test_matricula(self):
        ace = Ace.objects.get(nome='Antonio')
        self.assertEquals(ace.matricula, '14666')
    
    def test_zona(self):
        ace = Ace.objects.get(nome='Antonio')
        self.assertEquals(ace.zona, 3)
    
    def test_is_active(self):
        ace = Ace.objects.get(nome='Antonio')
        self.assertTrue(ace.is_active)


