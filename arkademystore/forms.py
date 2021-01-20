from django import forms  
from arkademystore.models import ArkademyStore 
    
class ArkademyStoreForm(forms.ModelForm):  
    class Meta:  
        model = ArkademyStore
        fields = "__all__"  