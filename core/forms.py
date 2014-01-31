from app.libr import KOModelForm
from core.models import Party, Employee


class PartyForm(KOModelForm):
    class Meta:
        model = Party


class EmployeeForm(KOModelForm):
    class Meta:
        model = Employee