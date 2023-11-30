from django import forms
from .models import Product
CATEGORY = (
    ('Oil Paint','Oil Paint'),
    ('Cement Paint','Cement Paint'),
    ('Distemper Paint','Distemper Paint'),
    ('Emulsion Paint','Emulsion Paint'),
    ('Whitewash','Whitewash'),
    ('Enamel Paint','Enamel Paint'),
    ('Acrylic Emulsion Paint','Acrylic Emulsion Paint'),
    ('Bituminous Paint','Bituminous Paint'),
    ('Synthetic Rubber Paint','Synthetic Rubber Paint'),
    ('Anti-Corrosion Paint','Anti-Corrosion Paint'),
    
)

class AddRecordForm(forms.ModelForm):
    # Color_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Color Name","class":"form-control"}),label="")
    # Category = forms.CharField(required=True,choices=CATEGORY,widget=forms.widgets.ChoiceWidget(attrs={"placeholder":"Category ","class":"form-control"}),label="")
    # Brand = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Brand ","class":"form-control"}),label="")
    # Color_code = forms.CharField(required=True,widget=forms.widgets.NumberInput(attrs={"placeholder":"Color Code","class":"form-control"}),label="")
    # quantity = forms.CharField(required=True,widget=forms.widgets.NumberInput(attrs={"placeholder":"Quantity","class":"form-control"}),label="")
    # price = forms.CharField(required=True,widget=forms.widgets.NumberInput(attrs={"placeholder":"Price","class":"form-control"}),label="")
    
    class Meta:
        model = Product
        fields = '__all__'

class StockSearchForm(forms.ModelForm):
   class Meta:
     model = Product
     fields = ['Category','Brand',]