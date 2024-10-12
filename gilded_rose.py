# -*- coding: utf-8 -*-
from abc import ABC
from abc import abstractmethod


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class processor_abstract(ABC):
    @abstractmethod
    def update_quality(self, item: Item):
        pass


class processor_normal(processor_abstract):
    def update_quality(self, item: Item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = max(item.quality - 1, 0)


class processor_sulfuras(processor_abstract):
    def update_quality(self, item: Item):
        pass


class processor_backstage_pass(processor_abstract):
    def update_quality(self, item: Item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11:
                item.quality = min(item.quality + 1, 50)
            if item.sell_in < 6:
                item.quality = min(item.quality + 1, 50)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0


class processor_aged_brie(processor_abstract):
    def update_quality(self, item: Item):
        item.quality = min(item.quality + 1, 50)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = min(item.quality + 1, 50)


class processor_conjured(processor_abstract):
    def update_quality(self, item: Item):
        drop = 4 if item.sell_in <= 0 else 2
        item.quality = max(item.quality - drop, 0)
        item.sell_in -= 1


class GildedRose(object):

    def __init__(self, items: list[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = self.get_processor(item)
            updater.update_quality(item)

    def get_processor(self, item: Item) -> processor_abstract:
        if item.name == "Sulfuras, Hand of Ragnaros":
            return processor_sulfuras()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return processor_backstage_pass()
        elif item.name == "Aged Brie":
            return processor_aged_brie()
        elif "Conjured" in item.name:
            return processor_conjured()
        else:
            return processor_normal()
