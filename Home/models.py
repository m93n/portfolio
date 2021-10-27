from django.db import models


SKILL_DURATION=[
    ('Less than 3 months', 'Less than 3 months'),
    ('Between 3 and 6 months', 'Between 3 and 6 months'),
    ('Less than 1 year', 'Less than 1 year'),
    ('Between 1 and 2 years', 'Between 1 and 2 years'),
    ('Between 2 and 3 years', 'Between 2 and 3 years'),
    ('Between 3 and 4 years', 'Between 3 and 4 years'),
    ('Between 4 and 5 years', 'Between 4 and 5 years'),
    ('Between 5 and 6 years', 'Between 5 and 6 years'),
    ('Between 6 and 7 years', 'Between 6 and 7 years'),
    ('Between 7 and 8 years', 'Between 7 and 8 years'),
    ('Between 8 and 9 years', 'Between 8 and 9 years'),
    ('Between 9 and 10 years', 'Between 9 and 10 years'),
]

SKILL_VALUE={
    'Less than 3 months': '8.3',
    'Between 3 and 6 months': '16.7',
    'Less than 1 year': '25',
    'Between 1 and 2 years': '33.3',
    'Between 2 and 3 years': '41.7',
    'Between 3 and 4 years': '50',
    'Between 4 and 5 years': '58.3',
    'Between 5 and 6 years': '66.7',
    'Between 6 and 7 years': '75',
    'Between 7 and 8 years': '83.3',
    'Between 8 and 9 years': '91.7',
    'Between 9 and 10 years': '99',
}


class home_page(models.Model):
    name = models.CharField(max_length=50)
    category = models.TextField(default='')

class media_page(models.Model):
    cv = models.FileField(default='', upload_to='Home/static/Home')
    my_picture = models.ImageField(default='', upload_to='Home/static/Home/images')

class contact(models.Model):
    instagram = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    link0 = models.ForeignKey("contactLink", null=True, blank=True, on_delete=models.CASCADE, related_name="link0")
    link1 = models.ForeignKey("contactLink", null=True, blank=True, on_delete=models.CASCADE, related_name="link1")
    link2 = models.ForeignKey("contactLink", null=True, blank=True, on_delete=models.CASCADE, related_name="link2")

class contactLink(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.title

class about(models.Model):
    description = models.TextField()
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    address = models.TextField()
    languages = models.TextField()

class skill(models.Model):
    name = models.CharField(max_length=40)
    duration = models.CharField(max_length=40, choices=SKILL_DURATION)
    value = models.CharField(max_length=40, auto_created=True)

    def save(self):
        self.value = SKILL_VALUE[self.duration]
        super(skill, self).save()

    def __str__(self):
        return self.name

class workExp(models.Model):
    title = models.CharField(max_length=80)
    position = models.CharField(max_length=200)
    start = models.CharField(max_length=20)
    end = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title

class educationExp(models.Model):
    degree = models.CharField(max_length=80)
    position = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    start = models.CharField(max_length=20)
    end = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.degree
