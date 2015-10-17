# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


# Views for Students

def students_list(request):
    students = (
        {'id': 1,
        'last_name': u'Деревенець',
        'first_name': u'Артем',
        'ticket': 235,
        'image': 'img/I_am.jpg'},
        {'id': 2,
        'last_name': u'Осінній',
        'first_name': u'Ілля',
        'ticket': 2123,
        'image': 'img/Illya.jpg'},
        {'id': 3,
        'last_name': u'Панченко',
        'first_name': u'Роман',
        'ticket': 223,
        'image': 'img/Roman.jpg'},
        )
    return render(request, 'students/students_list.html',{'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_journal(request,sid):
    return HttpResponse('<h1> Student %s in journal</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Groups


def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)

# Views for Journal

def journal(request):
    return HttpResponse('there will be the journal')
