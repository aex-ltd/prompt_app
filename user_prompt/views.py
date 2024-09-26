from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.core.mail import send_mail
# from django.conf import settings 

# from .services import ask_gpt, ask_gemini
from .forms import TextPromptForm
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
