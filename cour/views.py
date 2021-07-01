from django.http.response import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from cour.models import Comment, Course, Description
from django.contrib import messages

# Create your views here.
def index(request):
    # getting courses
    courses = Course.objects.all()
    
    context = {
        'all_courses': courses
    }
    
    return render(request, "index.html", context)

def new(request):    
    # getting form variables
    course_name = request.POST['course_name']
        
    course_description = request.POST['course_description']
    
    # errors dict is received
    errors = Course.objects.basic_validator(request.POST)
    # adding description errors, if they exist
    errors.update(Description.objects.basic_validator(request.POST))
    
    # if there are errors
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        
        form_data = {
            'course_name': course_name,
            'course_description': course_description,
        }
        
        request.session['form_data'] = form_data
    else:
        # creating course
        this_course = Course.objects.create(name=course_name)
        
        # creating description
        Description.objects.create(name=course_description, course=this_course)    
        
        if 'form_data' in request.session:
            del request.session['form_data']
            
        messages.success(request, "Course successfully created")
    
    return redirect(reverse("my_index"))

def view(request, course_id):
    # getting course
    this_course = Course.objects.get(id=course_id)
    
    # getting comments
    all_comments = Comment.objects.filter(course=Course.objects.get(id=course_id))
    
    context = {
        'this_course': this_course,
        'all_comments': all_comments
    }
    
    return render(request, "comment.html", context)

def comment(request, course_id):
    # getting current course
    this_course= Course.objects.get(id=course_id)
    
    # getting form variables
    course_comment = request.POST['course_comment']
    
    # errors dict is received
    errors = Comment.objects.basic_validator(request.POST)
    
    # if there are errors
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        
        form_data = {
            'course_comment': course_comment
        }
        
        request.session['form_data'] = form_data
    else:
        # adding comment
        Comment.objects.create(comment=course_comment, course= this_course)
        
        if 'form_data' in request.session:
            del request.session['form_data']
            
        messages.success(request, "Comment has been successfully posted")
        
    return redirect(reverse("my_view", args=(course_id,)))
    
def delete(request):
    # getting form variable
    course_id= request.POST['course_id']
    
    # getting current course
    this_course= Course.objects.get(id=course_id)
    
    print (this_course) 
       
    this_course.delete()
    
    context = {
        'all_courses': Course.objects.all()
    }
    
    return render(request, "courses.html", context)