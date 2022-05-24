from django.db import models
from .game import Game
from .gamer import Gamer


class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=12)
    date = models.DateField()
    time = models.TimeField()
    organizer = models.ForeignKey(Gamer, on_delete=models.DO_NOTHING)
