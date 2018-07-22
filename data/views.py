from django.shortcuts import render, redirect

from qbnk.models import QuestionBank, QuestionHeader
from lsgd.models import Lsgd, Taluk, Block, Assembly, Parliament
from data.models import D001, D002

from data.forms import F001, F002


# Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D001 - General Details                                                               #
########################################################################################################################################################
def gdls_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q001").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    taluks = Taluk.objects.filter(taluk_code__startswith = district_code).values().order_by('taluk_code')
    blocks = Block.objects.filter(block_code__startswith = district_code).values().order_by('block_code')
    assemblys = Assembly.objects.filter(assembly_code__startswith = district_code).values().order_by('assembly_code')
    parliaments = Parliament.objects.filter(parliament_code__startswith = district_code).values().order_by('parliament_code')


    if request.method == 'POST':
        data_form01 = F001(request.POST)
        data01 = D001()
        print(request.POST)

        if data_form01.is_valid():
            data01.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data01.lsgd_name = data_form01.cleaned_data['lsgd_name']
            data01.lsgd_year_of_formation = data_form01.cleaned_data['lsgd_year_of_formation']
            data01.lsgd_area_in_sqkm = data_form01.cleaned_data['lsgd_area_in_sqkm']
            data01.lsgd_taluk_name = data_form01.cleaned_data['lsgd_taluk_name']
            data01.lsgd_block_name = data_form01.cleaned_data['lsgd_block_name']
            data01.lsgd_parliamentary_constituency = data_form01.cleaned_data['lsgd_parliamentary_constituency']
            data01.lsgd_assembly_constituency = data_form01.cleaned_data['lsgd_assembly_constituency']
            data01.lsgd_no_of_wards = data_form01.cleaned_data['lsgd_no_of_wards']
            data01.lsgd_no_of_female_wards = data_form01.cleaned_data['lsgd_no_of_female_wards']
            data01.lsgd_no_of_scst_wards = data_form01.cleaned_data['lsgd_no_of_scst_wards']
            data01.lsgd_no_of_rivers = data_form01.cleaned_data['lsgd_no_of_rivers']
            data01.lsgd_name_of_rivers = data_form01.cleaned_data['lsgd_name_of_rivers']
            data01.lsgd_coastal_line_length_in_km = data_form01.cleaned_data['lsgd_coastal_line_length_in_km']
            data01.lsgd_forest_area_in_hectors = data_form01.cleaned_data['lsgd_forest_area_in_hectors']
            data01.lsgd_type_of_soil = data_form01.cleaned_data['lsgd_type_of_soil']
            data01.lsgd_main_roads = data_form01.cleaned_data['lsgd_main_roads']
            data01.lsgd_nearest_railway_station = data_form01.cleaned_data['lsgd_nearest_railway_station']
            data01.lsgd_jilla_panchayath_name = data_form01.cleaned_data['lsgd_jilla_panchayath_name']
            data01.lsgd_jilla_panchayath_ward = data_form01.cleaned_data['lsgd_jilla_panchayath_ward']
            data01.lsgd_block_panchayath_name = data_form01.cleaned_data['lsgd_block_panchayath_name']
            data01.lsgd_block_panchayath_wards = data_form01.cleaned_data['lsgd_block_panchayath_wards']
            data01.save()
        
            print(data_form01.cleaned_data['lsgd_name'])
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/demp/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")

    return render(request, 'data/gdls.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'taluks': taluks, 'blocks': blocks, 'assemblys': assemblys, 'parliaments': parliaments})



########################################################################################################################################################
#                                                 Data Entry for D002 - Demographic Particulars                                                        #
########################################################################################################################################################
def demp_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q002").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)

    if request.method == 'POST':
        data_form02 = F002(request.POST)
        data02 = D002()
        print(request.POST)

        if data_form02.is_valid():
            #print("sucess")
            data02.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data02.population_male = data_form02.cleaned_data['population_male']
            data02.save()

        else:
            print("Form not valid")

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/sddc/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/gdls/')

        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")

    return render(request, 'data/demp.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user})



########################################################################################################################################################
#                                                Data Entry for D003 - Sex Desegragated Data of Children                                               #
########################################################################################################################################################

def sddc_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q003").values('question_text')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)

    return render(request, 'data/sddc.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user})





########################################################################################################################################################
#                                                Data Entry TEST -- One page Template -- Old Copy                                                      #
########################################################################################################################################################
def data_page(request):
    current_header = 1
    lsgd_code = 'KL008M001'
    data_entry_year = 2018
    current_user = request.user

    questions =  QuestionBank.objects.filter(question_code__startswith = "Q001").values().order_by('question_code')
    headers = QuestionHeader.objects.all().values()
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    current_header_text = headers[current_header-1].get('header_text')

    # Update the left column menu and related values.
    if request.method == 'POST':
        #print(request.POST)
        clicked_header = int(request.POST['clicked_header'])
        if clicked_header > 20 and 'next_page' in request.POST:
            current_header = clicked_header - 19
            if current_header > 19:
                current_header = 1
        elif clicked_header > 20 and 'prev_page' in request.POST:
            current_header = clicked_header - 21
            if current_header < 1:
                current_header = 19
        elif clicked_header > 20 and 'save_details' in request.POST:
            current_header = clicked_header - 20
        else:
            current_header = clicked_header
        
        current_header_text = headers[current_header-1].get('header_text')
        current_questions = "Q" + str('{0:03}'.format(current_header))
        #print(current_questions)
        questions =  QuestionBank.objects.filter(question_code__startswith = current_questions).values().order_by('question_code')

        # Enter current data into the database by collecting data from the current form.
        data_form = F001(request.POST)
        #print(data_form)
        #print(request.POST)
        
        if data_form.is_valid():
            print(data_form.cleaned_data['f1'])
        else:
            print("not valid")


    return render(request, 'data/data.html', {'headers': headers, 'current_header': current_header, 'current_header_text': current_header_text, \
                            'questions': questions, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user})

