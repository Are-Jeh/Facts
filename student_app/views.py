from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .api_wrapper import FactsAPIWrapper

def fetch_student_details_view(request):
    facts_api = FactsAPIWrapper()
    # Step 1: Fetch family members
    family_data = facts_api.fetch_family_members()
    # Step 2: Identify students
    student_ids = facts_api.identify_students(family_data)
    # Step 3: Fetch student details
    student_details = facts_api.fetch_student_details(student_ids)
    return JsonResponse(student_details, safe=False)
