from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        # errors dictionary
        errors = {}
        
        # validating course name
        if len(postData['course_name']) == 0:
            errors['course_empty'] = "Name can't be empty"
        elif len(postData['course_name']) > 0 and len(postData['course_name']) < 5:
            errors['course_length'] = "Name must have at least 6 characters" 
            
        return errors            
            
class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __repr__(self):
        return f"Course: (ID: {self.id}) -> {self.name} -> {self.description}"

class DescriptionManager(models.Manager):
    def basic_validator(self, postData):
        # errors dictionary
        errors = {}
        
        # validating course description
        if len(postData['course_description']) == 0:
            errors['description_empty'] = "Description can't be empty"
        elif len(postData['course_description']) > 0 and len(postData['course_description']) < 16:
            errors['description_length'] = "Description must have at least 16 characters"   
            
        return errors  
    
class Description(models.Model):
    name = models.TextField()
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DescriptionManager()
    
    def __repr__(self):
        return f"Description: (ID: {self.id}) -> {self.name}" 


class CommentManager(models.Manager):
    def basic_validator(self, postData):
        # errors dictionary
        errors = {}

        # validating course comment
        if len(postData['course_comment']) == 0:
            print("Comentario vacio")
            errors['comment_empty'] = "Comment can't be empty"
        elif len(postData['course_comment']) > 0 and len(postData['course_comment']) < 16:
            errors['comment_length'] = "Comment must have at least 16 characters"   
            
        return errors            
            
class Comment(models.Model):
    comment = models.TextField()
    course = models.ForeignKey(Course, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()

    def __repr__(self):
        return f"Comment: (ID: {self.id}) -> {self.comment}"    