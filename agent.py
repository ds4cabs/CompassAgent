'''
Agent App
'''

import os
from dotenv import load_dotenv
from google import genai
from NIHRePORTER import find_pi_labs_nih
from oews import get_owes_salary
from usajobs import search_jobs_usajobs
from ONET import search_onset_skill

load_dotenv()

def generate_briefing(skills: list, location: str)->str:
    '''
    skills: Helps for finding a certain occupation
    location: A place where the job is located
    '''

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    chat = client.chats.create(
        model="gemini-3.1-flash-lite",
        config={
            "tools": [find_pi_labs_nih, get_owes_salary, search_jobs_usajobs, search_onset_skill],

        }

    )

    '''
    Command Prompt
    '''

    prompt = f"""
    A user has these skills based on their CV: {skills}.
    They are interested in jobs located in {location}.
    Please generate a career briefing for this person that includes the following:
    - Relevant job openings based on their skills and location
    - Occupations that match their skills, and expected salary data for those occupations
    - If their background suggests a research/academic direction, include relevant research labs and principal investigators working in related topic
    """

    print("About to send message...")
    response = chat.send_message(prompt)
    return response.text

if __name__ == "__main__":
    skills = ["python", "crispr", "cell culture", "flow cytometry", "microscopy"]
    location = "Washington, DC"
    print(generate_briefing(skills, location))