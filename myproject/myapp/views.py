from django.shortcuts import render, redirect
from .forms import StressCheckForm
from .models import StressCheckResponse
from django.views.generic import TemplateView

class TopView(TemplateView):
    template_name="survey.html"

def stress_check_form(request):
    if request.method == 'POST':
        form = StressCheckForm(request.POST)
        if form.is_valid():
            # Process the form data, save the response, etc.
            response = form.save()
            # Redirect to the results view with the response id
            return redirect('stress_check_results', response_id=response.id)
    else:
        form = StressCheckForm()
    return render(request, 'myapp/stress_check_form.html', {'form': form})

def stress_check_results(request, response_id):
    # Retrieve the stress check response using the response_id
    response = StressCheckResponse.objects.get(id=response_id)
    # Calculate results or fetch pre-calculated results from the model
    results = response.calculate_results()
    return render(request, 'myapp/stress_check_results.html', {'results': results})
