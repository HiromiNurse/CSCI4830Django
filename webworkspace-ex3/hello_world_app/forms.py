from django import forms
from .models import Games

class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = ['date', 'player1_name', 'player1_score', 'player2_name', 'player2_score']

    def save(self, commit=True):
        game = super().save(commit=False)

        if game.player1_score > game.player2_score:
            game.winner = game.player1_name

        elif game.player1_score < game.player2_score:
            game.winner = game.player2_name

        else:
            game.winner = "Draw"

        if commit:
            game.save()

        return game