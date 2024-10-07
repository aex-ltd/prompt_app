from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ( TextPromptForm, HintForm, Context, Role,
                    Goal, Restrictions, Audience, FormatResult,
                      WritingStyle, Tone, Keywords, Examples, Title
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



# prompt title view 
@login_required(login_url='login')
def prompt_title(request):
    hint = Hint.objects.all()
    if request.method == 'POST':
        form = Title(request.POST)

        if form.is_valid():
            # create new text prompt 
            prompt = TextPrompt.objects.create(user=request.user, title=form.cleaned_data['title'])
            # get prompt id 
            request.session['prompt_id'] = prompt.id
            prompt.save()

            return redirect('prompt_context') 
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'title.html', {'form':form, 'hint': hint})
    
    form = Title()
    return render(request, 'title.html', {'form':form, 'hint': hint})



# prompt context view 
@login_required(login_url='login')
def prompt_context(request):
    hint = Hint.objects.all()
    # get prompt_id from session 
    prompt_id = None 
    try:
        prompt_id = int(request.session.get('prompt_id'))
    except ( ValueError, TypeError):
        prompt_id = 0

    # get prompt 
    prompt = TextPrompt.objects.filter(user=request.user, id=prompt_id)
    if not prompt:
        messages.error(request, "Unable to fetch prompt. Please create a new prompt.")
        return redirect('prompt_title')

    if request.method == 'POST':
        form = Context(request.POST)

        if form.is_valid():
            for p in prompt:
                p.context = form.cleaned_data['context']
                p.save()
                return redirect('prompt_role') 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'context.html', {'form':form, 'hint': hint, 'prompt':prompt})
    
    form = Context()
    return render(request, 'context.html', {'form':form, 'hint': hint, 'prompt': prompt})



# prompt role view 
@login_required(login_url='login')
def prompt_role(request):
    hint = Hint.objects.all()
    # get prompt_id from session 
    prompt_id = None 
    try:
        prompt_id = int(request.session.get('prompt_id'))
    except ( ValueError, TypeError):
        prompt_id = 0

    # get prompt 
    prompt = TextPrompt.objects.filter(user=request.user, id=prompt_id)
    if not prompt:
        messages.error(request, "Unable to fetch prompt. Please create a new prompt.")
        return redirect('prompt_title')
    
    if request.method == 'POST':
        form = Role(request.POST)

        if form.is_valid():
            for p in prompt:
                p.role = form.cleaned_data['role']
                p.save()
                return redirect('prompt_goal') 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'role.html', {'form':form, 'hint': hint, 'prompt': prompt})
    
    form = Role()
    return render(request, 'role.html', {'form':form, 'hint': hint, 'prompt':prompt})



#prompt goal view 
@login_required(login_url='login')
def prompt_goal(request):
    hint = Hint.objects.all()
    # get prompt_id from session 
    prompt_id = None 
    try:
        prompt_id = int(request.session.get('prompt_id'))
    except ( ValueError, TypeError):
        prompt_id = 0

    # get prompt 
    prompt = TextPrompt.objects.filter(user=request.user, id=prompt_id)
    if not prompt:
        messages.error(request, "Unable to fetch prompt. Please create a new prompt.")
        return redirect('prompt_title')

    if request.method == 'POST':
        form = Goal(request.POST)

        if form.is_valid():
            for p in prompt:
                p.goal = form.cleaned_data['goal']
                p.save()
                return redirect('prompt_restrictions')  
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'goal.html', {'form':form, 'hint': hint, 'prompt': prompt})
    
    form = Goal()
    return render(request, 'goal.html', {'form':form, 'hint': hint, 'prompt':prompt})



# prompt restrictions view 
@login_required(login_url='login')
def prompt_restrictions(request):
    hint = Hint.objects.all()
    # get prompt_id from session 
    prompt_id = None 
    try:
        prompt_id = int(request.session.get('prompt_id'))
    except ( ValueError, TypeError):
        prompt_id = 0

    # get prompt 
    prompt = TextPrompt.objects.filter(user=request.user, id=prompt_id)
    if not prompt:
        messages.error(request, "Unable to fetch prompt. Please create a new prompt.")
        return redirect('prompt_title')

    if request.method == 'POST':
        form = Restrictions(request.POST)

        if form.is_valid():
            for p in prompt:
                p.restrictions = form.cleaned_data['restrictions']
                p.save()
                return redirect('prompt_audience') 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'restrictions.html', {'form':form, 'hint': hint, 'prompt':prompt})
    
    form = Restrictions()
    return render(request, 'restrictions.html', {'form':form, 'hint': hint, 'prompt':prompt})



# prompt audience view 
@login_required(login_url='login')
def prompt_audience(request):
    hint = Hint.objects.all()
    # get prompt_id from session 
    prompt_id = None 
    try:
        prompt_id = int(request.session.get('prompt_id'))
    except ( ValueError, TypeError):
        prompt_id = 0

    # get prompt 
    prompt = TextPrompt.objects.filter(user=request.user, id=prompt_id)
    if not prompt:
        messages.error(request, "Unable to fetch prompt. Please create a new prompt.")
        return redirect('prompt_title')

    if request.method == 'POST':
        form = Audience(request.POST)

        if form.is_valid():
            for p in prompt:
                p.audience = form.cleaned_data['audience']
                p.save()
                return redirect('prompt_format') 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'audience.html', {'form':form, 'hint': hint, 'prompt':prompt})
    
    form = Audience()
    return render(request, 'audience.html', {'form':form, 'hint': hint, 'prompt': prompt})



