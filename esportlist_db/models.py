from django.db import models

# Create your models here.
class nextmatches(models.Model):
    leaguename = models.CharField(max_length=900)
    games_id = models.IntegerField()
    opponent_one = models.CharField(max_length=100,blank=True)
    opponent_two = models.CharField(max_length=100,blank=True)
    datetime = models.CharField(max_length=100,blank=True)


class livematches(models.Model):
    leaguename = models.CharField(max_length=900)
    matches_id = models.IntegerField()
    opponent_one = models.CharField(max_length=100)
    opponent_two = models.CharField(max_length=100)
    datetime = models.CharField(max_length=100,blank=True)
    livescore_opone = models.IntegerField()
    livescore_optwo = models.IntegerField()
    matches_status = models.CharField(max_length=100)


class listmatches(models.Model):
    leaguename = models.CharField(max_length=950)
    opponent_one = models.CharField(max_length=100)
    opponent_two = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    pastscore_opone = models.IntegerField()
    pastscore_optwo = models.IntegerField()

    