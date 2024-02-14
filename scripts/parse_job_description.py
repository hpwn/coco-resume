import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set the API key for the OpenAI API calls
openai.api_key = openai_api_key


# Define the function to call the OpenAI API using GPT-3
def gpt3_call(prompt, engine="davinci", max_tokens=100):
    response = openai.Completion.create(
        engine=engine, prompt=prompt, max_tokens=max_tokens
    )
    return response.choices[0].text.strip()


# Function to parse the job description and extract relevant skills and technologies
def parse_job_description(job_description):
    # Extract keywords related to skills, technologies, and experiences using GPT-3
    skills_prompt = f"Extract all the skills and technologies required for this job:\n\n{job_description}"
    skills = gpt3_call(skills_prompt)

    experiences_prompt = f"Extract all the experiences that would make a candidate ideal for this job:\n\n{job_description}"
    experiences = gpt3_call(experiences_prompt)

    # Return a dictionary of the parsed elements
    return {"skills": skills, "experiences": experiences}


# Example job description (replace this with the actual job description)
job_description_example = """
The ideal candidate will have experience with Python, JavaScript, and React.
Experience with cloud services like AWS and familiarity with Agile development practices is a plus.
"""

# Parse the example job description
parsed_data = parse_job_description(job_description_example)
print(parsed_data)
