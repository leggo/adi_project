from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
from django.core.urlresolvers import reverse 
from django.views import generic

from adi_app.models import Question, Choice


# Create your views here.


def IndexView(generic.ListView):
	template_name = 'adi_app/index.html'
	context_object_name = 'latest_question_list'
	
	def get_queryset(self)
		return Question.objects.order_by('-pub_date')[:5]
		
#	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#	context = {'latest_question_list': latest_question_list}
#	return render(request, , context)


#	return render(request,'adi_project/index.html', 

#	meep = 'Hello world'
#	return HttpResponse(meep)
	
	
def time(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s. </body></html>" % now
	return HttpResponse(html)
	
	
def question(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'adi_app/question.html', {'question': question})

	return HttpResponse("You are looking at question number %s." % question_id)
	
	
def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'adi_app/question.html', {
			'question': p,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		
		return HttpResponseRedirect(reverse('results', args=(p.id,)))
		
		
def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'adi_app/results.html', {'question': question})