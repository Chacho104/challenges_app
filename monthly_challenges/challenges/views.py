from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create a dictionary of months with their monthly challenges
monthly_challenges = {
        "january": "Eat no meat for the entire month!",
        "february": "Walk for at least 20 minutes every day!",
        "march": "Learn Django for at least 30 minutes every day!",
        "april": "Read one book every week!",
        "may": "Practice yoga for at least 15 minutes every day!",
        "june": "Drink at least 2 liters of water every day!",
        "july": "Write a journal entry every day!",
        "august": "Try a new recipe every week!",
        "september": "Spend at least 30 minutes outdoors every day!",
        "october": "Learn a new skill or hobby!",
        "november": "Practice gratitude by writing down three things you're thankful for every day!",
        "december": None
    }

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"month_list": months})

def monthly_challenge_by_number(request, month):
    # Create a list of keys (months) from the monthly_challenges dictionary
    months = list(monthly_challenges.keys())

    # Check month does not exceed length of months
    if month > len(months):
        return HttpResponseNotFound("This month is not supported. Please enter a number between 1 and 12!")

    # Use index to get redirect month - bearing in mind that lists are zero-indexed!
    redirect_month = months[month - 1]

    # Use redirects to redirect int month to respective month
    # To make it flexible, use reverse function and path name to construct the redirect_path
    redirect_path = reverse("monthly-challenge", args=[redirect_month])

    # Now you can return the flexible redirect path - no hard-coded path!
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        return render(request, "challenges/challenge.html", {"month": month, "text": challenge_text})
    except:
        return HttpResponseNotFound("<h1>This month is not a valid challenge month. Please try again.</h1>")
