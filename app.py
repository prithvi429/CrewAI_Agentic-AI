from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
from crewai_tools import tools
from crewai_tools.tools.serper import SerperTool
import os

load_dotenv()
api_key = os.getenv("SERPER_API_KEY")
search_tool = SerperTool(api_key=api_key)
# Topic to research
topic = 'medical industry using generative AI'

# Tool: LLM
llm = LLM(model="gpt-4")

# Tool: Search Tool
search_tool = SerperDevTool(n=10)

# Agent: Senior Research Analyst
senior_research_analyst = Agent(
    role="Senior Research Analyst",
    goal="Research, analyze, and synthesize data on how the medical industry is using generative AI.",
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
    allow_delegation=False,
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

# Task 1: Research
research_task = Task(
    description=(
        f"Conduct in-depth research on the topic: '{topic}'. Your goal is to gather, analyze, and synthesize up-to-date information "
        "on how generative AI is currently being used in the medical industry. Focus on the following key areas:\n\n"
        "1. Applications: Identify specific use cases of generative AI in medical settings (e.g., medical imaging, drug discovery, "
        "clinical decision support, personalized treatment, medical documentation, patient communication).\n"
        "2. Benefits: Highlight the advantages and impact generative AI brings to medical practitioners, patients, and healthcare systems.\n"
        "3. Challenges: Discuss current limitations, risks, or ethical concerns (e.g., data privacy, bias, regulatory compliance).\n"
        "4. Key Players: Mention notable companies, research institutions, or startups leading innovation in this space.\n"
        "5. Future Trends: Summarize expert opinions or emerging trends that may shape the future of generative AI in healthcare.\n\n"
        "Use reliable, up-to-date sources from academic literature, industry reports, and news articles. Provide citations where applicable."
    ),
    agent=senior_research_analyst,
    expected_output=(
        "A comprehensive and well-structured report (500-800 words) summarizing the state of generative AI in the medical industry. "
        "The report should be informative enough to serve as the foundation for a blog post or whitepaper."
    )
)

# Task 2: Blog Writing (Chained to Task 1)
content_writing_task = Task(
    description=(
        "Using the research summary provided by the Senior Research Analyst, write an engaging and informative blog post "
        "on how generative AI is transforming the medical industry. Your writing should:\n\n"
        "1. Begin with a strong introduction that hooks the reader and briefly introduces the topic.\n"
        "2. Explain key applications of generative AI in healthcare in a clear, non-technical way.\n"
        "3. Highlight real-world examples, benefits, and innovation leaders where possible.\n"
        "4. Address challenges and ethical considerations in a balanced tone.\n"
        "5. End with a forward-looking conclusion that reflects on the future potential of generative AI in medicine.\n\n"
        "The tone should be professional yet accessible to a broad audience, including healthcare professionals, tech enthusiasts, and policy makers. "
        "Aim for 700–900 words. Make the content blog-ready with proper structure, subheadings, and readability."
    ),
    agent=content_writer,
    expected_output="A polished, blog-ready article titled 'How Generative AI Is Revolutionizing the Medical Industry'.",
    input_tasks=[research_task]  # Ensures sequencing
)

# Create the Crew
crew = Crew(
    agents=[senior_research_analyst, content_writer],
    tasks=[research_task, content_writing_task],
    verbose=True
)

# Run the Crew
result = crew.kickoff(inputs={"topic": topic})
print(result)
