from django.db import models

# Create your models here.
class upcomingmatches(models.Model):
    leaguename = models.CharField(max_length=900)
    opponent_one = models.CharField(max_length=100)
    opponent_two = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    odds_one = models.DecimalField(max_digits=5,decimal_places=2)
    odds_two = models.DecimalField(max_digits=5,decimal_places=2)

class livematches(models.Model):
    leaguename = models.CharField(max_length=900)
    opponent_one = models.CharField(max_length=100)
    opponent_two = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    livescore_opone = models.IntegerField()
    livescore_optwo = models.IntegerField()

class listmatches(models.Model):
    leaguename = models.CharField(max_length=900)
    opponent_one = models.CharField(max_length=100)
    opponent_two = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    pastscore_opone = models.IntegerField()
    pastscore_optwo = models.IntegerField()

    