from django.shortcuts import render

# Create your views here.
from django.shortcuts import *
from pyy import pc
from home import models
import datetime
import random
today="20191202"                                                                 #我修改过
#today = datetime.datetime.now().strftime("%Y%m%d")
print(today)
def collect (request):
    stuinfo_dic={}
    if request.method =="POST":
        t1 = models.stuinfo.objects.filter(username=request.POST['lg']).exists()
        if t1:
            return render(request, 'collect.html',{'war':'该用户已经存在'})
        stuinfo_dic={'username':request.POST['lg'] ,
                'password':request.POST['pass'] ,
                'email': request.POST['emi'],
                'intro': request.POST['txt'],
                'sex': request.POST['sex'],
                'grade': request.POST['grade'],
                'phone': request.POST['phone'],
                'address': request.POST['address']}
        models.stuinfo.objects.create( **stuinfo_dic )
        return render(request,'index.html')
    return render(request,'collect.html')
    # HttpResponse与render的区别在于，前者只用于返回文本信息，
    # 而render即其字面意思“渲染”，意思是使用context渲染html页面后返回。
def login(request):
    if request.method=="POST":
        log_name=request.POST['user']
        log_pas=request.POST['pass']
        t0=models.stuinfo.objects.filter(username=log_name).exists()
        if t0:
            t01=models.stuinfo.objects.filter(username=log_name).filter(password=log_pas).exists()
            if t01==False:
                return render(request, 'index.html',{'war':'密码错误'})
        else:
            return render(request, 'index.html', {'warr': '用户不存在'})
        t1 = models.stuinfo.objects.filter(username=log_name).filter(password=log_pas).exists()
        if t1:
            homedata= models.stuinfo.objects.all().filter(username=log_name)
            print(homedata)
            print(type(homedata))
            return render(request,'Home.html',{'homedata':homedata})
    return render(request,'index.html')
def Home(request):
    pass
def test(request):
    user_list_obj = models.stuinfo.objects.all()
    data_obj = models.scuinfo_content.objects.all()
    data_obj2 =models.scuinfo_pic.objects.all()
    data_obj31 = models.main_pic.objects.filter(cday=today).first()
    data_obj3=models.main_pic.objects.filter(cday=today)[1:7]
    #print(data_obj2)
    return render(request,'test.html',{'lit':user_list_obj,'date':data_obj,'data2':data_obj2,'data3':data_obj3,'data31':data_obj31})
