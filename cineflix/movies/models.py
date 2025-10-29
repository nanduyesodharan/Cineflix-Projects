from django.db import models

import uuid

from multiselectfield import MultiSelectField

from embed_video.fields import EmbedVideoField

# Create your models here.

class BaseClass(models.Model):

    uuid=models.UUIDField(unique=True,default=uuid.uuid4)

    active_status=models.BooleanField(default=True)

    created_at=models.DateTimeField(auto_now_add=True)

    updated_at=models.DateTimeField(auto_now=True)

    class Meta:

        abstract=True

class IndustryChoices(models.TextChoices):

    MOLLYWOOD='Mollywood','Mollywood'

    HOLLYWOOD='Hollywood','Hollywood'

    BOLLYWOOD='Bollywood','Bollywood'

    TOLLYWOOD='Tollywood','Tollywood'

class CertificationChoices(models.TextChoices):

    A='A','A'

    UA='U/A','U/A'

    U='U','U'

    SC='SC','SC'

class GenreChoices(models.TextChoices):

    ACTION='Action','Action'

    ROMANTIC='Romantic','Romantic'

    THRILLER='Thriller','Thriller'

    COMEDY='Comedy','Comedy'

    HORROR='Horror','Horror'

class ArtistsChoices(models.TextChoices):

    MOHANLAL='Mohanlal','Mohanlal'

    MAMMOOTTY='Mammootty','Mammootty'

    NIVINPAULY='Nivin Pauly','Nivin Pauly'

class LanguageChoices(models.TextChoices):

    MALAYALAM='Malayalam','Malayalam'

    TAMIL='Tamil','Tamil'

    ENGLISH='English','English'

    TELUGU='Telugu','Telugu'

    KANNADA='Kannada','Kannada'

    HINDI='Hindi','Hindi'

class Movie(BaseClass):

    name=models.CharField(max_length=50)

    photo=models.ImageField(upload_to='movies/banner-images')

    description=models.TextField()

    release_date=models.DateField()

    industry=models.CharField(max_length=20,choices=IndustryChoices.choices)

    runtime=models.TimeField()

    certification=models.CharField(max_length=5,choices=CertificationChoices.choices)

    genre=MultiSelectField(choices=GenreChoices.choices)

    artists=MultiSelectField(choices=ArtistsChoices.choices)

    video=EmbedVideoField()

    tag=models.TextField()

    languages=MultiSelectField(choices=LanguageChoices.choices)

    class Meta:

        verbose_name='Movies'

        verbose_name_plural='Movies'

    def __str__(self):

        return f'{self.name}'