import re

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .forms import RegexForm

# WILL BE CALLED ONCE THE SUBMIT BUTTON IS CLICKED
class RegexView(View):
    template_name = 'regex/regex_home.html'

    def get(self, request, *args, **kwargs):
        form = RegexForm()
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = RegexForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            user_re, text = data['user_regex'], data['test_text']
            matched_result = re.findall(user_re, text)

            context = {'form': form}
            
            if matched_result:
                return render(request, self.template_name, {**context, "result": matched_result[0]})
            
        return render(request, self.template_name, {'form': form})

# WILL BE CALLED USING AJAX
def evaluate_regex(request):
    if request.method == "GET":
        user_re = request.GET.get('user_re', None)
        test_txt = request.GET.get('test_txt', None)

        data = {'alert': 'danger'}
        matched_result = re.findall(user_re, test_txt)

        if matched_result:
            data['alert'] = 'success'
            data['result'] = matched_result[0]
        
        return JsonResponse(data)
    
