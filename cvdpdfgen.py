from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import random

def generate_sample_medical_report(name, age, gender, chest_pain_type, bp, bc, bsugar,ecg,heartrate,ex_ind_angina,old_peak,slope,no_vessels_colored,thal):
    # Create a PDF document
    c = canvas.Canvas("cvd_sample_medical_report.pdf", pagesize=letter)

    # Set font styles
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1 * inch, 10.5 * inch, "Medical Report")

    # Add a line separator
    c.setStrokeColorRGB(0, 0, 0)
    c.line(1 * inch, 10.25 * inch, 7.5 * inch, 10.25 * inch)

    # Add patient details
    c.setFont("Helvetica", 12)
    details = [
        ("Name:", name),
        ("Age:", str(age)),
        ("Gender:", str(gender)),
        ("Chest pain type:", str(chest_pain_type)),
        ("Resting Blood Pressure:", str(bp)),
        ("Blood Cholesterol Level:", str(bc)),
        ("Fasting Blood Sugar:", str(bsugar)),
        ("Resting ECG:", str(ecg)),
        ("Heartrate:", str(heartrate)),
        ("Exercise Induced angina:", str(ex_ind_angina)),
        ("Old peak:", str(old_peak)),
        ("Slope:", str(slope)),
        ("No.of vessels colored:", str(no_vessels_colored)),
        ("Thal:", str(thal))
    ]
    y_position = 9.5 * inch
    for label, value in details:
        c.drawString(2 * inch, y_position, label)
        c.drawString(2.5 * inch, y_position, value)
        y_position -= 0.35 * inch

    # Add a line separator
    c.line(1 * inch, 6.5 * inch, 7.5 * inch, 6.5 * inch)

    # Add a random diagnosis
    # diagnoses = ["Normal", "High Blood Pressure", "High Glucose", "High Insulin", "High BMI"]
    # random_diagnosis = random.choice(diagnoses)
    # c.setFont("Helvetica-Bold", 14)
    # c.drawString(1 * inch, 6.2 * inch, "Diagnosis:")
    # c.setFont("Helvetica", 12)
    # c.drawString(1.5 * inch, 5.8 * inch, random_diagnosis)

    # Save the PDF document
    c.save()

if __name__ == "__main__":
    # Replace the following values with the desired sample data
    name = "Arsh Singh"
    age = 63
    gender = 1
    chest_pain_type = 3
    bp = 145
    bc = 233
    bsugar = 1
    ecg = 0
    heartrate = 150
    ex_ind_angina = 0
    old_peak = 2.3
    slope = 0
    no_vessels_colored = 0
    thal = 1

    generate_sample_medical_report(name, age, gender, chest_pain_type, bp, bc, bsugar,ecg,heartrate,ex_ind_angina,old_peak,slope,no_vessels_colored,thal)
