from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from dataclasses import dataclass
# Create your views here.
@dataclass
class Stream:
    stream_plat: str
    description: str
    top_5: List


def hello_streams(request, name):
    context = {
        "name": name, 
        "streams": {"Netflix": Stream("Netflix", "Netflix is an American over-the-top media service and original programming production company. It was founded in 1997. Below are the top 5 viewed movies shown on this platform", ["My Little Pony: New Generation", "The Starling", "Grown Ups", "Intrusion", "Vivo"]),
        "HBO MAX": Stream("HBO MAX", "HBO Max is an American subscription video on demand streaming service owned by AT&T's WarnerMedia, through its WarnerMedia Direct subsidiary. The service was launched on May 27, 2020. Below are the top 5 movies shown on this platform", ["Unpregnant", "Charm City Kings", "Zack Snyder's Justice League", "Locked Down", "An American Pickle"]), 
        "Hulu": Stream("Hulu", "Hulu is an American online streaming service owned by The Walt Disney Company and Comcast. Started on October 29, 2007. Below are the top 5 movies shown on Hulu", ["Barb and Star Go To Vista Del Mar", "Dredd", "Run", "Logan Lucky", "Terminator Dark Fate"]), 
        "Disney+": Stream("Disney+", "Disney+ is an American subscription video on-demand over-the-top streaming service owned and operated by the Media and Entertainment Distribution division of The Walt Disney Company. Below are the top 5 Movies shown on Disney+.", ["Soul", "Hamilton", "Iron Man", "The Lion King", "The Toy Story"]) }
    } 
    return render(request, "details.html", context)

def streams(request):
    context = {
        "streams": ["Netflix", "HBO MAX", "Hulu", "Disney+"]
    } 
    return render(request, "streams.html", context)