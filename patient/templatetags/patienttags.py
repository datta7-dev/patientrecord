from patient.models import Patient
from django import template
register = template.Library()


# tag to count the total numbe of patients
@register.simple_tag(name="patient_count")
def patient_count():
    # print(Patient.objects.count())
    return Patient.objects.count()
