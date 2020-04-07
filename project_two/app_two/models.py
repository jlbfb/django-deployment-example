from django.db import models

# Create your models here.
class States(models.Model):
    # state_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=3, unique=True)
    
    def __str__(self):
        return self.state

class Documents(models.Model):
    # document_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.title

class Headings(models.Model):
    # heading_id = models.AutoField(primary_key=True)
    document = models.ForeignKey(Documents, on_delete=models.CASCADE) # , default=1)
    heading = models.CharField(max_length=264)
    # metadata = models.CharField(max_length=500, blank=True)

    class Meta:
        unique_together = (('document', 'heading'),)

    def __str__(self):
        return self.heading

class SubHeadings(models.Model):
    # subheading_id = models.AutoField(primary_key=True)
    heading = models.ForeignKey(Headings, on_delete=models.CASCADE) # , default=1)
    subheading = models.CharField(max_length=264)
    # metadata = models.CharField(max_length=500, blank=True)

    class Meta:
        unique_together = (('subheading', 'heading'),)

    def __str__(self):
        return self.subheading

class Texts(models.Model):
    # text_id = models.AutoField(primary_key=True)
    subheading = models.ForeignKey(SubHeadings, on_delete=models.CASCADE)
    text = models.TextField()
    keywords = models.CharField(max_length=500, blank=True)
    # screenshots = models.IntegerField(default=0)

    def __str__(self):
        return self.text[0:30]

class Images(models.Model):
    # image_id = models.AutoField(primary_key=True)
    imageURL = models.URLField(unique=True)
    # caption = models.TextField()

    def __str__(self):
        return self.imageURL

class Relations(models.Model):
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    document = models.ForeignKey(Documents, on_delete=models.CASCADE)
    heading = models.ForeignKey(Headings, on_delete=models.CASCADE)
    subheading = models.ForeignKey(SubHeadings, on_delete=models.CASCADE)
    text = models.ForeignKey(Texts, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('state', 'document', 'heading', 'subheading', 'text'),)





