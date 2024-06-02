# import os
from crewai import Crew
from textwrap import dedent
from travel_agents import TravelAgents
from travel_tasks import TravelTasks

# OPENAI_API_KEY = os.getenv['OPENAI_API_KEY'] # Set your OpenAI API Key here

class TravelCrew:

  def __init__(self, origin, cities, date_range, interests):
    self.cities = cities
    self.origin = origin
    self.interests = interests
    self.date_range = date_range

  def run(self):
    agents = TravelAgents()
    tasks = TravelTasks()

    city_selector_agent = agents.city_selection_agent()
    local_expert_agent = agents.local_expert()
    travel_concierge_agent = agents.travel_concierge()

    identify_task = tasks.identify_task(
      city_selector_agent,
      self.origin,
      self.cities,
      self.interests,
      self.date_range
    )
    gather_task = tasks.gather_task(
      local_expert_agent,
      self.origin,
      self.interests,
      self.date_range
    )
    plan_task = tasks.plan_task(
      travel_concierge_agent, 
      self.origin,
      self.interests,
      self.date_range
    )

    crew = Crew(
      agents=[
        city_selector_agent, local_expert_agent, travel_concierge_agent
      ],
      tasks=[identify_task, gather_task, plan_task],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("----------> Welcome to Travel Planner Crew <----------")
  print('------------------------------------------------------')
  location = input(
    dedent("""
      Your current city ?
    """))
  cities = input(
    dedent("""
      What cities you like to visit in your travel?
    """))
  date_range = input(
    dedent("""
      On which date will you travel and when will you complete the travel(Use this format: DD/MM/YYYY - DD/MM/YYYY)?
    """))
  interests = input(
    dedent("""
      Describe some of your high level interests and hobbies which are related to the travelling?
    """))
  
  travel_crew = TravelCrew(location, cities, date_range, interests)
  result = travel_crew.run()
  print("\n\n<<<----------------------------------------------------------------------->>>")
  print("                             Here is you Travel Plan                            ")
  print("<<<----------------------------------------------------------------------->>>\n")
  print(result)
