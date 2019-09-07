from django.db import models


class Signals(models.Model):
	description = models.TextField(verbose_name="описание")
	img = models.CharField(verbose_name="img URL", max_length=128)

	def __str__(self):
		return str(self.id)

