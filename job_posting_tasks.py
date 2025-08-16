from crewai import Task


class JobPostingTasks:
    """Class to define all tasks for job posting creation."""

    def company_research_task(self, agent, company_name, industry):
        """Task for researching company and industry information."""
        return Task(
            description=f"""
            Conduct comprehensive research on {company_name} in the {industry} industry.
            
            Your research should include:
            1. Company overview and history
            2. Mission, vision, and core values
            3. Company culture and work environment
            4. Recent news, achievements, and developments
            5. Industry position and competitive landscape
            6. Employee benefits and perks (if available)
            7. Company size and growth trajectory
            8. Notable clients or projects
            9. Leadership team and company structure
            10. Any unique selling points or differentiators
            
            Use web search to gather the most current and accurate information.
            Focus on information that would be relevant for attracting potential job candidates.
            """,
            agent=agent,
            expected_output="""A comprehensive company research report containing:
            - Company overview and background
            - Culture and values analysis
            - Industry position and competitive advantages
            - Recent developments and achievements
            - Key differentiators that would appeal to job candidates
            - Workplace environment and employee benefits information""",
        )

    def job_analysis_task(self, agent, job_title, department, experience_level, company_name):
        """Task for analyzing job requirements and creating detailed job specifications."""
        return Task(
            description=f"""
            Based on the company research, create a comprehensive analysis for the {job_title} position 
            in the {department} department at {company_name}.
            
            Your analysis should include:
            1. Core responsibilities and daily tasks
            2. Required technical skills and qualifications
            3. Required soft skills and personal attributes
            4. Minimum experience level: {experience_level}
            5. Preferred qualifications and nice-to-have skills
            6. Key performance indicators and success metrics
            7. Career growth opportunities
            8. How this role fits into the company's organizational structure
            9. Collaboration requirements with other teams/departments
            10. Any specific industry knowledge or certifications needed
            
            Ensure the requirements are realistic and aligned with the experience level specified.
            """,
            agent=agent,
            expected_output="""A detailed job analysis document containing:
            - Comprehensive list of responsibilities and tasks
            - Required and preferred qualifications
            - Technical and soft skills requirements
            - Experience level specifications
            - Performance expectations and success metrics
            - Career development opportunities
            - Team collaboration requirements""",
        )

    def job_posting_creation_task(self, agent, job_title, company_name, location, additional_requirements):
        """Task for creating the final job posting content."""
        return Task(
            description=f"""
            Create a compelling and comprehensive job posting for the {job_title} position at {company_name}.
            
            The job posting should include:
            1. An attention-grabbing job title and summary
            2. Engaging company overview highlighting culture and values
            3. Detailed role description with key responsibilities
            4. Clear requirements (required vs. preferred)
            5. Skills and qualifications needed
            6. What we offer (benefits, growth opportunities, work environment)
            7. Location information: {location}
            8. Additional requirements: {additional_requirements}
            9. Application process and next steps
            10. Equal opportunity statement
            
            Writing guidelines:
            - Use an engaging and professional tone
            - Make it appealing to top talent
            - Be specific about expectations
            - Highlight unique company benefits and culture
            - Keep it well-structured and easy to read
            - Include keywords relevant to the role for searchability
            """,
            agent=agent,
            expected_output="""A complete, professional job posting ready for publication containing:
            - Compelling job title and summary
            - Engaging company description
            - Detailed role responsibilities
            - Clear requirements and qualifications
            - Benefits and opportunities offered
            - Location and work arrangement details
            - Application instructions
            - Professional formatting and structure
            The posting should be 500-800 words and ready to publish on job boards.""",
        )