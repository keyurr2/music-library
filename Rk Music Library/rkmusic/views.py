from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.templatetags.staticfiles import static
import os
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.template import loader, Context
from django.http import StreamingHttpResponse
from django.views.decorators.cache import cache_page

real_path = os.path.dirname(os.path.realpath(__file__));
staticPath = os.path.join(real_path, "static")
libraryPath = os.path.join(staticPath, "library")
musicPath = os.path.join(libraryPath, "music")
# Create your views here.

# t = loader.get_template('rkmusic/audio.html') # or whatever
# buffer = ' ' * 1024

@cache_page(60 * 15)
def index(request):
	return render(request, 'rkmusic/index.html', {})

@cache_page(60 * 15)
def dirLevelOne(request, name):
	if name == 'contactus':
		if request.method == "GET":
			return render(request, 'rkmusic/contacts.html', {})
		elif request.method == "POST":
			name,email,message = request.POST.get('name'), request.POST.get('email'),request.POST.get('message')
			SendMail(name,email,message)
		return redirect('index')
	elif name:	
		name = name.encode('ascii','ignore') if name else ''	
		dataPath = os.path.join(libraryPath,"music",name)
		if os.path.exists(dataPath):
			albums = os.listdir(dataPath)
			dataArray = prepareData(albums)
			return render(request, 'rkmusic/gallery.html', {'dataArray' : dataArray, 'name' : name})
		return redirect('index')
	else:
		return redirect('index')	


@cache_page(60 * 15)
def dirLevelTwo(request, name, dirname):
	dirPath = dirname.replace ("-", " ").title()
	name = name if name else ''	
	songPath = os.path.join(musicPath,name,dirPath)	
	# print(request.META['HTTP_HOST'])
	if os.path.exists(songPath):
		extensions = {".jpg", ".png", ".gif", ".jpeg"}
		songs = [f for f in os.listdir(songPath) if f.endswith('mp3')]
		dataArray = prepareData2(songs, name, dirPath)
		return render(request, 'rkmusic/audio.html', {'dataArray' : dataArray, 'dirPath' : dirPath})
	return redirect('index')

def audio(request):
	dataPath = os.path.join(real_path, "static","library","music")
	albums = os.listdir(dataPath)
	dataArray = prepareData(albums)	
	return render(request, 'rkmusic/gallery.html', {'rk' : dataArray})

def prepareData2(albums, name, dirPath):
	dataArray = []
	counter,port = 1,9001
	for a in albums:
		# if counter % 9 == 0:
			# port = 9001
			# counter = 1
		data = {}
		data['name'] = str(a.encode('ascii','ignore'))
		# data['url'] = "http://localhost:"+str(port)+"/static/library/music/"+name+"/"+dirPath+"/"+str(a.encode('ascii','ignore'))
		# data['url'] = "http://localhost:3000/"+name+"/"+dirPath+"/"+str(a.encode('ascii','ignore'))
		data['url'] = "http://192.168.4.125:3020/"+name+"/"+dirPath+"/"+str(a.encode('ascii','ignore'))
		data['counter'] = counter
		dataArray.append(data) 
		# counter = counter + 1
		# port = port + 1
	return dataArray
					

def prepareData(albums):	
	dataArray = []
	counter = 1
	for a in albums:
		if counter % 3 == 0:
			counter = 0
		data = {}
		data['name'] = str(a.encode('ascii','ignore'))
		data['counter'] = counter
		dataArray.append(data) 
		counter = counter + 1
	return dataArray

def SendMail(name, email, message):
	title = "RK Music Player"
	email_message = "Thanks for contactus.\nYour message\n"+message+"\nwill be useful to us for improving app."
	send_mail(title, email_message, 'RK Music Player <'+settings.EMAIL_HOST_USER+'>',
    [email, settings.DEFAULT_TO_EMAIL], fail_silently=False)
