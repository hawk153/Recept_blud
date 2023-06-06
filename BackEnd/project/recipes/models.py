from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['pk']

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="dishes")
    description = models.TextField()
    photo = models.ImageField(blank=True)

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

    def __str__(self):
        return self.name
