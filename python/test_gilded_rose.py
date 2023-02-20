# -*- coding: utf-8 -*-
import unittest
import copy
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):   

    items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=16),
            ]     

    def compare_results(self, test_results, code_results):
        for index, item in enumerate(test_results):
            self.assertEqual(item.name, code_results[index].name)
            self.assertEqual(item.sell_in, code_results[index].sell_in)
            self.assertEqual(item.quality, code_results[index].quality)

    def test_update_second_day(self):
        days = 2
        items_updated = [
                        Item(name="+5 Dexterity Vest", sell_in=8, quality=18),
                        Item(name="Aged Brie", sell_in=0, quality=2),
                        Item(name="Elixir of the Mongoose", sell_in=3, quality=5),
                        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
                        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=13, quality=22),
                        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=50),
                        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=50),
                        Item(name="Conjured Mana Cake", sell_in=1, quality=12),
                        ]
        gilded_rose = GildedRose(copy.deepcopy(self.items))
        for day in range(days):
            gilded_rose.update_quality()
        self.compare_results(items_updated, gilded_rose.items)

    def test_update_third_day(self):
        days = 3
        items_updated = [
                        Item(name="+5 Dexterity Vest", sell_in=7, quality=17),
                        Item(name="Aged Brie", sell_in=-1, quality=4),
                        Item(name="Elixir of the Mongoose", sell_in=2, quality=4),
                        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
                        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=12, quality=23),
                        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=7, quality=50),
                        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=2, quality=50),
                        Item(name="Conjured Mana Cake", sell_in=0, quality=10),
                        ]
        gilded_rose = GildedRose(copy.deepcopy(self.items))
        for day in range(days):
            gilded_rose.update_quality()
        self.compare_results(items_updated, gilded_rose.items)

    def test_update_fifth_day(self):
        days = 5
        items_updated = [
                        Item(name="+5 Dexterity Vest", sell_in=5, quality=15),
                        Item(name="Aged Brie", sell_in=-3, quality=8),
                        Item(name="Elixir of the Mongoose", sell_in=0, quality=2),
                        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
                        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=25),
                        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=50),
                        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=50),
                        Item(name="Conjured Mana Cake", sell_in=-2, quality=2),
                        ]
        gilded_rose = GildedRose(copy.deepcopy(self.items))
        for day in range(days):
            gilded_rose.update_quality()
        self.compare_results(items_updated, gilded_rose.items)

    def test_update_tenth_day(self):
        days = 10
        items_updated = [
                        Item(name="+5 Dexterity Vest", sell_in=0, quality=10),
                        Item(name="Aged Brie", sell_in=-8, quality=18),
                        Item(name="Elixir of the Mongoose", sell_in=-5, quality=0),
                        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
                        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=35),
                        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=50),
                        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-5, quality=0),
                        Item(name="Conjured Mana Cake", sell_in=-7, quality=0),
                        ]
        gilded_rose = GildedRose(copy.deepcopy(self.items))
        for day in range(days):
            gilded_rose.update_quality()
        self.compare_results(items_updated, gilded_rose.items)

        
if __name__ == '__main__':
    unittest.main()


#python -m unittest test_gilded_rose.py