from django.forms import ModelForm 
from lab_management.models import Test

class TestForm(ModelForm):
    class Meta:
        model = Test
        exclude = ('created_at', 'deleted_at', 'is_deleted','updated_at')
        