def page_of_scu(request):
    t1=models.main_pic.objects.filter(cday=today).exists()
    t2=models.scuinfo_pic.objects.filter(cday=today).exists()
    t3=models.scuinfo_content.objects.filter(cday=today).exists()
    if t1 and t2 and t3 :#如果数据库有目前的数据，就直接从数据库取
        data_obj = models.scuinfo_content.objects.filter(cday=today)[:11]
        data_obj2 = random.sample(list(models.scuinfo_pic.objects.filter(cday=today)), 2)
        data_obj31 = models.main_pic.objects.filter(cday=today).first()
        data_obj3 = models.main_pic.objects.filter(cday=today)[1:7]
        if request.method == 'GET':
            if str(request.GET.get('year')) != 'None' and str(request.GET.get('month')) != 'None' and str(request.GET.get('day')) != 'None':
                try:
                    if (bool(int(request.GET.get('year'))) and bool(int(request.GET.get('month'))) and bool(int(request.GET.get('day'))))==False:
                        pass
                except Exception as e:
                    return render(request,'page_of_scu.html',{'warnning':'注入警告！！！！！','date': data_obj, 'date2': data_obj2, 'date3': data_obj3, 'date31': data_obj31})
                ser = str(request.GET.get('year')) + str(request.GET.get('month')) + str(request.GET.get('day'))
                t11 = models.main_pic.objects.filter(cday=ser).exists()
                t22 = models.scuinfo_pic.objects.filter(cday=ser).exists()
                t33 = models.scuinfo_content.objects.filter(cday=ser).exists()
                if (t11 and t22 and t33)==False:  #如果数据库没有要查询的数据，就发出警告然后显示今天的信息
                    return render(request, 'page_of_scu.html',
                                  {'date': data_obj, 'date2': data_obj2,
                                   'date3': data_obj3,
                                   'date31': data_obj31,
                                   'warnning':'您要找的新闻数据不存在'
                                   })
                data_obj = models.scuinfo_content.objects.filter(cday=ser)
                data_obj2 = random.sample(list(models.scuinfo_pic.objects.filter(cday=ser)), 2)
                data_obj31 = models.main_pic.objects.filter(cday=ser).first()
                data_obj3 = models.main_pic.objects.filter(cday=ser)[1:7]
                # randon.sample 选取列表、集合、元组、字典；但是查询时返回的是dicts
                # TypeError: Population must be a sequence or set.  For dicts, use list(d).
                # QueryDict 实现了Python字典数据类型的所有标准方法，因为它是字典的子类。
                return render(request, 'page_of_scu.html',
                              {'date': data_obj, 'date2': data_obj2, 'date3': data_obj3, 'date31': data_obj31})
        return render(request, 'page_of_scu.html',{'date': data_obj, 'date2': data_obj2, 'date3': data_obj3, 'date31': data_obj31})
    dataa = pc.data()
    dataaa= pc.data1()
    dataaaa=pc.data2()
    scuinfo_pic_dic={}
    scuinfo_pic_content_dic={}
    scuinfo_main_pic_dic={}
    for items in  dataa:
        #print(items)
        scuinfo_content_dic={
            'href_1':items['href'],
            'tit_1':items['title'],
            'date_1':items['data'],
            'cday':today
        }
        models.scuinfo_content.objects.get_or_create( **scuinfo_content_dic)
    for items in  dataaa:
        #print(items)
        scuinfo_pic_dic={
            'hre_f':items['hre_f'],
            'titl_e':items['titl_e'],
            'pic_url':items['pic_url'],
            'cday':today
        }
        #print(scuinfo_pic_dic)
        models.scuinfo_pic.objects.get_or_create( **scuinfo_pic_dic)
    for items in  dataaaa:
        #print(items)
        scuinfo_main_pic_dic={
            'hre_f':items['hre_f'],
            'titl_e':items['titl_e'],
            'pic_url':items['pic_url'],
            'cday':today
        }
        #print(scuinfo_main_pic_dic)
        models.main_pic.objects.get_or_create( **scuinfo_main_pic_dic)
    if request.method=='GET':
        if str(request.GET.get('year'))!='None' and str(request.GET.get('month'))!='None' and str(request.GET.get('day'))!='None':
            ser=str(request.GET.get('year'))+str(request.GET.get('month'))+str(request.GET.get('day'))
            data_obj=models.scuinfo_content.objects.filter(cday=ser)
            data_obj2=random.sample(list(models.scuinfo_pic.objects.filter(cday=ser)),2)
            data_obj31 = models.main_pic.objects.filter(cday=ser).first()
            data_obj3 = models.main_pic.objects.filter(cday=ser)[1:7]
            #randon.sample 选取列表、集合、元组、字典；但是查询时返回的是dicts
            #TypeError: Population must be a sequence or set.  For dicts, use list(d).
            #QueryDict 实现了Python字典数据类型的所有标准方法，因为它是字典的子类。
            return render(request,'page_of_scu.html',{'date':data_obj,'date2':data_obj2,'date3':data_obj3,'date31':data_obj31})
    data_obj=models.scuinfo_content.objects.filter(cday=today)[:11]
    data_obj2 = random.sample(list(models.scuinfo_pic.objects.filter(cday=today)),2)
    data_obj31 =models.main_pic.objects.filter(cday=today).first()
    data_obj3 = models.main_pic.objects.filter(cday=today)[1:7]
    return render(request, 'page_of_scu.html',{'date': data_obj, 'date2': data_obj2, 'date3': data_obj3, 'date31': data_obj31})
