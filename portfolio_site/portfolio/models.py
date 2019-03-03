from django.db import models

# Create your models here.
class WorkExperiences(models.Model):
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date =  models.DateTimeField('Start Date')
    end_date = models.DateTimeField('End Date')
    current_job = models.BooleanField()

    # add image of the companies logo eventually

    job_description = models.TextField()

    def __str__(self):
        return self.job_title

class Bio(models.Model):
    title = models.CharField(max_length=200)
    current_job = models.CharField(max_length=200)
    current_company = models.CharField(max_length=200)
    description = models.TextField()
    skill_summary = models.TextField()

    def __str__(self):
        return self.title

class Projects(models.Model):
    project_name = models.CharField(max_length=200)
    team = models.BooleanField()
    teamates = models.CharField(max_length=200)

    def __str__(self):
        return self.project_name

class Education(models.Model):
    school_name = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)

    def __str__(self):
        return self.school_name

class AwardsCertifications(models.Model):
    certificate_name = models.CharField(max_length=200)
    certificate_organization = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.certificate_name

class VolunteerExperience(models.Model):
    job_title = models.CharField(max_length=200)
    organization_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date =  models.DateTimeField('Start Date')
    end_date = models.DateTimeField('End Date')
    current = models.BooleanField()

    # add image of the organizations logo eventually

    job_description = models.TextField()

    def __str__(self):
        return self.job_title