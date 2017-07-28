from django.db import models

# Create your models here.
class BarterEvent(models.Model):
	barter_account = models.ForeignKey(
		'BarterAccount',
		#on_delete=models.CASCADE,
	)
	ADD = 'Add'
	SUBTRACT = 'Subtract'
	NOTE = 'Note'
	EVENT_TYPE_CHOICES = (
		(ADD, 'Add'),
		(SUBTRACT, 'Subtract'),
		(NOTE, 'Note'),
	)
	event_type = models.CharField(
		max_length=20,
		choices = event_type_choices,
		default = SUBTRACT,
	)
	event_time = models.DateTimeField(auto_now_add=True)
	#staff_id = models.ForeignKey()

class BarterAccount(models.Model):
	patron_name = models.CharField(max_length=100)
	balance = models.IntegerField(max_length=30)
	