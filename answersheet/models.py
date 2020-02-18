import uuid
from django.db import models


class AnswerSheet(models.Model):
    def getImagePath(self, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return 'static/images/answer-sheets/' + filename

    image = models.ImageField(upload_to=getImagePath, null=True, blank=True)
    marks = models.FloatField(null=True, blank=True)



