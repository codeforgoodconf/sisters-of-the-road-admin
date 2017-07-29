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
		choices = EVENT_TYPE_CHOICES,
		default = SUBTRACT,
	)
	event_time = models.DateTimeField(auto_now_add=True)
	#staff_id = models.ForeignKey()

class BarterAccount(models.Model):
	customer_name = models.CharField(max_length=100)
	balance = models.DecimalField(max_digits=5, decimal_places=2)
	