class Card:
    def __init__(self, number, level, force, feature):
        self.number = number
        self.level = level
        self.force = force
        self.feature = feature

class CharCardDict:
    def __init__(self):
        self.cards = {}

    def add_card(self, number, card):
        self.cards[number] = card

    def get_level(self, number):
        return self.cards[number].level

    def get_force(self, number):
        return self.cards[number].force

    def get_feature(self, number):
        return self.cards[number].feature

    def change_level(self, number, re_level):
        self.cards[number].level = re_level

    def change_force(self, number, re_force):
        self.cards[number].force = re_force

    def change_feature(self, number, re_feature):
        self.cards[number].feature = re_feature




# 카드 덱 설정
deck= CharCardDict()

import os
# 폴더 경로
numcard_folder_path='./data/numcard'
chacard_folder_path='./data/chrcard'

charfiles = os.listdir(chacard_folder_path)

for chacard in charfiles:
    card = Card()