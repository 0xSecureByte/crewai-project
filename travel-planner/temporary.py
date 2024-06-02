import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# Set up environment variables for API keys
os.environ["SERPER_API_KEY"] = "Your_SerperDev_API_Key"

# Define the SerperDevTool
research_tool = SerperDevTool()

# Define the Travel Researcher Agent
travel_researcher = Agent(
    role='Travel Researcher',
    goal='Gather information on travel destinations and attractions.',
    verbose=True,
    memory=True,
    backstory="You have a passion for exploring new places and finding hidden gems.",
    tools=[research_tool],
    allow_delegation=True
)

# Define the Travel Itinerary Planner Agent
itinerary_planner = Agent(
    role='Travel Itinerary Planner',
    goal='Organize travel details into a basic itinerary.',
    verbose=True,
    memory=True,
    backstory="You excel at organizing and planning, ensuring every detail is accounted for.",
    tools=[],
    allow_delegation=False
)

# Define the Research Destinations Task
research_task = Task(
    description=(
        "Identify potential travel destinations based on user preferences. "
        "Your final report should include top recommendations and highlights."
    ),
    expected_output='A list of top 3 travel destinations with highlights.',
    tools=[research_tool],
    agent=travel_researcher,
)

# Define the Plan Itinerary Task
itinerary_task = Task(
    description=(
        "Create a simple day-by-day plan including top attractions. "
        "Ensure the itinerary is enjoyable."
    ),
    expected_output='A simple travel itinerary.',
    tools=[],
    agent=itinerary_planner,
)

# Assemble the Crew
crew = Crew(
    agents=[travel_researcher, itinerary_planner],
    tasks=[research_task, itinerary_task],
    process=Process.sequential
)

# Kick Off the Process
result = crew.kickoff(inputs={'user_preferences': 'beach destinations'})
print(result)
