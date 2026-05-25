from django.shortcuts import render, redirect
from .models import FoodItem
from django.db.models import Sum

def home(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')

        FoodItem.objects.create(
            name=name,
            calories=calories
        )

        return redirect('home')

    foods = FoodItem.objects.all().order_by('-created_at')

    total_calories = foods.aggregate(
        Sum('calories')
    )['calories__sum'] or 0

    context = {
        'foods': foods,
        'total_calories': total_calories
    }

    return render(request, 'home.html', context)


def delete_food(request, id):
    food = FoodItem.objects.get(id=id)
    food.delete()

    return redirect('home')


def reset_calories(request):
    FoodItem.objects.all().delete()

    return redirect('home')