from django.db import models
from .gamer import Gamer
from .game_type import GameType


class Game(models.Model):
    game_type = models.ForeignKey(GameType, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=55)
    maker = models.CharField(max_length=12)
    gamer = models.ForeignKey(Gamer, on_delete=models.DO_NOTHING)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
