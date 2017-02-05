from django.db import models


class GameCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Game(models.Model):
    owner = models.ForeignKey(
        'auth.User',
        related_name='games',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, unique=True, blank=True, default='')
    release_date = models.DateTimeField()
    game_category = models.ForeignKey(
        GameCategory,
        related_name='games',
        on_delete=models.CASCADE
    )
    played = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Player(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, unique=True, blank=True, default='')
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MALE,
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class PlayerScore(models.Model):
    player = models.ForeignKey(
        Player,
        related_name='scores',
        on_delete=models.CASCADE
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )
    score = models.IntegerField()
    score_date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-score',)