from django.db.models import Q
from .models import Profile, Skill

def searchProfiles(request):
    search_query = '' 

    #if anything is entered into search box
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains = search_query)
    
    #filter profiles by search query
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains = search_query) | 
        Q(short_intro__icontains = search_query) |
        Q(skill__in=skills))

    return profiles, search_query