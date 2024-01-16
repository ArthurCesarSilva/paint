from django.db import models




class Color(models.Model):
    color_name = models.CharField(max_length=200)

    inverted_color = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    def like(self):
        return self.likes
    def cor(self):
        return self.color_name
    def corinvetida(self):
        return self.inverted_color
     