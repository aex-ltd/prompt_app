from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .services import ask_ai
from .forms import TextPromptForm

User = get_user_model()

# ask ai view 
@login_required(login_url='login')
def ask_ai_view(request):
    if request.method == 'POST':
        form = TextPromptForm(request.POST)
        if form.is_valid():
            # Get form data
            context = form.cleaned_data['context']
            role = form.cleaned_data['role']
            goal = form.cleaned_data['goal']
            restrictions = form.cleaned_data['restrictions']
            audience = form.cleaned_data['audience']
            writing_style = form.cleaned_data['writing_style']
            tone = form.cleaned_data['tone']
            keywords = form.cleaned_data['keywords']
            examples = form.cleaned_data['examples']
            
            # Build the prompt with newlines or spaces between sections
            question = (f"Context: {context}\nRole: {role}\nGoal: {goal}\n"
                        f"Restrictions: {restrictions}\nAudience: {audience}\n"
                        f"Writing Style: {writing_style}\nTone: {tone}\n"
                        f"Keywords: {keywords}\nExamples: {examples}")

            # Ask ChatGPT
            response = ask_ai(question)
            if response:
                messages.success(request, "Response fetched successfully!")
                
                # Save form data and response to the database
                text_prompt = form.save(commit=False)
                text_prompt.response = response
                text_prompt.user = request.user  # Ensure the user is assigned
                text_prompt.save()

                return render(request, 'chat.html', {'question': question, 'response': response, 'form': form})
            else:
                messages.error(request, "Error fetching response from ChatGPT.")
        else:
            messages.error(request, "Invalid data format. Please check the form.")
        
        # Show the form with errors
        return render(request, 'chat.html', {'form': form})

    # GET request, render empty form
    form = TextPromptForm()
    return render(request, 'chat.html', {'form': form})
