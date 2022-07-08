from ast import arg
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Run a 5k in the month of January",
    "february": "Run a 10k in the month of February",
    "march": "Sleep 8 hours in the month of March",
    "april": "Learn Django in the month of April",
    "may": "Eat meat",
    "june": "Stop eating meat",
    "july": "Run a 15k in the month of July",
    "august": "School starts in the month of August",
    "september": "Final exam in the month of September",
    "october": "Run a 20k in the month of October",
    "november": "Learn Python in the month of November",
    "december": "Finish Django in the month of December"
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponse("<h1>This month is not supported!</h1>")
