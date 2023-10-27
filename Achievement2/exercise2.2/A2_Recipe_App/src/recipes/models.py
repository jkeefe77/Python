from django.db import models

# Create your models here.


class Recipe(models.Model):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    HARD = "HARD"

    DIFFICULTY_CHOICES = [
        (BEGINNER, "Beginner"),
        (INTERMEDIATE, "Intermediate"),
        (HARD, "Hard"),
    ]

    recipe_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    cooking_time = models.PositiveBigIntegerField
    ingredients = models.CharField(max_length=120)

    difficulty = models.CharField(
        max_length=15,
        choices=DIFFICULTY_CHOICES,
        default=BEGINNER,
    )

    def save(self, *args, **kwargs):
        # Adjust these thresholds as needed based on your criteria
        if self.cooking_time <= 30 and self.ingredients <= 5:
            self.difficulty = self.BEGINNER
        elif self.cooking_time <= 60 and self.ingredients <= 10:
            self.difficulty = self.INTERMEDIATE
        else:
            self.difficulty = self.HARD

    def __str__(self):
        return str(self.name)