# prompt format view 
@login_required(login_url='login')
def prompt_format(request):
    hint = Hint.objects.all()
    # get prompt_id from session 
    prompt_id = None 
    try:
        prompt_id = int(request.session.get('prompt_id'))
    except ( ValueError, TypeError):
        prompt_id = 0

    # get prompt 
    prompt = TextPrompt.objects.filter(user=request.user, id=prompt_id)
    if not prompt:
        messages.error(request, "Unable to fetch prompt. Please create a new prompt.")
        return redirect('prompt_title')

    if request.method == 'POST':
        form = FormatResult(request.POST)

        if form.is_valid():
            for p in prompt:
                p.format_result = form.cleaned_data['format_result']
                p.save()
                return redirect('prompt_writing_style') 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'format_result.html', {'form':form, 'hint': hint, 'prompt': prompt})
    
    form = FormatResult()
    return render(request, 'format_result.html', {'form':form, 'hint': hint, 'prompt': prompt})



# prompt Writing style view 
@login_required(login_url='login')
def prompt_writing_style(request):
    hint = Hint.objects.all()
    # get prompt_id from session 
    prompt_id = None 
    try:
        prompt_id = int(request.session.get('prompt_id'))
    except ( ValueError, TypeError):
        prompt_id = 0

    # get prompt 
    prompt = TextPrompt.objects.filter(user=request.user, id=prompt_id)
    if not prompt:
        messages.error(request, "Unable to fetch prompt. Please create a new prompt.")
        return redirect('prompt_title')

    if request.method == 'POST':
        form = WritingStyle(request.POST)

        if form.is_valid():
            for p in prompt:
                p.writing_style = form.cleaned_data['writing_style']
                p.save()
                return redirect('prompt_tone') 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'writing_style.html', {'form':form, 'hint': hint, 'prompt': prompt})
    
    form = WritingStyle()
    return render(request, 'writing_style.html', {'form':form, 'hint': hint, 'prompt': prompt})



# prompt tone view 
@login_required(login_url='login')
def prompt_tone(request):
    hint = Hint.objects.all()
    # get prompt_id from session 
    prompt_id = None 
    try:
        prompt_id = int(request.session.get('prompt_id'))
    except ( ValueError, TypeError):
        prompt_id = 0

    # get prompt 
    prompt = TextPrompt.objects.filter(user=request.user, id=prompt_id)
    if not prompt:
        messages.error(request, "Unable to fetch prompt. Please create a new prompt.")
        return redirect('prompt_title')

    if request.method == 'POST':
        form = Tone(request.POST)

        if form.is_valid():
            for p in prompt:
                p.tone = form.cleaned_data['tone']
                p.save()
                return redirect('prompt_keywords') 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'tone.html', {'form':form, 'hint': hint, 'prompt': prompt})
    
    form = Tone()
    return render(request, 'tone.html', {'form':form, 'hint': hint, 'prompt': prompt})



# prompt keywords view 
@login_required(login_url='login')
def prompt_keywords(request):
    hint = Hint.objects.all()
    # get prompt_id from session 
    prompt_id = None 
    try:
        prompt_id = int(request.session.get('prompt_id'))
    except ( ValueError, TypeError):
        prompt_id = 0

    # get prompt 
    prompt = TextPrompt.objects.filter(user=request.user, id=prompt_id)
    if not prompt:
        messages.error(request, "Unable to fetch prompt. Please create a new prompt.")
        return redirect('prompt_title')

    if request.method == 'POST':
        form = Keywords(request.POST)

        if form.is_valid():
            for p in prompt:
                p.keywords = form.cleaned_data['keywords']
                p.save()
                return redirect('prompt_examples') 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'keywords.html', {'form':form, 'hint': hint, 'prompt': prompt})
    
    form = Keywords()
    return render(request, 'keywords.html', {'form':form, 'hint': hint, 'prompt': prompt})



# prompt example view 
@login_required(login_url='login')
def prompt_examples(request):
    hint = Hint.objects.all()
    # get prompt_id from session 
    prompt_id = None 
    try:
        prompt_id = int(request.session.get('prompt_id'))
    except ( ValueError, TypeError):
        prompt_id = 0

    # get prompt 
    prompt = TextPrompt.objects.filter(user=request.user, id=prompt_id)
    if not prompt:
        messages.error(request, "Unable to fetch prompt. Please create a new prompt.")
        return redirect('prompt_title')

    if request.method == 'POST':
        form = Examples(request.POST)

        if form.is_valid():
            for p in prompt:
                p.examples = form.cleaned_data['examples']
                p.question = f"{p.context} {p.role} {p.goal} {p.restrictions} {p.audience} {p.format_result} {p.writing_style} {p.tone} {p.keywords} {p.examples}"
                p.save()
                messages.success(request, "Prompt saved successfully.")
                return redirect('dashboard') 
        
        else:
            messages.error(request, "Invalid data format. Please try again")
            return render(request, 'examples.html', {'form':form, 'hint': hint, 'prompt': prompt})
    
    form = Examples()
    return render(request, 'examples.html', {'form':form, 'hint': hint, 'prompt': prompt})
