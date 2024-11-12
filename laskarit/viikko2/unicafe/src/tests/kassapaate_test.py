import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_kassa_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edullisia_lounaita_nolla(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukkaita_lounaita_nolla(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_syo_edullisesti_kateisella(self):
        change = self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000 + 240)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(change, 60)

    def test_syo_edullisesti_kateisella_riittamaton_maksu(self):
        change = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(change, 200)

    def test_syo_maukkaasti_kateisella(self):
        change = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000 + 400)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(change, 100)

    def test_syo_maukkaasti_kateisella_riittamaton_maksu(self):
        change = self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(change, 300)

    def test_syo_edullisesti_kortilla(self):
        value = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertTrue(value)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla(self):
        value = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertTrue(value)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kortilla_liian_vahan_rahaa(self):
        kortti = Maksukortti(200)
        value = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertFalse(value)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_liian_vahan_rahaa(self):
        kortti = Maksukortti(200)
        value = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertFalse(value)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kortti.saldo, 2000)
        self.assertEqual(self.kassa.kassassa_rahaa, 101000)

    def test_lataa_rahaa_kortille_negatiivinen_summa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1)
        self.assertEqual(self.kortti.saldo, 1000)

    def test_kassassa_rahaa_euroina(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)
