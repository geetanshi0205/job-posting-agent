from crewai import Agent
from crewai_tools import SerperDevTool


class JobPostingAgents:
    """Class to define all agents for job posting creation."""

    def __init__(self):
        self.search_tool = SerperDevTool()

    def company_research_agent(self):
        """Agent responsible for researching companies and industries."""
        return Agent(
            role="Company Research Specialist",
            goal="Conduct comprehensive research on companies, their culture, industry position, and competitive landscape",
            backstory="""You are an experienced business analyst with expertise in company research and industry analysis. 
            You have a keen eye for understanding organizational culture, market positioning, and competitive advantages. 
            Your research forms the foundation for creating compelling job postings that accurately reflect the company's values and appeal to the right candidates.""",
            tools=[self.search_tool],
            verbose=True,
            allow_delegation=False,
        )

    def job_strategist_agent(self):
        """Agent responsible for defining job requirements and candidate profiles."""
        return Agent(
            role="Job Requirements Strategist",
            goal="Define comprehensive job requirements, responsibilities, and ideal candidate profiles based on company needs",
            backstory="""You are a seasoned HR professional with over 10 years of experience in talent acquisition and job role definition. 
            You understand how to translate business needs into clear job requirements and can identify the key skills, experiences, 
            and qualifications that make candidates successful in specific roles.""",
            verbose=True,
            allow_delegation=False,
        )

    def content_creator_agent(self):
        """Agent responsible for creating compelling job postings."""
        return Agent(
            role="Job Posting Content Creator",
            goal="Create engaging, comprehensive, and professionally written job postings that attract top talent",
            backstory="""You are a skilled copywriter specializing in HR content and recruitment marketing. 
            You know how to craft compelling job descriptions that not only clearly communicate role requirements 
            but also sell the opportunity and company culture to potential candidates. Your writing style is 
            professional yet engaging, and you understand what motivates different types of professionals.""",
            verbose=True,
            allow_delegation=False,
        )