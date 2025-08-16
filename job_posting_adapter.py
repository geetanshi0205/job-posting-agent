#!/usr/bin/env python3

import os

from crewai import Crew
from dotenv import load_dotenv
from uagents_adapter import CrewaiRegisterTool

from job_posting_agents import JobPostingAgents
from job_posting_tasks import JobPostingTasks


class JobPostingCrew:
    """CrewAI crew for automated job posting creation."""
    
    def __init__(self, company_name, industry, job_title, department, experience_level, location="", additional_requirements=""):
        self.company_name = company_name
        self.industry = industry
        self.job_title = job_title
        self.department = department
        self.experience_level = experience_level
        self.location = location
        self.additional_requirements = additional_requirements

    def run(self):
        """Execute the job posting creation workflow."""
        agents = JobPostingAgents()
        tasks = JobPostingTasks()

        # Create agents
        company_research_agent = agents.company_research_agent()
        job_strategist_agent = agents.job_strategist_agent()
        content_creator_agent = agents.content_creator_agent()

        # Create tasks
        research_task = tasks.company_research_task(
            company_research_agent,
            self.company_name,
            self.industry
        )
        
        analysis_task = tasks.job_analysis_task(
            job_strategist_agent,
            self.job_title,
            self.department,
            self.experience_level,
            self.company_name
        )
        
        creation_task = tasks.job_posting_creation_task(
            content_creator_agent,
            self.job_title,
            self.company_name,
            self.location,
            self.additional_requirements
        )

        # Set task dependencies
        analysis_task.context = [research_task]
        creation_task.context = [research_task, analysis_task]

        # Create crew
        crew = Crew(
            agents=[company_research_agent, job_strategist_agent, content_creator_agent],
            tasks=[research_task, analysis_task, creation_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result

    def kickoff(self, inputs=None):
        """
        Compatibility method for uAgents integration.
        Accepts a dictionary of inputs and calls run() with them.
        """
        if inputs:
            self.company_name = inputs.get("company_name", self.company_name)
            self.industry = inputs.get("industry", self.industry)
            self.job_title = inputs.get("job_title", self.job_title)
            self.department = inputs.get("department", self.department)
            self.experience_level = inputs.get("experience_level", self.experience_level)
            self.location = inputs.get("location", self.location)
            self.additional_requirements = inputs.get("additional_requirements", self.additional_requirements)

        return self.run()


def main():
    """Main function to demonstrate Job Posting Agent with CrewAI adapter."""

    # Load API key from environment
    load_dotenv()
    api_key = os.getenv("AGENTVERSE_API_KEY")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    serper_api_key = os.getenv("SERPER_API_KEY")
    
    if not api_key:
        print("Error: AGENTVERSE_API_KEY not found in environment")
        return

    if not openai_api_key:
        print("Error: OPENAI_API_KEY not found in environment")
        return
        
    if not serper_api_key:
        print("Error: SERPER_API_KEY not found in environment")
        return

    # Set API keys in environment
    os.environ["OPENAI_API_KEY"] = openai_api_key
    os.environ["SERPER_API_KEY"] = serper_api_key

    # Create an instance of JobPostingCrew with default empty values
    job_posting_crew = JobPostingCrew("", "", "", "", "", "", "")

    # Create tool for registering the crew with Agentverse
    register_tool = CrewaiRegisterTool()

    # Define parameters schema for the job posting agent
    query_params = {
        "company_name": {"type": "str", "required": True},
        "industry": {"type": "str", "required": True},
        "job_title": {"type": "str", "required": True},
        "department": {"type": "str", "required": True},
        "experience_level": {"type": "str", "required": True},
        "location": {"type": "str", "required": False},
        "additional_requirements": {"type": "str", "required": False},
    }

    # Register the crew with parameter schema
    result = register_tool.run(
        tool_input={
            "crew_obj": job_posting_crew,
            "name": "Job Posting Agent",
            "port": 8001,
            "description": "A Job Posting Agent that creates comprehensive job postings using company research, job analysis, and content creation specialists",
            "api_token": api_key,
            "mailbox": True,
            "query_params": query_params,
            "example_query": "Create a job posting for TechCorp in the Technology industry for a Senior Software Engineer position in the Engineering department requiring 5+ years experience, remote work in San Francisco, with Python and AI/ML background preferred.",
        }
    )

    # Get the agent address from the result
    if isinstance(result, dict) and "address" in result:
        agent_address = result["address"]
        print(f"Agent registered with address: {agent_address}")

    print(f"\nJob Posting Agent registration result: {result}")

    # Keep the program running
    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting...")


if __name__ == "__main__":
    main()