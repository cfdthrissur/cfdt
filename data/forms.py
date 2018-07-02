from django import forms


class DataForm01(forms.Form):
    lsgd_name = forms.CharField(max_length=100)
    lsgd_year_of_formation = forms.IntegerField()
    lsgd_area_in_sqkm = forms.FloatField()

