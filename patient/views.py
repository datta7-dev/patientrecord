from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from patient.models import Patient
# Create your views here.


# to get list of patients
class PatientListView(ListView):
    model = Patient
    template_name = "patientlist.html"


# to insert new patient data
class PatientData(View):

    # to get add patient template
    def get(self, request):
        return render(request, "addpatient.html")

    # to add new patient in patient record
    def post(self, request):
        try:
            first_name = request.POST.get("f_name")
            last_name = request.POST.get("l_name")
            email = request.POST.get("email")
            gender = request.POST.get("gender")
            age = request.POST.get("age")
            disease = request.POST.get("disease")
            doctor_name = request.POST.get("doctor_name")
            doctor_fees = request.POST.get("doctor_fees")
            medicine_start_date = request.POST.get("medicine_start_date")

            if Patient.objects.filter(email=email).exists():
                context = {
                    'msg': 'email-id must be unique'
                }
                return render(request, "addpatient.html", context)

            else:
                p = Patient(first_name=first_name, last_name=last_name, email=email, gender=gender, age=age, disease=disease,
                            doctor_name=doctor_name, doctor_fees=doctor_fees, medicine_start_date=medicine_start_date)
                p.save()

                return redirect("patientlist")
        except Exception as e:
            print(e)


# to update patient data
class UpdatePatient(View):

    def get(self, request, id):
        try:
            print(id)
            if Patient.objects.filter(id=id).exists():
                patient = Patient.objects.get(id=id)
                context = {
                    'patient': patient
                }
                return render(request, "updatepatient.html", context)
            else:
                context = {
                    'msg': 'data not found',
                    'patient_list': Patient.objects.all()
                }
                return render(request, "patientlist.html", context)
        except Exception as e:
            print(e)

    def post(self, request):
        try:
            id = request.POST.get("id")
            first_name = request.POST.get("f_name")
            last_name = request.POST.get("l_name")
            email = request.POST.get("email")
            gender = request.POST.get("gender")
            age = request.POST.get("age")
            disease = request.POST.get("disease")
            doctor_name = request.POST.get("doctor_name")
            doctor_fees = request.POST.get("doctor_fees")
            medicine_start_date = request.POST.get("medicine_start_date")

            if Patient.objects.filter(id=id).exists():
                Patient.objects.filter(id=id).update(
                    first_name=first_name, last_name=last_name, email=email, gender=gender, age=age, disease=disease, doctor_name=doctor_name, doctor_fees=doctor_fees, medicine_start_date=medicine_start_date)
                context = {
                    'msg': 'data updated successfully'
                }
                return render(request, "updatepatient.html", context)
            else:
                context = {
                    'msg': 'failed to update data'
                }
                return render(request, "updatepatient.html", context)
        except Exception as e:
            print(e)


# delete patient record
def DeletePatient(request, id):
    try:
        if request.method == "GET":
            if Patient.objects.filter(id=id).exists():
                patient = Patient.objects.get(id=id)
                patient.delete()
                return redirect("patientlist")
            else:
                context = {
                    'msg': 'data not found',
                    'patient_list': Patient.objects.all()
                }
                return render(request, "patientlist.html", context)
        else:
            return HttpResponse("<h1>Method Not Allowed</h1>")
    except Exception as e:
        print(e)
