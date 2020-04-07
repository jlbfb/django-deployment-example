from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from app_two.models import States, Documents, Headings, SubHeadings, Texts, Relations
from app_two.forms import StateForm, DocumentForm, HeadingForm, SubHeadingForm, TextForm, RelationsForm, UpdateTextForm

# Create your views here.
def index(request):
    
    request.session['screen_shots'] = 8
    my_dict = {'insert_me': 'Now I am coming from app_two index.html!', 'screenshots': request.session['screen_shots'], 'title': 'The Index Page'}
    return render(request, 'app_two/index.html', context = my_dict)

def help(request):
    my_dict = {'insert_help' : 'Help Page'}
    return render(request,'app_two/help.html', context = my_dict)

def headings(request):
    headings_list = Headings.objects.order_by('heading')
    screen_shots = request.session['screen_shots']
    headings_dict = {'insert_headings' : headings_list, 'screen_shots': screen_shots, 'title': 'Headings'}
    return render(request,'app_two/headings.html', context = headings_dict)

def screens(request):

    the_id = request.session['the_id']

    text_obj = Texts.objects.get(pk = the_id)
    the_text = text_obj.text
    the_section = SubHeadings.objects.get(pk = text_obj.subheading_id)
    the_keywords = text_obj.keywords

    screens_dict = {'the_id': the_id, 
                    'title': 'Screens', 
                    'the_text':the_text,
                    'the_section':the_section,
                    'the_keywords':the_keywords}

    return render(request, 'app_two/screens.html', context=screens_dict)

def relations(request):
    
    relations_form = RelationsForm()
    
    if request.method == 'POST':

        relations_form = RelationsForm(data=request.POST)

        '''
        state_form = StateForm(data=request.POST)
        document_form = DocumentForm(data=request.POST)
        heading_form = HeadingForm(data=request.POST)
        subheading_form = SubHeadingForm(data=request.POST)

        TO CREATE A FORM TO CHANGE AN EXISTING FIELD:
        title = Documents.objects.get(pk=1)  # or whatever the pk is
        form = DocumentForm(instance=title)
        '''

        if relations_form.is_valid():

            relations = relations_form.save()
            relations.save()
        
            return screens(request)
        
        else:
            print(relations_form.errors)
    else:
        relations_form = RelationsForm()
    
    return render(request,'app_two/relations.html',{'relations_form':relations_form})

def import_text(request):

    text_form = TextForm()
    
    if request.method == 'POST':

        text_form = TextForm(data=request.POST)

        '''
        state_form = StateForm(data=request.POST)
        document_form = DocumentForm(data=request.POST)
        heading_form = HeadingForm(data=request.POST)
        subheading_form = SubHeadingForm(data=request.POST)

        TO CREATE A FORM TO CHANGE AN EXISTING FIELD:
        title = Documents.objects.get(pk=1)  # or whatever the pk is
        form = DocumentForm(instance=title)
        '''

        if text_form.is_valid():

            text = text_form.save()
            # text.save()
            the_id = text.pk
            request.session['the_id'] = the_id
        
            return HttpResponseRedirect('/app_two/update_text/') #screens(request)
        
        else:
            print(text_form.errors)
    else:
        text_form = TextForm()
    
    return render(request,'app_two/import_text.html',{'text_form':text_form, 'title': 'Import Text'})

def update_text(request):

    the_id = request.session['the_id']
    text_obj = Texts.objects.get(pk = the_id)
    # update_text_form = UpdateTextForm()

    if request.method == 'POST':

        update_text_form = UpdateTextForm(request.POST, instance=text_obj)

        if update_text_form.is_valid():

            update_text_form.save()
        
            return screens(request)

        else:
            print(update_text_form.errors)

    else:
        update_text_form = UpdateTextForm(instance=text_obj)
    
    return render(request, 'app_two/update_text.html', {'update_text_form': update_text_form, 'title': 'Update Text', 'the_id': the_id})