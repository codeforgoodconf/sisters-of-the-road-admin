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
	amount = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
	
			
class BarterAccount(models.Model):
	patron_name = models.CharField(max_length=100)
	balance = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
	
	def add(self, amount):
		self.balance += amount
		return self.balance
	
	def subtract(self, amount):
		self.balance -= amount
		return self.balance
	
	def __str__(self):
		return 'Account: {}'.format(self.patron_name)
	