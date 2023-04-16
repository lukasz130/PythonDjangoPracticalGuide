from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


monthly_challenges = {
    "january": "Eat no meat for entire month!",
    "february": "Walk at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for entire month!",
    "may": "Walk at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for entire month!",
    "august": "Walk at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for entire month!",
    "november": "Walk at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!",
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month.")
    redirect_mouth = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_mouth])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This mount is not supported!")
