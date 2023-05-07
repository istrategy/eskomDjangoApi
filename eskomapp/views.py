# eskomapp/views.py
from django.shortcuts import render
from .api import search_areas, get_area_info
from datetime import datetime

def search(request):
    query = request.GET.get('q', '')
    arearesults = []

    if query:
        results = search_areas(query)
        arearesults = results['areas']
        # Filter out results without an id attribute
        arearesults = [result for result in arearesults if 'id' in result]
    else:
        arearesults = []

    context = {
        'query': query,
        'results': arearesults,
    }
    return render(request, 'eskomapp/search.html', context)


def area_info(request, area_id):
    area, events = get_area_info(area_id)

    # Convert the start and end times to datetime objects
    for event in events:
        event['start'] = datetime.fromisoformat(event['start'])
        event['end'] = datetime.fromisoformat(event['end'])

    context = {
        'area': area,
        'events': events,
    }
    return render(request, 'eskomapp/area_info.html', context)