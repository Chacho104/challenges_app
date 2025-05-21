from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
        "december": "Reflect on the year and set goals for the next year!"
    }

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        # Capitalize moth for link label
        capitalized_month = month.capitalize()

        # Create dynamic path using reverse function
        month_path = reverse("monthly-challenge", args=[month])

        # Generate a list of a tag and add to list items
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"""
        <h1>Click on a month to reveal the challenge:</h1>
        <ul>{list_items}</ul>
    """

    return HttpResponse(response_data)

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
    # challenge_text = monthly_challenges.get(month.lower(), "This month is not a valid challenge month. Please try again.")
    # return HttpResponse(challenge_text)
    try:
        challenge_text = monthly_challenges[month.lower()]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not a valid challenge month. Please try again.</h1>")
