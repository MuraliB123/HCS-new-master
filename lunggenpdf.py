from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import random

def generate_sample_medical_report(gender, age, smoking, yellow_fingers, anxiety_mean, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol_consumption, coughing, shortness_of_breath, swallowing_difficulty, chest_pain):
    # Create a PDF document
    c = canvas.Canvas("sample_medical_report_lung.pdf", pagesize=letter)

    # Set font styles
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1 * inch, 10.5 * inch, "Medical Report")

    # Add a line separator
    c.setStrokeColorRGB(0, 0, 0)
    c.line(1 * inch, 10.25 * inch, 7.5 * inch, 10.25 * inch)

    # Add patient details
    c.setFont("Helvetica", 12)
    details = [
        ("Gender:", str(gender)),
        ("Age:", str(age)),
        ("Smoking:", str(smoking)),
        ("Yellow Fingers:", str(yellow_fingers)),
        ("Anxiety Mean:", str(anxiety_mean)),
        ("Peer Pressure:", str(peer_pressure)),
        ("Chronic Disease:", str(chronic_disease)),
        ("Fatigue:", str(fatigue)),
        ("Allergy:", str(allergy)),
        ("Wheezing:", str(wheezing)),
        ("Alcohol Consumption:", str(alcohol_consumption)),
        ("Coughing:", str(coughing)),
        ("Shortness of Breath:", str(shortness_of_breath)),
        ("Swallowing Difficulty:", str(swallowing_difficulty)),
        ("Chest Pain:", str(chest_pain))
    ]
    y_position = 9.5 * inch
    for label, value in details:
        c.drawString(1 * inch, y_position, label)
        c.drawString(2.5 * inch, y_position, value)
        y_position -= 0.35 * inch

    # Save the PDF document
    c.save()

if __name__ == "__main__":
    # Replace the following values with the desired sample data
    gender = 1
    age = 35
    smoking = 0.5
    yellow_fingers = 0.2
    anxiety_mean = 4.7
    peer_pressure = 3.2
    chronic_disease = 0.1
    fatigue = 5
    allergy = 1
    wheezing = 2
    alcohol_consumption = 3
    coughing = 2
    shortness_of_breath = 1
    swallowing_difficulty = 0
    chest_pain = 0

    generate_sample_medical_report(
        gender, age, smoking, yellow_fingers, anxiety_mean, peer_pressure,
        chronic_disease, fatigue, allergy, wheezing, alcohol_consumption,
        coughing, shortness_of_breath, swallowing_difficulty, chest_pain
    )
