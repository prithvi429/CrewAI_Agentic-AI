import streamlit as st
from dotenv import load_dotenv
import os
from crewai import Agent, Task, Crew, LLM
from crewai_tools.tools.serper import SerperTool

# Load environment variables
load_dotenv()
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# Setup LLM
llm = LLM(model="gpt-4")

# Setup search tool
search_tool = SerperTool(api_key=SERPER_API_KEY)

# Define agents
def create_agents():
    research_analyst = Agent(
        role="Senior Research Analyst",
        goal="Research and analyze how the medical industry uses generative AI.",
        backstory=(
            "With 15+ years in healthcare and life sciences, the analyst excels at identifying trends in AI's medical use."
        ),
        tools=[search_tool],
        allow_delegation=False,
        llm=llm
    )

    writer = Agent(
        role="Content Writer",
        goal="Create a clear, engaging blog post about how generative AI is transforming the medical industry.",
        backstory=(
            "An expert writer with a knack for explaining complex topics in accessible language."
        ),
        allow_delegation=False,
        llm=llm
    )

    return research_analyst, writer

# Define tasks
def create_tasks(topic, analyst, writer):
    research_task = Task(
        description=f"""Conduct detailed research on: '{topic}'.
        Focus on:
        - Applications of generative AI (e.g., medical imaging, drug discovery)
        - Benefits to patients and healthcare professionals
        - Challenges and ethical issues
        - Leading companies and institutions
        - Future trends""",
        agent=analyst,
        expected_output="A structured research report (500–800 words) with examples and citations."
    )

    content_task = Task(
        description=f"""Using the research report, write a polished blog post titled: 
        'How Generative AI Is Revolutionizing the Medical Industry'.""",
        agent=writer,
        expected_output="A blog post (700–900 words) that's well-organized, clear, and engaging for general readers.",
        input_tasks=[research_task]  # Ensure chaining
    )

    return research_task, content_task

# Streamlit UI
st.title("🧠 Generative AI in Healthcare Explorer")

topic = st.text_input("Enter a research topic:", "How generative AI is used in the medical industry")

if st.button("Run Research"):
    with st.spinner("Running CrewAI agents..."):

        analyst, writer = create_agents()
        research_task, content_task = create_tasks(topic, analyst, writer)

        crew = Crew(
            agents=[analyst, writer],
            tasks=[research_task, content_task],
            verbose=True
        )

        result = crew.kickoff(inputs={"topic": topic})

    st.success("Done! 🎉")
    st.markdown("### Final Blog Output")
    st.write(result)
