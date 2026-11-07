import unittest
from multimodal_demo.core import render, search, recall_at_k

class TestSearch(unittest.TestCase):
    def setUp(self): self.items=[{"id":"red_circle","color":"red","shape":"circle"},{"id":"blue_square","color":"blue","shape":"square"}]
    def test_image(self): self.assertEqual(render("red","circle").size,(96,96))
    def test_search(self): self.assertEqual(search(self.items,"blue square",1)[0]["id"],"blue_square")
    def test_unknown(self): self.assertEqual(search(self.items,"unknown",1),[])
    def test_recall(self): self.assertEqual(recall_at_k(self.items,[{"text":"red circle","relevant_ids":["red_circle"]}]),1.0)
