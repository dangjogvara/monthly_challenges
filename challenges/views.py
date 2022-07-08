from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
        return HttpResponse(challenge_text)
    except:
        return HttpResponse("This month is not supported!")
