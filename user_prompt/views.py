from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings 

from .services import ask_gpt, ask_gemini
from .forms import TextPromptForm
from .models import TextPrompt, FilePrompt

User = get_user_model()


# dashbaord
@login_required(login_url='login')
def dashboard(request):
    text_prompt = TextPrompt.objects.filter(user=request.user)
    file_prompt = FilePrompt.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {'text_prompt':text_prompt, 'file_prompt':file_prompt})

# ask ai view 
@login_required(login_url='login')
def ask_ai_view(request):
    if request.method == 'POST':
        form = TextPromptForm(request.POST)
        if form.is_valid():
            # get user email 
            email = request.user.email 

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

            # Ask ChatGPT
            # gpt_response = ask_gpt(question)
            # gemini_response = ask_gemini(question)

            # response_1 = None
            # response_2 = None

            # if gpt_response:
            #     response_1 = f"{gpt_response} \n"
            # else:
            #     response_1 = f"Unable to get response from ChatGPT\n"

            # if gemini_response:
            #      response_2 = f"{gemini_response} \n"
            # else:
            #     response_2 = f"Unable to get response from Gemini\n"
            
            # context = {
            #     'form':form,
            #     'question':question,
            #     'response_1':response_1,
            #     'response_2': response_2
            # }
            # # save form data and response to database 
            # text_prompt = form.save(commit=False)
            # text_prompt.response = f"{response_1} \n {response_2} \n"
            # text_prompt.user = request.user
            # text_prompt.save()

            subject = f"New Prompt Alert"
            body = f"Prompt: \n {question}"

            # try to send mail
            try:
                send_mail(subject, body, "webmaster@aex.com", [email,])

                messages.success(request, "Your prompt has been sent to your email")
                return redirect('dashboard')
            
            except Exception as e:
                print(e)
                messages.error(request, "An error occured. Unable to send mail")
                 
        else:
            messages.error(request, "Invalid data format. Please check the form.")
        
        # Show the form with errors
        return render(request, 'chat.html', {'form': form})

    # GET request, render empty form
    form = TextPromptForm()
    return render(request, 'chat.html', {'form': form})
