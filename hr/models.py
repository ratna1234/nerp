from django.db import models
from users.models import User

class Punch(models.Model):
	time=models.DateTimeField()
	user=models.ForeignKey(User)

	class Meta:
		abstract=True

class PunchIn(Punch):
	pass

class PunchOut(Punch):
	pass

# Create your models here.
