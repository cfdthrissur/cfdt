from django import forms


class DataForm01(forms.Form):
    lsgd_name = forms.CharField(max_length=100)
    lsgd_year_of_formation = forms.IntegerField(required = False)
    lsgd_area_in_sqkm = forms.FloatField(required = False)
    lsgd_taluk_name = forms.CharField(max_length = 100, required = False)
    lsgd_block_name = forms.CharField(max_length = 100, required = False)
    lsgd_parliamentary_constituency = forms.CharField(max_length = 100, required = False) 
    lsgd_assembly_constituency = forms.CharField(max_length = 100, required = False)
    lsgd_no_of_wards = forms.IntegerField(required = False)
    lsgd_no_of_female_wards = forms.IntegerField(required = False)
    lsgd_no_of_scst_wards = forms.IntegerField(required = False)

