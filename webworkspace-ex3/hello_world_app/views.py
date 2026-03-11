# from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Games
from .forms import GamesForm
import json

# # Score Functions
# def score_view(request):
# 	# List all scores
# 	scores = Score.objects.all()

# 	if request.method == "POST":
# 		form = ScoreForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('score_view')  # Redirect to the same page
# 	else:
# 		form = ScoreForm()

# 	return render(request, 'score_list.html', {'form': form, 'scores': scores})
# 	# return render(request, 'score_list_css.html', {'form': form, 'scores': scores})

# def edit_score(request, score_id):
# 	# Edit a specific score
# 	score = get_object_or_404(Score, id=score_id)

# 	if request.method == "POST":
# 		form = ScoreForm(request.POST, instance=score)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('score_view')
# 	else:
# 		form = ScoreForm(instance=score)

# 	return render(request, 'score_edit.html', {'form': form, 'score': score})
# 	# return render(request, 'score_edit_css.html', {'form': form, 'score': score})

# def delete_score(request, score_id):
# 	# Delete a specific score
# 	score = get_object_or_404(Score, id=score_id)
# 	score.delete()
# 	return redirect('score_view')



# Games Functions
def score_view(request):
	return render(request, 'score_view_css.html')

def games_view(request):
	# List all games
	games = Games.objects.all()

	if request.method == "POST":
		form = GamesForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/game/games_view') # Redirect to the same page
	else:
		form = GamesForm()

	return render(request, 'games_list_css.html', {'form': form, 'games': games})

def edit_game(request, game_id):
	# Edit a specific game
	game = get_object_or_404(Games, id=game_id)

	if request.method == "POST":
		form = GamesForm(request.POST, instance=game)
		if form.is_valid():
			form.save()
			return redirect('/game/games_view')
	else:
		form = GamesForm(instance=game)

	return render(request, 'games_edit_css.html', {'form': form, 'game': game})
	# return render(request, 'score_edit_css.html', {'form': form, 'score': score})

def delete_game(request, game_id):
	# Delete a specific game
	game = get_object_or_404(Games, id=game_id)
	game.delete()
	return redirect('games_view')

@csrf_exempt
def save_game(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = GamesForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
