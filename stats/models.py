from django.db import models


# Create your models here.
class TestCase(models.Model):
    endpoint_url = models.CharField(max_length=300)
    headers = models.CharField(max_length=4000)
    params = models.CharField(max_length=4000)
    expected_response_code = models.IntegerField()
    response_code = models.IntegerField()
