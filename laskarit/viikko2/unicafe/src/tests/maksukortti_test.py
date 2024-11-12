import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1234)
        self.assertEqual(self.maksukortti.saldo_euroina(), 22.34)

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(900)
        self.assertEqual(self.maksukortti.saldo_euroina(), 1)

    def test_saldo_ei_mene_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_ota_rahaa_palauttaa_True(self):
        value = self.maksukortti.ota_rahaa(900)
        self.assertTrue(value)

    def test_ota_rahaa_palauttaa_False(self):
        value = self.maksukortti.ota_rahaa(1100)
        self.assertFalse(value)
