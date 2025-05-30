from crewai import Agent, Task, Crew, LLM
from crewai.tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

# Topic to research
topic = 'medical industry using generative AI'

# Tool: LLM
llm = LLM(model="gpt-4")

# Tool: Search Tool
search_tool = SerperDevTool(n=10)

# Agent: Senior Research Analyst
senior_research_analyst = Agent(
    role="Senior Research Analyst",
    goal="Research, analyze, and synthesize data on {topic}how the medical industry is using generative AI.",
    backstory=(
        "With over 15 years of experience in the healthcare and life sciences sectors, "
        "the Senior Research Analyst has led numerous strategic initiatives at the intersection "
        "of medicine, data science, and emerging technologies. Having worked with top hospitals, "
        "biotech firms, and AI startups, they possess deep domain knowledge in clinical workflows, "
        "medical imaging, drug discovery, and patient data management. Passionate about innovation, "
        "they are known for translating complex technical trends into actionable insights for "
        "executives and policymakers. Their recent focus has been on how generative AI is revolutionizing "
        "healthcare—from accelerating diagnoses to personalizing treatment plans and streamlining research operations."
    ),
    tools=[search_tool],
    allow_delegation=False
    llm=llm,
    verbose=True
)


# Agent: Content Writer
content_writer = Agent(
    role="Content Writer",
    goal="Transform research findings into engaging, accessible, and well-structured blog posts while ensuring factual accuracy and clarity.",
    backstory=(
        "A seasoned writer and editor with a decade of experience creating high-impact content for tech and healthcare publications. "
        "Specialized in translating complex research into compelling narratives that resonate with both expert and general audiences. "
        "Having collaborated with researchers, startups, and major healthcare institutions, this writer knows how to blend storytelling "
        "with technical accuracy. Their work is known for clarity, depth, and the ability to engage readers with diverse backgrounds."
    ),
    allow_delegation=False,
    llm=llm,
    verbose=True
)


# Task: Research the topic
research_task = Task(
    description=f"Conduct thorough research and provide insights on: {topic}.",
    agent=senior_research_analyst,
    expected_output="A detailed summary of how generative AI is being applied in the medical industry, including examples and trends."
)

