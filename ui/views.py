from django.http import HttpResponse
from django.shortcuts import render

from .utils import extract_mcqs_from_pdf
from .models import MCQ

# Create your views here.
def home(request):
    return render(request, "home.html")

def upload_mcq(request):
    if request.method == "POST" and request.FILES.get("pdf"):
        pdf_file = request.FILES["pdf"]
        mcqs = extract_mcqs_from_pdf(pdf_file)

        for mcq in mcqs:
            MCQ.objects.create(
                question=mcq["question"],
                option_a=mcq["option_a"],
                option_b=mcq["option_b"],
                option_c=mcq["option_c"],
                option_d=mcq["option_d"],
                correct_answer=mcq["correct_answer"]
            )
        return render(request, "success.html")

    return render(request, "upload.html")