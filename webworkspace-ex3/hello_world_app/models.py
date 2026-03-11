from django.db import models
from datetime import date

# class Score(models.Model):
#     name = models.CharField(max_length=100)
#     value = models.IntegerField()

#     def __str__(self):
# 	    return f'{self.name}: {self.value}'

class Games(models.Model):
    date = models.DateField(default=date.today())
    player1_score = models.IntegerField()
    player2_score = models.IntegerField()
    player1_name = models.CharField(max_length=100)
    player2_name = models.CharField(max_length=100)
    winner = models.CharField(max_length=100, default="player1")

    def __str__(self):
        return f'Game ID: {self.id}\n{self.player1_name} score: {self.player1_score} \n{self.player2_name} score: {self.player2_score}'
