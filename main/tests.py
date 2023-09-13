from django.test import TestCase

from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_nama_siswa_benar(self):
        response = response = Client().get('/main/')
        self.assertContains(response,'Zaidan Naufal Ilmi')
    
    def test_npm_siswa_benar(self):
        response = response = Client().get('/main/')
        self.assertContains(response,'2206081761')

    def test_kelas_siswa_benar(self):
        response = response = Client().get('/main/')
        self.assertContains(response,'PBP F')
    
