from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

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
    "december": None
}


# Return list of challenges
def index(request):
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {
        'months': months
    })


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
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            'month_name': month

        })

    except:
        return HttpResponse("<h1>This month is not supported!</h1>")
