from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

class Quiz(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(blank=True)
	roll_out = models.BooleanField(default=False)


	class Meta:
		def __str__(self):
			return self.name


class Question(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	label = models.CharField(max_length=100)


	def __str__(self):
		return self.label


class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	label = models.CharField(max_length=100)
	is_correct = models.BooleanField(default=False)

	def __str__(self):
		return self.label


class UsersAnswer(models.Model):

	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.question.label

class result(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	score=models.IntegerField(default=0)


@receiver(pre_save, sender=Quiz)
def slugify_name(sender, instance, *args, **kwargs):
	instance.slug = slugify(instance.name)
