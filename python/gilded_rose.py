# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_expired_item(self, item):
        if item.sell_in < 0:
            item_name = item.name.lower()
            if item_name == "aged brie" and item.quality < 50:
                item.quality = item.quality + 1
            elif "backstage passes" in item_name:
                item.quality = 0
            elif not "sulfuras" in item_name and item.quality > 0:
                item.quality = item.quality - 1
                if "" in item_name and item.quality > 0:
                    item.quality = item.quality - 1

    def calculate_sell_in(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1

    def decrease_quality(self, item):
        item_name = item.name.lower()
        if item.quality > 0:
            if item.quality - 1 > 0 and "conjured" in item_name:
                item.quality = item.quality - 1  
            item.quality = item.quality - 1  

    def increase_quality(self, item):
        item_name = item.name.lower()
        if item.quality < 50:
            item.quality = item.quality + 1
            if "backstage passes" in item_name:
                if item.sell_in < 11 and  item.quality < 50:
                    item.quality = item.quality + 1
                    if item.sell_in < 6 and item.quality < 50:
                        item.quality = item.quality + 1

    def calculate_quality(self, item):
        item_name = item.name.lower()
        if "aged brie" in item_name or "backstage passes" in item_name:
            self.increase_quality(item)
        elif not "sulfuras" in item_name:
            self.decrease_quality(item)         

    def update_quality(self):
        for item in self.items:
            self.calculate_quality(item)
            self.calculate_sell_in(item)
            self.update_expired_item(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
