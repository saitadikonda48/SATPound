from django.db import models
from videos.models import Video
# Create your models here.

class OpenQuestion(models.Model):
	video = models.ForeignKey(Video)
	text = models.TextField()
	answer = models.CharField(max_length=10)
	help = models.TextField()

	def __unicode__(self):
		return self.text

class MultipleChoiceQuestion(models.Model):
	video = models.ForeignKey(Video)
	text = models.TextField()
	choiceA = models.CharField(max_length=350)
	choiceB = models.CharField(max_length=350)
	choiceC = models.CharField(max_length=350)
	choiceD = models.CharField(max_length=350)
	correctAnswer = models.CharField(max_length=1)
	answerExplanation = models.TextField()
	help = models.TextField()

	def __unicode__(self):
		return self.text
