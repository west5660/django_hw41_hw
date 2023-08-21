from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello world</h1>')
def tatan(request):
    return HttpResponse('index.html')
def home(request):
    return render(request,'index.html')
def djec(request,id):
    id=int(id)
    month=['ДЖЕК','Роуз','Капитан','Титаник','Айсберг']
    workers=['Джек молодой и любит Роуз','Роуз молода и любит Джека,но он умрет((','Опытный моряк, но очень упертый и самоуверенный. Это их и погубило','Вершина инженерной мыси того времени, шикарный лайнер и элитное место. Хоть и с плохим концом','Пресная вода в твердом агрегатном состоянии, холодная и в основном белая']
    role=['В ролях Леонардо Ди Каприо','В ролях Роза Дьюитт Бьюкейтер','В ролях Эдвард Джон Смит','В ролях корабля и графика','В ролях графика конечно, но все же айсберг']
    img=['img/img.png','img/img_2.png','img/img_3.png','img/img_4.png','img/img_5.png']
    link=['https://ru.wikipedia.org/wiki/Доусон,_Джозеф','https://titanic.fandom.com/wiki/Rose_DeWitt_Bukater','https://titanicsociety.ru/captain_smith_mify/','https://ru.wikipedia.org/wiki/Титаник','https://dzen.ru/a/YdlactUu9nM6ZWr1']
    data={'k1':month[id],'k2':workers[id],'k3':role[id],'k4':img[id],'k5':link[id]}
    return render(request,'persona.html', context=data)