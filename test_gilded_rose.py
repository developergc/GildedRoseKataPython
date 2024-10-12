# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_conjured_minimum_zero(self):
        cur = [Item("Conjured Salad", 0, 2)]
        gr = GildedRose(cur)
        gr.update_quality()
        gr.update_quality()
        gr.update_quality()
        assert cur[0].quality == 0

    def test_conjured_decrease(self):
        cur = [Item("Conjured Salad", 5, 8)]
        gr = GildedRose(cur)
        gr.update_quality()
        assert cur[0].sell_in == 4
        assert cur[0].quality == 6

    def test_conjured_fast_decrease(self):
        cur = [Item("Conjured Salad", 0, 8)]
        gr = GildedRose(cur)
        assert cur[0].sell_in == -1
        gr.update_quality()
        assert cur[0].quality == 4


    def test_backstage(self):
        bp = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(bp, 5, 15)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 18

    def test_sulfuras(self):
        s = "Sulfuras, Hand of Ragnaros"
        items = [Item(s, 1, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 20
        assert items[0].sell_in == 1

    def test_aged_brie(self):
        ab = "Aged Brie"
        items = [Item(ab, 2, 48)]
        gr = GildedRose(items)
        gr.update_quality()
        gr.update_quality()
        gr.update_quality()
        gr.update_quality()
        assert items[0].quality == 50


if __name__ == '__main__':
    unittest.main()
