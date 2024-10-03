from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ( TextPromptForm, HintForm, Context, Role,
                    Goal, Restrictions, Audience, FormatResult,
                      WritingStyle, Tone, Keywords, Examples
)

from .models import TextPrompt, Hint

User = get_user_model()


# dashbaord
@login_required(login_url='login')
def dashboard(request):
    # get all prompts 
    text_prompt = TextPrompt.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {'text_prompt':text_prompt})

# ask ai view 
@login_required(login_url='login')
def prompt_view(request):
    if request.method == 'POST':
        form = TextPromptForm(request.POST)
        if form.is_valid():
            # Get form data
            context = form.cleaned_data['context']
            role = form.cleaned_data['role']
            goal = form.cleaned_data['goal']
            restrictions = form.cleaned_data['restrictions']
            audience = form.cleaned_data['audience']
            format_result = form.cleaned_data['format_result']
            writing_style = form.cleaned_data['writing_style']
            tone = form.cleaned_data['tone']
            keywords = form.cleaned_data['keywords']
            examples = form.cleaned_data['examples']
            
            # Build the prompt with newlines or spaces between sections
            question = f"{context} {role} {goal} {restrictions} {audience} {format_result} {writing_style} {tone} {keywords} {examples}"

            # save the prompt 
            prompt = form.save(commit=False)
            prompt.user = request.user
            prompt.question = question
            prompt.save()
            # success message 
            messages.success(request, "Prompt saved successfully")
            return render(request, 'chat.html', {'form':form, 'question':question})
        
        else:
            messages.error(request, "Unable to process prompt. Please make sure you provide valid inputs in form fields")
            return render(request, 'chat.html', {'form':form})

    # GET request, render empty form
    form = TextPromptForm()
    return render(request, 'chat.html', {'form': form})


# prompt context view 
def prompt_context(request):
    hint = Hint.objects.all()
    if request.method == 'POST':
        form = Context(request.POST)

        if form.is_valid():
            pass 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'context.html', {'form':form, 'hint': hint.context})
    
    form = Context()
    return render(request, 'context.html', {'form':form, 'hint': hint.context})


# prompt role view 
def prompt_role(request):
    hint = Hint.objects.all()
    if request.method == 'POST':
        form = Role(request.POST)

        if form.is_valid():
            pass 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'role.html', {'form':form, 'hint': hint.role})
    
    form = Role()
    return render(request, 'role.html', {'form':form, 'hint': hint.role})


#prompt goal view 
def prompt_goal(request):
    hint = Hint.objects.all()
    if request.method == 'POST':
        form = Goal(request.POST)

        if form.is_valid():
            pass 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'goal.html', {'form':form, 'hint': hint.goal})
    
    form = Goal()
    return render(request, 'goal.html', {'form':form, 'hint': hint.goal})


# prompt restrictions view 
def prompt_restrictions(request):
    hint = Hint.objects.all()
    if request.method == 'POST':
        form = Restrictions(request.POST)

        if form.is_valid():
            pass 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'restrictions.html', {'form':form, 'hint': hint.restrictions})
    
    form = Restrictions()
    return render(request, 'restrictions.html', {'form':form, 'hint': hint.restrictions})

# prompt audience view 
def prompt_audience(request):
    hint = Hint.objects.all()
    if request.method == 'POST':
        form = Audience(request.POST)

        if form.is_valid():
            pass 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'audience.html', {'form':form, 'hint': hint.audience})
    
    form = Audience()
    return render(request, 'audience.html', {'form':form, 'hint': hint.audience})


# prompt format view 
def prompt_format(request):
    hint = Hint.objects.all()
    if request.method == 'POST':
        form = FormatResult(request.POST)

        if form.is_valid():
            pass 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'format_result.html', {'form':form, 'hint': hint.format_result})
    
    form = FormatResult()
    return render(request, 'format_result.html', {'form':form, 'hint': hint.format_result})

# prompt Writing style view 
def prompt_writing_style(request):
    hint = Hint.objects.all()
    if request.method == 'POST':
        form = WritingStyle(request.POST)

        if form.is_valid():
            pass 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'writing_style.html', {'form':form, 'hint': hint.writing_style})
    
    form = WritingStyle()
    return render(request, 'writing_style.html', {'form':form, 'hint': hint.writing_style})


# prompt tone view 
def prompt_tone(request):
    hint = Hint.objects.all()
    if request.method == 'POST':
        form = Tone(request.POST)

        if form.is_valid():
            pass 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'tone.html', {'form':form, 'hint': hint.tone})
    
    form = Tone()
    return render(request, 'tone.html', {'form':form, 'hint': hint.tone})

# prompt keywords view 
def prompt_keywords(request):
    hint = Hint.objects.all()
    if request.method == 'POST':
        form = Keywords(request.POST)

        if form.is_valid():
            pass 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'keywords.html', {'form':form, 'hint': hint.keywords})
    
    form = Keywords()
    return render(request, 'keywords.html', {'form':form, 'hint': hint.keywords})


# prompt example view 
def prompt_example(request):
    hint = Hint.objects.all()
    if request.method == 'POST':
        form = Examples(request.POST)

        if form.is_valid():
            pass 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'examples.html', {'form':form, 'hint': hint.examples})
    
    form = Examples()
    return render(request, 'examples.html', {'form':form, 'hint': hint.examples})
