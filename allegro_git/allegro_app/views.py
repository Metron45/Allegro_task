from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.
def repos(request, user):
    r = requests.get('https://api.github.com/users/' + user + '/repos')
    json_response = r.json()

    response, star_sum, lang_dict = list_repositories(json_response)
    response += list_languages(lang_dict)
    response += "<br/> Sum of Stars: " + str(star_sum) + "<br/>"

    return HttpResponse(response)


def list_repositories(git_response):
    response = ""
    star_sum = 0
    lang_dict = {}
    for repo in git_response:
        response += repo["name"] + " " + str(repo["stargazers_count"]) + " "
        star_sum += repo["stargazers_count"]
        if repo["language"] is not None:
            response += repo["language"]
            if repo["language"] in lang_dict:
                lang_dict[repo["language"]] += repo["size"]
            else:
                lang_dict[repo["language"]] = repo["size"]
        response += " " + str(repo["size"])
        response += "<br/>"
    response += "<br/>"
    return response, star_sum, lang_dict


def list_languages(lang_dict):
    response = ""
    if len(lang_dict) >= 3:
        for _ in range(0, 3):
            favourite = max(lang_dict, key=lang_dict.get)
            response += favourite + " " + str(lang_dict[favourite]) + "<br/>"
            lang_dict.pop(favourite)
    else:
        for _ in range(0, len(lang_dict)):
            favourite = max(lang_dict, key=lang_dict.get)
            response += favourite + " " + str(lang_dict[favourite]) + "<br/>"
            lang_dict.pop(favourite)
    return response
