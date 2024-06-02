from django.shortcuts import render
from django.http import HttpResponse
from travel_agents import TravelAgents
from travel_tasks import TravelTasks
from main import TravelCrew

def plan_travel(request):
    if request.method == 'POST':
        # Get form data
        origin = request.POST.get('origin')
        cities = request.POST.get('cities')
        date_range = request.POST.get('date_range')
        interests = request.POST.get('interests')
        
        # Create TravelCrew instance and run
        travel_crew = TravelCrew(origin, cities, date_range, interests)
        result = travel_crew.run()
        
        # Write result to a file
        with open('travel_plan_result.docx', 'w') as file:
            file.write(result)
        
        # Render result template with the result
        return render(request, 'result.html', {'result': result})
    else:
        # Render home template for GET requests
        return render(request, 'home.html')
