from django.shortcuts import render, redirect

from qbnk.models import QuestionBank
from lsgd.models import Lsgd
from data.models import D01_GeneralDetails

from data.forms import DataForm01

# Create your views here.
def test_page(request):
    lsgd_code = 'KL008P001'
    data_entry_year = 2018

    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q01").values('question_text')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)

    questions_list = []
    for q in questions_queryset:
        questions_list.append(q['question_text'])

    if request.method == 'POST':
        #return render(request, 'r2n2/index.html')
        data_form01 = DataForm01(request.POST)
        data01 = D01_GeneralDetails()
        if data_form01.is_valid():
            data01.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data01.lsgd_name = data_form01.cleaned_data['lsgd_name']
            data01.lsgd_year_of_formation = data_form01.cleaned_data['lsgd_year_of_formation']
            data01.lsgd_area_in_sqkm = data_form01.cleaned_data['lsgd_area_in_sqkm']
            data01.save()

    else:
        print("testing..")

    return render(request, 'r2n2/test.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year})

def test1_page(request):
    return render(request, 'r2n2/test2.html')
