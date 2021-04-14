from django.shortcuts import render
from sightings.models import squirrel_data

def map(request):
    map_squirrel = squirrel_data.objects.all()[:100]
    return render(request,'map/map.html',{"map_squirrel":map_squirrel})
.
