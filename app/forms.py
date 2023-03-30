from django import forms

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#CCC'}))

class SignatureForm(forms.Form):
    signature = JSignatureField()