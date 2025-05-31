from django.db import models

class Route(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='active')  # e.g. active/inactive
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Stop(models.Model):
    route = models.ForeignKey(Route, related_name='stops', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField()  # Order of the stop in the route

    def __str__(self):
        return f"{self.name} (Order: {self.order})"