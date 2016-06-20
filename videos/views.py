from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, Http404, HttpResponseRedirect, get_object_or_404

# Create your views here.
from analytics.signals import page_view
from comments.forms import CommentForm
from comments.models import Comment
from questions.models import OpenQuestion, MultipleChoiceQuestion
from .models import Video, Category, TaggedItem


#@login_required
def video_detail(request, cat_slug, vid_slug):
	cat = get_object_or_404(Category, slug=cat_slug)
	obj = get_object_or_404(Video, slug=vid_slug, category=cat)
	quiz_count=range(1, 12)
	multiple_choice_questions = MultipleChoiceQuestion.objects.filter(video=obj)
	open_questions = OpenQuestion.objects.filter(video=obj)
	mc_question_list = list(multiple_choice_questions)
	myList = mc_question_list
	# try:
	# 	question5 = mc_question_list.pop()
	# except:
	# 	question5 = ""
	try:
		question1 = mc_question_list.pop()
	except:
		question1 = ""
	try:
		question2 = mc_question_list.pop()
	except:
		question2 = ""
	try:
		question3 = mc_question_list.pop()
	except:
		question3 = ""
	try:
		question4 = mc_question_list.pop()
	except:
		question4 = ""
	

	print question4
	page_view.send(request.user, 
				page_path=request.get_full_path(), 
				primary_obj=obj,
				secondary_obj=cat)
	if request.user.is_authenticated() or obj.has_preview:
		try:
			is_member = request.user.is_member
		except:
			is_member = None
		if is_member or obj.has_preview:
			comments = obj.comment_set.all()
			for c in comments:
				c.get_children()
			comment_form = CommentForm()
			context = {"obj": obj,
				'question1':question1,
				'question2':question2,
				'question3':question3,
				'question4':question4,
				# 'question5':question5,
				"myList":myList,
				"comments":comments,
				"quiz_count":quiz_count,
				"comment_form": comment_form,
				"multiple_choice_questions":multiple_choice_questions,
				"open_questions":open_questions}
			return render(request, "videos/video_detail.html", context)
		else:
			# upgrade account
			next_url = obj.get_absolute_url()
			return HttpResponseRedirect("%s?next=%s"%(reverse('account_upgrade'), next_url))
	else:
		next_url = obj.get_absolute_url()
		return HttpResponseRedirect("%s?next=%s"%(reverse('login'), next_url))


def category_list(request):
	queryset = Category.objects.all()
	context = {
		"queryset": queryset,
	}
	return render(request, "videos/category_list.html", context)



# @login_required
def category_detail(request, cat_slug):
	obj = get_object_or_404(Category, slug=cat_slug)
	queryset = obj.video_set.all()
	page_view.send(request.user, 
				page_path=request.get_full_path(), 
				primary_obj=obj)


	print queryset
	return render(request, "videos/video_list.html", {"obj": obj, "queryset": queryset})