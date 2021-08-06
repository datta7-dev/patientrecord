from django.urls import path
from patient import views
urlpatterns = [
    path("", views.PatientListView.as_view(), name="patientlist"),
    path("updatepatient/<int:id>",
         views.UpdatePatient.as_view(), name="updatepatient"),
    path("updatepatient",
         views.UpdatePatient.as_view(), name="updatepatient"),
    path("addpatient",
         views.PatientData.as_view(), name="addpatient"),
    path("patientlist",
         views.PatientListView.as_view(), name="patientlist"),
    path("deletepatient/<int:id>",
         views.DeletePatient, name="deletepatient"),

]
