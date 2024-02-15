from openai import OpenAI

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set the API key for the OpenAI API calls
client = OpenAI(api_key=openai_api_key)


# Define the function to call the OpenAI API using GPT-3.5-turbo
def gpt3_call(prompt, model="gpt-3.5-turbo", max_tokens=100):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens,
    )
    if response.choices:
        return response.choices[0].message.content.strip()
    else:
        return "No response generated."


# Function to parse the job description from an input file and extract relevant skills and technologies
def parse_job_description(file_path):
    with open(file_path, "r") as file:
        job_description = file.read()

    skills_prompt = f"Extract all the skills and technologies required for this job:\n\n{job_description}"
    skills = gpt3_call(skills_prompt)

    experiences_prompt = f"Extract all the experiences that would make a candidate ideal for this job:\n\n{job_description}"
    experiences = gpt3_call(experiences_prompt)

    # Return a dictionary of the parsed elements
    return {"skills": skills, "experiences": experiences}


# Location of the job description input file
job_description_file_path = "input/job_description.txt"

# Parse the job description from the input file
parsed_data = parse_job_description(job_description_file_path)
print(parsed_data)
