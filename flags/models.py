from django.db import models
from PIL import Image

class Flags(models.Model):
	symbol = models.CharField(verbose_name="символ", db_index=True, unique=True, max_length=64)
	description = models.TextField(verbose_name="описание")
	img = models.CharField(verbose_name="img URL", max_length=128)

	def __str__(self):
		return self.symbol

