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
    lsgd_no_of_rivers = forms.IntegerField(required = False)
    lsgd_name_of_rivers = forms.CharField(max_length = 200, required = False)
    lsgd_coastal_line_length_in_km = forms.IntegerField(required = False)
    lsgd_forest_area_in_hectors = forms.FloatField(required = False)
    lsgd_type_of_soil = forms.CharField(max_length = 100, required = False)
    lsgd_main_roads = forms.CharField(max_length = 200, required = False)
    lsgd_nearest_railway_station = forms.CharField(max_length = 100, required = False)
    lsgd_jilla_panchayath_name = forms.CharField(max_length = 100, required = False)
    lsgd_jilla_panchayath_ward = forms.IntegerField(required = False)
    lsgd_block_panchayath_name = forms.CharField(max_length = 100, required = False)
    lsgd_block_panchayath_wards = forms.CharField(max_length = 100, required = False)
    

