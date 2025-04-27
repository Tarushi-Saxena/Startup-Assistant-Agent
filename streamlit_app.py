# streamlit_app.py

import streamlit as st
import os
import warnings
from datetime import datetime

# Suppress warnings
warnings.filterwarnings('ignore')

# Imports
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from pydantic import BaseModel
from google.generativeai import configure

# Setup environment
GEMINI_API_KEY = "AIzaSyAKe3fdi3uTIcsciS0hoaPB3KkuhnthACY"
SERPER_API_KEY = "8d602abe0f5ebb126d553632d467ef66c73b318f"

os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY
os.environ["SERPER_API_KEY"] = SERPER_API_KEY
os.environ["GEMINI_MODEL_NAME"] = "gemini-1.5-flash"

configure(api_key=os.environ["GEMINI_API_KEY"])

# Initialize LLM
llm = LLM(model="gemini/gemini-1.5-flash")

# Initialize tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# Define Agents
market_research_analyst = Agent(
    role="Market Research Analyst",
    goal="Analyze startup market trends, identify niche opportunities and assess competitors",
    backstory="You're an expert in finding valuable market insights.",
    llm=llm,
    tools=[search_tool, scrape_tool],
    verbose=True
)

idea_brainstormer = Agent(
    role="Idea Brainstormer",
    goal="Generate startup ideas based on niche input.",
    backstory="Creative expert for startup ideation.",
    llm=llm,
    verbose=True
)

lean_canvas_builder = Agent(
    role="Lean Canvas Builder",
    goal="Auto-create business models for validation.",
    backstory="Helps in building structured lean canvases quickly.",
    llm=llm,
    verbose=True
)

pitch_generator = Agent(
    role="Pitch Generator",
    goal="Generate a compelling startup pitch.",
    backstory="Expert in startup pitches for investors.",
    llm=llm,
    verbose=True
)

brand_strategist = Agent(
    role="Brand Strategist",
    goal="Suggest names, slogans, and visual identity concepts.",
    backstory="Branding expert for memorable startups.",
    llm=llm,
    verbose=True
)

content_assistant = Agent(
    role="Content Assistant",
    goal="Suggest blog posts, product descriptions, and social media content.",
    backstory="Helps in content creation for marketing.",
    llm=llm,
    verbose=True
)

operations_strategist = Agent(
    role="Startup Operations Strategist",
    goal="Manage operations for startups.",
    backstory="Efficient in setting up tools and workflows.",
    llm=llm,
    tools=[search_tool, scrape_tool],
    verbose=True
)

# Define Tasks
class ProjectDetails(BaseModel):
    name: str
    description: str
    stage: str
    team_size: int
    status: str

def create_tasks(project_input):
    project_task = Task(
        description="Gather all necessary details for startup {project_name}.",
        expected_output="Startup project details.",
        human_input=True,
        output_json=ProjectDetails,
        agent=operations_strategist
    )

    idea_task = Task(
        description="Generate startup ideas based on the niche {niche_input}.",
        expected_output="List of startup ideas.",
        human_input=True,
        agent=idea_brainstormer
    )

    market_research_task = Task(
        description="Analyze market trends, competitors for {project_name}.",
        expected_output="Detailed market research report.",
        human_input=True,
        agent=market_research_analyst
    )

    lean_canvas_task = Task(
        description="Auto-generate a Lean Canvas for {project_name}.",
        expected_output="Complete Lean Canvas model.",
        human_input=True,
        agent=lean_canvas_builder
    )

    pitch_task = Task(
        description="Create a compelling startup pitch for {project_name}.",
        expected_output="Investor pitch deck.",
        human_input=True,
        output_file="pitch.md",
        agent=pitch_generator
    )

    brand_task = Task(
        description="Generate brand name, slogan, and identity for {project_name}.",
        expected_output="Branding strategy.",
        human_input=True,
        agent=brand_strategist
    )

    content_task = Task(
        description="Generate marketing content for {project_name}.",
        expected_output="Blog posts, product descriptions, social posts.",
        human_input=True,
        agent=content_assistant
    )

    operations_task = Task(
        description="Create an operations strategy for {project_name}.",
        expected_output="Detailed operational strategy.",
        human_input=True,
        agent=operations_strategist
    )

    return [
        project_task, idea_task, market_research_task, lean_canvas_task,
        pitch_task, brand_task, content_task, operations_task
    ]

def generate_startup_assistant(inputs):
    tasks = create_tasks(inputs)

    startup_assistant_agent = Crew(
        agents=[market_research_analyst, idea_brainstormer, lean_canvas_builder,
                pitch_generator, brand_strategist, content_assistant, operations_strategist],
        tasks=tasks,
        verbose=True
    )

    result = startup_assistant_agent.kickoff(inputs=inputs)
    return result

# Streamlit App UI
st.set_page_config(page_title="Startup Assistant Agent", page_icon="🚀")
st.title("🚀 Startup Assistant Agent")

st.markdown("**Fill out your startup project details:**")

project_name = st.text_input("Project Name")
project_description = st.text_area("Project Description")
project_city = st.text_input("City")
tentative_launch_date = st.date_input("Tentative Launch Date", value=datetime.today())
expected_team_size = st.number_input("Expected Team Size", min_value=1)
budget = st.number_input("Budget ($)", min_value=0)
business_model = st.text_input("Business Model (e.g., SaaS, E-commerce)")
niche_input = st.text_input("Niche (example: AI tools for startup founders)")

if st.button("🚀 Generate My Startup Plan"):
    if project_name and project_description:
        startup_project_details = {
            'project_name': project_name,
            'project_description': project_description,
            'project_city': project_city,
            'tentative_launch_date': tentative_launch_date.strftime("%Y-%m-%d"),
            'expected_team_size': expected_team_size,
            'budget': budget,
            'business_model': business_model,
            'niche_input': niche_input
        }

        with st.spinner('Building your startup assistant report...'):
            result = generate_startup_assistant(startup_project_details)

        st.success("🚀 Your startup plan is ready!")
        st.markdown("### Final Output:")
        st.markdown(result.raw)
    else:
        st.warning("⚠️ Please fill at least Project Name and Description!")
