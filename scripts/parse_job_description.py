from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from collections import deque

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set the API key for the OpenAI API calls
client = OpenAI(api_key=openai_api_key)


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


def parse_job_description(file_path):
    with open(file_path, "r") as file:
        job_description = file.read()

    skills_prompt = f"Extract all the skills and technologies required for this job:\n\n{job_description}"
    skills = gpt3_call(skills_prompt)

    experiences_prompt = f"Extract all the experiences that would make a candidate ideal for this job:\n\n{job_description}"
    experiences = gpt3_call(experiences_prompt)

    return {
        "job_description": job_description,
        "skills": skills,
        "experiences": experiences,
    }


def update_job_data_file(data, file_path):
    # Check if the file exists and read the existing data
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            existing_data = file.read()
    else:
        existing_data = ""

    # Prepend the new data to the existing data
    new_data = json.dumps(data) + "\n" + existing_data

    # Write the updated data back to the file
    with open(file_path, "w") as file:
        file.write(new_data)


# Location of the job description input file and output file
job_description_file_path = "input/job_description.txt"
output_file_path = "output/job_data/job_data_log.txt"

# Parse the job description from the input file
parsed_data = parse_job_description(job_description_file_path)

# Update the output file with the parsed data
update_job_data_file(parsed_data, output_file_path)

print("Job data updated successfully.")
