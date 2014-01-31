from app.libr import KOModelForm
from core.models import Party

class PartyForm(KOModelForm):
    class Meta:
        model = Party

