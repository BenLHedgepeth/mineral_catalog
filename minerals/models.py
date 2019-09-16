from django.db import models


# Create your models here.
class Mineral(models.Model):
    name = models.CharField(max_length=255, null="")
    image_filename = models.CharField(max_length=255, null="")
    image_caption = models.CharField(max_length=255, null="")
    category = models.CharField(max_length=255, null="")
    formula = models.CharField(max_length=255, null="")
    strunz_classification = models.CharField(max_length=255, null="")
    color = models.CharField(max_length=255, null="")
    crystal_system = models.CharField(max_length=255, null="")
    unit_cell = models.CharField(max_length=255, null="")
    crystal_symmetry = models.CharField(max_length=255, null="")
    cleavage = models.CharField(max_length=255, null="")
    mohs_scale_hardness = models.CharField(max_length=255, null="")
    luster = models.CharField(max_length=255, null="")
    streak = models.CharField(max_length=255, null="")
    diaphaneity = models.CharField(max_length=255, null="")
    optical_properties = models.CharField(max_length=255, null="")
    refractive_index = models.CharField(max_length=255, null="")
    crystal_habit = models.CharField(max_length=255, null="")
    specific_gravity = models.CharField(max_length=255, null="")
    group = models.CharField(max_length=255, null="")


def __str__(self):
    return self.name
