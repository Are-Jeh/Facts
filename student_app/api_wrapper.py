import os
import requests
from django.conf import settings

class FactsAPIWrapper:
    BASE_URL = "https://api.factsmgt.com"

    def __init__(self):
        self.headers = {
            "Ocp-Apim-Subscription-Key": settings.FACTS_API_KEY,
            "Content-Type": "application/json",
        }
        self.api_version = settings.FACTS_API_VERSION

    def fetch_family_members(self):
        url = f"{self.BASE_URL}/People/ParentStudent"
        response = requests.get(url, headers=self.headers, params={"api-version": self.api_version})
        response.raise_for_status()
        family_data = response.json()
        return family_data.get("results", [])

    def identify_students(self, family_data):
        student_ids = [member['studentID'] for member in family_data if member.get('studentID')]
        return student_ids

    def fetch_student_details(self, student_ids):
        student_details = []
        for student_id in student_ids:
            url = f"{self.BASE_URL}/People/{student_id}/Demographic"
            response = requests.get(url, headers=self.headers, params={"api-version": self.api_version})
            if response.status_code == 200:
                student_details.append(response.json())
        return student_details
