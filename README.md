# Job Posting Agent 

This project wraps a Job Posting Agent in a uAgent adapter, making it accessible as a networked AI agent that can create, manage, and optimize job postings for organizations.

## Features

- **Multi-Agent Workflow**: Uses specialized agents for job requirement analysis, posting creation, and optimization
- **Job Requirement Analysis**: Analyzes company needs, role requirements, and market standards
- **Smart Job Posting Creation**: Creates compelling and accurate job postings
- **Posting Optimization**: Optimizes job postings for better visibility and candidate attraction
- **Market-Competitive Postings**: Ensures postings align with current market trends and standards
- **Networked Access**: Exposed as a uAgent for integration with other agents and systems

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Required API Keys**:
   - OpenAI API key for CrewAI agents
   - Serper API key for web search functionality
   - Agentverse API key for uAgent registration

## Usage

### Running the Agent

```bash
python job_posting_adapter.py
```

The agent will register itself on port 8001 and be available for queries through the Agentverse network.

### Query Parameters

- `company_name` (required): Name of the hiring company
- `job_title` (required): Job title or position to post
- `department` (required): Department or team
- `location` (required): Job location or remote option
- `experience_level` (required): Required experience level
- `job_type` (required): Full-time, part-time, contract, etc.
- `salary_range` (optional): Salary range for the position
- `key_responsibilities` (optional): Main job responsibilities
- `required_skills` (optional): Required technical and soft skills
- `company_culture` (optional): Company culture and values
- `benefits` (optional): Benefits and perks offered

### Example Query

```python
query = {
    "company_name": "TechCorp Inc.",
    "job_title": "Senior Software Engineer",
    "department": "Engineering",
    "location": "San Francisco, CA (Hybrid)",
    "experience_level": "5+ years",
    "job_type": "Full-time",
    "salary_range": "$120,000 - $180,000",
    "key_responsibilities": "Lead development of scalable web applications, mentor junior developers",
    "required_skills": "Python, React, AWS, Docker, Kubernetes",
    "company_culture": "Innovative, collaborative, fast-paced startup environment",
    "benefits": "Health insurance, 401k, equity, flexible PTO"
}
```

## Architecture

The adapter consists of three main components:

1. **JobPostingCrew**: Job Posting Agent implementation with specialized agents
   - Job Requirements Analyst: Analyzes role requirements and market standards
   - Job Posting Creator: Creates compelling and accurate job postings
   - Posting Optimizer: Optimizes postings for visibility and candidate attraction

2. **uAgent Wrapper**: Network interface using CrewaiRegisterTool
   - Handles parameter validation
   - Manages agent communication
   - Provides Agentverse registration

3. **Task Pipeline**: Sequential workflow for job posting creation
   - Requirements analysis → Posting creation → Optimization

## Agents

### Job Requirements Analyst
- **Role**: Job Requirements Analysis Specialist
- **Goal**: Analyze and define comprehensive job requirements and market standards
- **Tools**: Web search via Serper API for market research and competitive analysis

### Job Posting Creator
- **Role**: Job Posting Creation Expert
- **Goal**: Create compelling and accurate job postings that attract top talent
- **Expertise**: Content creation and employer branding

### Posting Optimizer
- **Role**: Job Posting Optimization Specialist
- **Goal**: Optimize job postings for maximum visibility and candidate engagement
- **Expertise**: SEO optimization and recruitment marketing

## Output

The agent returns a comprehensive job posting package including:
- Market-competitive job posting with optimized content
- Detailed job requirements and qualifications
- Compelling job description with company culture highlights
- Optimized posting for job boards and ATS systems
- Recommended posting channels and platforms
- Keywords and tags for better searchability
- Salary benchmarking and market analysis
- Candidate attraction strategies
- Interview process recommendations

## Author

**Geetanshi Goel**
- GitHub: [@geetanshi](https://github.com/geetanshi0205)
- LinkedIn: [Geetanshi Goel](https://www.linkedin.com/in/geetanshi-goel-49ba5832b/)