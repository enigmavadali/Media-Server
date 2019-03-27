from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from videoapp.forms import DocumentForm, LectureForm, CommentForm
from videoapp.models import Document, History , Lecture , Like, Comment
from random import randint
from django.db.models import F
import subprocess
import os, shutil
from django.utils.timezone import localtime, now
from datetime import datetime
from datetime import date
from random import shuffle


def home(request):
    documents = Document.objects.all()
    lectures = Lecture.objects.all()
    return render(request, 'index.html', {'documents': documents, 'lectures': lectures})


def history(request):
    hist = History.objects.filter(user=request.user.username)
    docs = Document.objects.all()
    vids=[]
    for elem in hist:
        for doc in docs:
            if(elem.vid_id == doc.id):
                vids.append(doc)
                break
    vids.reverse()
    return render(request,'history-page.html',{'watched':vids})


def admin_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            uploadname = str(request.FILES['docfile'].name)
            uploadname = uploadname.replace(" ","_")
            foldername = uploadname.replace('.mp4','')
            instance = form.save(commit=False)
            #instance.id = randint(10**3, (10**4))
            instance.thumbnail = 'videos/admin/'+foldername+'/'+foldername+'.jpg'
            instance.mpdfile= 'videos/admin/'+foldername+'/'+foldername+'.mpd'
            #instance.mpdfile= 'videos/'+foldername+'/'+'.mpd'
            #instance.upload_date=datetime.datetime.now()
            instance.save()

            name1=uploadname.replace('.','_video_240.')
            name2=uploadname.replace('.','_video_360.')
            name3=uploadname.replace('.','_video_480.')
            name4=uploadname.replace('.','_video_720.')
            name_aud=uploadname.replace('.','_audio.')
            name_img=uploadname.replace('.mp4','.jpg')
            output_mpd_name=uploadname.replace('.mp4','.mpd')

            folder_path='media/videos/admin/'+foldername
            os.mkdir(folder_path)
            #shutil.move("media/videos/"+uploadname,"media/videos/"+foldername+"/"+uploadname)
            subprocess.call(['ffmpeg', '-i', "media/videos/admin/" + uploadname, '-ss', '00:00:03.000', '-vframes', '1', 'media/videos/admin/'+foldername+'/' + name_img])
            subprocess.call(["ffmpeg",'-i',"media/videos/admin/" +uploadname,'-s','426x240','-c:v','libx264','-b:v','640k','-g','90','-an','media/videos/admin/'+foldername+'/'+name1])
            subprocess.call(["ffmpeg",'-i',"media/videos/admin/" +uploadname,'-s','480x360','-c:v','libx264','-b:v','960k','-g','90','-an','media/videos/admin/'+foldername+'/'+name2])
            subprocess.call(["ffmpeg",'-i',"media/videos/admin/" +uploadname,'-s','640x480','-c:v','libx264','-b:v','1280k','-g','90','-an','media/videos/admin/'+foldername+'/'+name3])
            subprocess.call(["ffmpeg",'-i',"media/videos/admin/" +uploadname,'-s','1280x720','-c:v','libx264','-b:v','2560k','-g','90','-an','media/videos/admin/'+foldername+'/'+name4])
            subprocess.call(["ffmpeg",'-i',"media/videos/admin/" +uploadname,'-c:a','aac','-b:a','128k','-vn','media/videos/admin/'+foldername+'/'+name_aud])

            subprocess.call(['mp4box','-dash','10000','-rap','-profile','dashavc264:onDemand','-mpd-title','BBB','-out','media/videos/admin/'+foldername+'/'+output_mpd_name,'-frag','5000','media/videos/admin/'+foldername+'/'+name_aud,'media/videos/admin/'+foldername+'/'+name1,'media/videos/admin/'+foldername+'/'+name2,'media/videos/admin/'+foldername+'/'+name3,'media/videos/admin/'+foldername+'/'+name4])

            #checking duration
            result = subprocess.Popen(["ffprobe", "media/videos/admin/" + uploadname], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
            dur = [x for x in result.stdout.readlines() if b'Duration' in x]
            duration_string = dur[0].decode("utf-8")

            duration_string = duration_string[duration_string.find("Duration")+10:duration_string.find(".")]
            if(duration_string[0:2]=="00"):
                duration_string=duration_string[3:]
                #print(str2)
                instance.duration = duration_string

            else:
                #print(str)
                instance.duration = duration_string
            instance.save()
            #subprocess.call(["mp4box",'-dash','4000','-frag','4000','-out','media/videos/'+foldername+'/','-rap','-segment-name','segment_','media/videos/'+foldername+'/'+name_aud,'media/videos/'+foldername+'/'+name1,'media/videos/'+foldername+'/'+name2,'media/videos/'+foldername+'/'+name3,'media/videos/'+foldername+'/'+name4])
        return redirect("/home")
    else:
        form = DocumentForm() # A empty, unbound form
    return render(request, 'upload.html',{'form': form})

def professor_upload(request):
    #print("yaha")
    if request.method == 'POST':
        #print("yaha aa gaya")
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            uploadname = str(request.FILES['docfile'].name)
            uploadname = uploadname.replace(" ","_")
            foldername = uploadname.replace('.mp4','')
            instance = form.save(commit=False)
            #instance.id = randint(10**3, (10**4))
            instance.thumbnail = 'videos/professor/'+foldername+'/'+foldername+'.jpg'
            instance.mpdfile= 'videos/professor/'+foldername+'/'+foldername+'.mpd'
            #instance.mpdfile= 'videos/'+foldername+'/'+'.mpd'
            #instance.upload_date=datetime.datetime.now()
            instance.save()

            name1=uploadname.replace('.','_video_240.')
            name2=uploadname.replace('.','_video_360.')
            name3=uploadname.replace('.','_video_480.')
            name4=uploadname.replace('.','_video_720.')
            name_aud=uploadname.replace('.','_audio.')
            name_img=uploadname.replace('.mp4','.jpg')
            output_mpd_name=uploadname.replace('.mp4','.mpd')

            folder_path='media/videos/professor/'+foldername
            os.mkdir(folder_path)
            #shutil.move("media/videos/"+uploadname,"media/videos/"+foldername+"/"+uploadname)
            subprocess.call(['ffmpeg', '-i', "media/videos/professor/" + uploadname, '-ss', '00:00:03.000', '-vframes', '1', 'media/videos/professor/'+foldername+'/' + name_img])
            subprocess.call(["ffmpeg",'-i',"media/videos/professor/" +uploadname,'-s','426x240','-c:v','libx264','-b:v','640k','-g','90','-an','media/videos/professor/'+foldername+'/'+name1])
            subprocess.call(["ffmpeg",'-i',"media/videos/professor/" +uploadname,'-s','480x360','-c:v','libx264','-b:v','960k','-g','90','-an','media/videos/professor/'+foldername+'/'+name2])
            subprocess.call(["ffmpeg",'-i',"media/videos/professor/" +uploadname,'-s','640x480','-c:v','libx264','-b:v','1280k','-g','90','-an','media/videos/professor/'+foldername+'/'+name3])
            subprocess.call(["ffmpeg",'-i',"media/videos/professor/" +uploadname,'-s','1280x720','-c:v','libx264','-b:v','2560k','-g','90','-an','media/videos/professor/'+foldername+'/'+name4])
            subprocess.call(["ffmpeg",'-i',"media/videos/professor/" +uploadname,'-c:a','aac','-b:a','128k','-vn','media/videos/professor/'+foldername+'/'+name_aud])

            subprocess.call(['mp4box','-dash','10000','-rap','-profile','dashavc264:onDemand','-mpd-title','BBB','-out','media/videos/professor/'+foldername+'/'+output_mpd_name,'-frag','5000','media/videos/professor/'+foldername+'/'+name_aud,'media/videos/professor/'+foldername+'/'+name1,'media/videos/professor/'+foldername+'/'+name2,'media/videos/professor/'+foldername+'/'+name3,'media/videos/professor/'+foldername+'/'+name4])
            #subprocess.call(["mp4box",'-dash','4000','-frag','4000','-out','media/videos/'+foldername+'/','-rap','-segment-name','segment_','media/videos/'+foldername+'/'+name_aud,'media/videos/'+foldername+'/'+name1,'media/videos/'+foldername+'/'+name2,'media/videos/'+foldername+'/'+name3,'media/videos/'+foldername+'/'+name4])

            #checking duration
            result = subprocess.Popen(["ffprobe",  "media/videos/professor/" + uploadname], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
            dur = [x for x in result.stdout.readlines() if b'Duration' in x]
            duration_string = dur[0].decode("utf-8")

            duration_string = duration_string[duration_string.find("Duration")+10:duration_string.find(".")]
            if(duration_string[0:2]=="00"):
                duration_string=duration_string[3:]
                #print(str2)
                instance.duration = duration_string
            else:
                #print(str)
                instance.duration = duration_string
            instance.save()
        return redirect("/home")
    else:
        form = LectureForm() # A empty, unbound form
    return render(request, 'upload.html',{'form': form})


def play(request, ID):
    if(request.user.is_authenticated):
        Id = ID
        obj_type = "Doc"
        obj = Document.objects.get(pk=Id)
        Document.objects.filter(pk=Id).update(views=F('views') + 1)
        hist = History.objects.filter(user=request.user.username)
        for elem in hist:
            if elem.vid_id == ID:
                elem.delete()
                his_obj = History()
                his_obj.user = request.user.username
                his_obj.vid_id = Id
                his_obj.tag = obj.tag
                his_obj.save()
                break
        else:
            m, created = History.objects.get_or_create(user=request.user.username, vid_id=ID, tag=obj.tag)
            m.save()
        recommended_docs,recommended_hist = recommend_algo(request,ID,obj)
        all_comments = Comment.objects.filter(v_id=ID , obj_type=obj_type)
        comment_form = CommentForm()
        check_value = True
        #documents = Document.objects.all()
        #lectures = Lecture.objects.all()
        return render(request, 'PlayVid.html', {'obj': obj, 'recommended_docs': recommended_docs, 'recommended_hist': recommended_hist,'all_comments':all_comments, 'comment_form':comment_form,'check_value':check_value,'obj_type':obj_type })
    else:
        return HttpResponseRedirect(reverse('videoapp:home'))


def recommend_algo(request,ID,obj):
    final_list_hist=[]
    final_list_doc=[]
    temp=[]
    final_list_hist.clear()
    final_list_doc.clear()
    temp.clear()
    video_hist = History.objects.filter(user=request.user.username)
    doc_hist = Document.objects.all()
    #print(type(list(doc_hist)))
    doc_hist=list(doc_hist)

    video_hist.reverse()
    count_hist=4
    for elem in video_hist:
        if elem.vid_id != ID and count_hist>0:
            temp.append(elem)
            count_hist-=1
    shuffle(temp)
    for i in temp:
        for j in doc_hist:
            if i.vid_id == j.id:
                final_list_hist.append(j)

    doc_hist.sort(key=lambda x: x.views, reverse=True)
    current_tag = obj.tag
    count_doc= 10 - len(final_list_hist)
    for elem in doc_hist:
        if elem.tag == current_tag and elem.id!=ID and count_doc>0 and elem not in final_list_hist:
            final_list_doc.append(elem)
            count_doc-=1
    if count_doc>0:
        for elem in doc_hist:
            if elem not in final_list_doc and count_doc>0 and elem.id != ID and elem not in final_list_hist:
                final_list_doc.append(elem)
                count_doc-=1
    shuffle(final_list_doc)
    return final_list_doc,final_list_hist

def play_lecture(request, ID):
    Id = ID
    obj_type = "Lec"
    obj = Lecture.objects.get(pk=Id)
    Lecture.objects.filter(pk=Id).update(views=F('views') + 1)
    lectures = Lecture.objects.all()
    tem = localtime(now()).date()
    current_datetime = datetime.now()
    current_hour = current_datetime.hour
    current_min = current_datetime.minute
    # his_obj = History()
    # his_obj.user = request.user.username
    # his_obj.vid_id = Id
    # his_obj.tag = obj.tag
    # his_obj.save()
    # if obj.Start_date < obj.antim_tarikh:
    #     obj.is_time_started = True
    # elif obj.Start_hour <= tem.hour and obj.Start_min <= tem.minute and obj.End_hour >= tem.hour and obj.End_min >= tem.minute:
    #     obj.is_time_started = True

    # obj.is_time_started = False
    if obj.start_date <= tem and obj.antim_tarikh >= tem:
        if (obj.start_hour <= current_hour and obj.start_min <= current_min) and (
                obj.end_hour >= current_hour and obj.end_min >= current_min):
             obj.is_time_started = True

    list_of_students = obj.reg_students
    check_value = False
    if request.user.username in list_of_students:
        check_value= True
    #print(check_value)
    all_comments = Comment.objects.filter(v_id=ID,obj_type=obj_type)
    comment_form = CommentForm()

    return render(request, 'PlayVid.html', {'obj': obj,'check_value':check_value,'obj_type':obj_type,'all_comments':all_comments, 'comment_form':comment_form})

def reg_student_for_video(request, ID):
    obj = Lecture.objects.get(pk=ID)
    obj.reg_students.append(request.user.username)
    check_value= True
    obj.save()
    return render(request, 'PlayVid.html', {'obj': obj,'check_value':check_value})

def comment(request, obj_type ,ID):
    obj = Document.objects.get(pk=ID)
    if request.method == 'POST':
        #print("yaha aa gaya")
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user.username
            instance.v_id = ID
            instance.obj_type = obj_type
            instance.save()
            # all_comments = Comment.objects.filter(v_id=ID)
            # comment_form = CommentForm()
            # return render(request, 'PlayVid.html', {'obj': obj, 'all_comments':all_comments, 'comment_form':comment_form})
    #url_togo = "home/"+str(ID)
    return HttpResponseRedirect(reverse('videoapp:play',args=(ID,)))

def like(request, ID):
    if (request.user.is_authenticated):
        liked = Like.objects.filter(vid_id=ID)
        for people in liked:
            #print(people.username,request.user.username)
            if people.username == request.user.username:
                break
        else:
            m, created = Like.objects.get_or_create(username=request.user.username, vid_id=ID, liked=True)
            m.save()
            Document.objects.filter(pk=ID).update(likes=F('likes') + 1)
        #url_togo = "home/"+str(ID)
        return HttpResponseRedirect(reverse('videoapp:play',args=(ID,)))
        #return render(request, 'PlayVid.html', {'obj': obj, 'documents': documents})
    else:
        return HttpResponseRedirect(reverse('videoapp:home'))


def remove_vid(request,ID):
    #print("yeh function hai")
    obj = Document.objects.get(pk=ID)
    the_file = obj.docfile.name
    #print(type(the_file))
    the_file = the_file.replace(' ','_')
    the_folder = the_file.replace('.mp4','')
    #print(type(the_folder))
    #subprocess.call(['rmdir','-r','media/'+the_folder])
    #subprocess.call(['rm','-r','media/'+the_file])
    os.remove('media/'+the_file)
    shutil.rmtree('media/'+the_folder)
    obj.delete()
    documents = Document.objects.all()
    return HttpResponseRedirect(reverse('videoapp:home'))

# def view_all(request):
#     documents = Document.objects.all()
#     return render(request, "video_history.html",{'documents': documents} )
