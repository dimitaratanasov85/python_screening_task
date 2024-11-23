from django.db import models

class Request(models.Model):
    user = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request from {self.user} - {self.name}"

class CalculationResult(models.Model):
    request = models.ForeignKey(Request, related_name='results', on_delete=models.CASCADE)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for request {self.request.name}: {self.result}"
