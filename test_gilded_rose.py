# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    
    def test_backstage(self):
        bp = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(bp, 0, 10)]
        gr = GildedRose(items)
        gr.update_quality()
        ans = 5
        assert items[0].quality == ans


    def test_sulfuras(self):
        s = "Sulfuras, Hand of Ragnaros"
        items = [Item(s, 0, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 18
        assert items[0].sell_in == 1

    def test_aged_brie(self):
        ab = "Aged Brie"
        items = [Item(ab, 2, 48)]
        gr = GildedRose(items)
        gr.update_quality()
        gr.update_quality()
        gr.update_quality()
        gr.update_quality()
        ans = 52
        assert items[0].quality == ans

if __name__ == '__main__':
    unittest.main()
