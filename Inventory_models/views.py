from django.shortcuts import render
from threading import Thread
from Inventory_models.server import start_server
from Inventory_models.client import receive_and_print_data
from Inventory_models.models import Recieved_data,line_graph_data,Cylinder,Conical
import schedule
import time,math
from django.http import JsonResponse

# running client.py and server.py page
th = Thread(target=start_server, args=('192.168.1.16', 12356))#server.py
th.daemon = True
th.start()

th2 = Thread(target=receive_and_print_data, args=('192.168.1.16,', 12356))#client.py
th2.daemon = True
th2.start()


def index(request):
    return render(request, 'index.html')

def config(request):
    return render(request, 'config.html')

def Tag1(request):
    return render(request, 'tag1.html')
def Tag2(request):
    return render(request, 'tag2.html')
def Tag3(request):
    return render(request, 'tag3.html')
def Tag4(request):
    return render(request, 'tag4.html')
def Tag5(request):
    return render(request, 'tag5.html')
def Tag6(request):
    return render(request, 'tag6.html')
def Tag7(request):
    return render(request, 'tag7.html')
def Tag8(request):
    return render(request, 'tag8.html')
# def data():

#     a=list(Recieved_data.objects.all().values())
#     all_tag_values = [value for data_dict in a for key, value in data_dict.items() if key.startswith('tag')]#storing all the tag values in a single list
#     print("===============",all_tag_values)
# if __name__ == "__main__":
#     while True:
#         data()
#         time.sleep(6)
def data(request):
    a = list(Recieved_data.objects.all().values())
    all_tag_values = [value for data_dict in a for key, value in data_dict.items() if key.startswith('tag')]
    # print("===============", all_tag_values)
    # return render(request, 'index.html', {'all_tag_values': all_tag_values})
    return JsonResponse({'all_tag_values':all_tag_values})   
# Schedule the data() function to run every 6 seconds
# schedule.every(6).seconds.do(data)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
def line_data(request):
    a = list(line_graph_data.objects.all().values())
    # all_tag_values = [value for data_dict in a for key, value in data_dict.items() if key.startswith('tag')]
    # print("===============",a)
    tag1_values = [entry['tag1'] for entry in a]
    tag2_values = [entry['tag2'] for entry in a]
    tag3_values = [entry['tag3'] for entry in a]
    tag4_values = [entry['tag4'] for entry in a]
    tag5_values = [entry['tag5'] for entry in a]
    tag6_values = [entry['tag6'] for entry in a]
    tag7_values = [entry['tag7'] for entry in a]
    tag8_values = [entry['tag8'] for entry in a]


    if request.method == 'GET':
        data = Cylinder.objects.all().order_by('id').values()
        tanks_volume = [item['tanks_volume'] for item in data if item['tanks_volume']]

    if request.method == 'GET':
        data = Conical.objects.all().order_by('id').values()
        tanks_volume2 = [item['tanks_volume'] for item in data if item['tanks_volume']]
        # print(Product_name)
    # print("-------------------",tag1_values)
    # return render(request, 'index.html', {'all_tag_values': all_tag_values})
    return JsonResponse({'tag1_values':tag1_values,'tag2_values':tag2_values,'tag3_values':tag3_values,'tag4_values':tag4_values,
                        'tag5_values':tag5_values,'tag6_values':tag6_values,'tag7_values':tag7_values,'tag8_values':tag8_values,
                        'tanks_volume':tanks_volume,'tanks_volume2':tanks_volume2})
def alltag(request):
    return render(request, 'alltag.html')

def cylindrical(request):
    if request.method=='POST':
        # print("aaaaaaaaaaaaaaah")
        diameter=request.POST.get('diameter1d1')
        height=request.POST.get('height1h1')
        tank_name=request.POST.get('tank_name')
        # print(tank_name)
        product=request.POST.get('product')
        volume_in_liters = (math.pi * (float(diameter)/2)**2 * float(height))*1000

        if tank_name=='Tank1':
            if Cylinder.objects.filter(pk=1).exists():
                
                print(volume_in_liters)
        # If it exists, update its fields
                Cylinder.objects.filter(pk=1).update(diameter=diameter, height=height, product=product,tanks_volume=volume_in_liters)
            else:
        # If it doesn't exist, create a new Cylinder object with id 1
                Cylinder.objects.create(pk=1, diameter=diameter, height=height, product=product)
        elif tank_name=='Tank2':
            if Cylinder.objects.filter(pk=2).exists():
                Cylinder.objects.filter(pk=2).update(diameter=diameter, height=height, product=product,tanks_volume=volume_in_liters)
            else:
                Cylinder.objects.create(pk=2, diameter=diameter, height=height, product=product)
        elif tank_name=='Tank3':
            if Cylinder.objects.filter(pk=3).exists():
                Cylinder.objects.filter(pk=3).update(diameter=diameter, height=height, product=product,tanks_volume=volume_in_liters)
            else:
                Cylinder.objects.create(pk=3, diameter=diameter, height=height, product=product)
        elif tank_name=='Tank4':
            if Cylinder.objects.filter(pk=4).exists():
                Cylinder.objects.filter(pk=4).update(diameter=diameter, height=height, product=product,tanks_volume=volume_in_liters)
            else:
                Cylinder.objects.create(pk=4, diameter=diameter, height=height, product=product)                
        elif tank_name=='Tank5':
            if Cylinder.objects.filter(pk=5).exists():
                Cylinder.objects.filter(pk=5).update(diameter=diameter, height=height, product=product,tanks_volume=volume_in_liters)
            else:
                Cylinder.objects.create(pk=5, diameter=diameter, height=height, product=product)
        elif tank_name=='Tank6':
            if Cylinder.objects.filter(pk=6).exists():
                Cylinder.objects.filter(pk=6).update(diameter=diameter, height=height, product=product,tanks_volume=volume_in_liters)
            else:
                Cylinder.objects.create(pk=6, diameter=diameter, height=height, product=product)
        elif tank_name=='Tank7':
            if Cylinder.objects.filter(pk=7).exists():
                Cylinder.objects.filter(pk=7).update(diameter=diameter, height=height, product=product,tanks_volume=volume_in_liters)
            else:
                Cylinder.objects.create(pk=7, diameter=diameter, height=height, product=product)
        elif tank_name=='Tank8':
            if Cylinder.objects.filter(pk=8).exists():
                Cylinder.objects.filter(pk=8).update(diameter=diameter, height=height, product=product,tanks_volume=volume_in_liters)
            else:
                Cylinder.objects.create(pk=8, diameter=diameter, height=height, product=product)    

        
    return render(request,'cylindrical.html')

def conical(request):
    if request.method=='POST':
        # print("aaaaaaaaaaaaaaah")
        diameter=request.POST.get('diameter2d1')
        diameter2=request.POST.get('diameter2d2')
        height=float(request.POST.get('height2h1'))
        height2=float(request.POST.get('height2h2'))
        h=height+height2
        tank_name=request.POST.get('tank_name')
        # prfloat(tank_name)
        product=request.POST.get('product')
        radius = float (diameter) / 2
        radius2 = float(diameter2) / 2
        volume_in_liters = (1/3) * math.pi * h * (radius**2 + radius * radius2 + radius2**2) * 1000

        if tank_name=='Tank1':
            if Conical.objects.filter(pk=1).exists():
                print(volume_in_liters)
        # If it exists, update its fields
                Conical.objects.filter(pk=1).update(diameter1=diameter,diameter2=diameter2, height1=height, height2=height2, product=product,tanks_volume=volume_in_liters)
            else:
        # If it doesn't exist, create a new Conical object with id 1
                Conical.objects.create(pk=1, diameter1=diameter, height1=height, product=product)
        elif tank_name=='Tank2':
            if Conical.objects.filter(pk=2).exists():
                Conical.objects.filter(pk=2).update(diameter1=diameter,diameter2=diameter2, height1=height, height2=height2, product=product,tanks_volume=volume_in_liters)
            else:
                Conical.objects.create(pk=2, diameter1=diameter, height1=height, product=product)
        elif tank_name=='Tank3':
            if Conical.objects.filter(pk=3).exists():
                Conical.objects.filter(pk=3).update(diameter1=diameter,diameter2=diameter2, height1=height, height2=height2, product=product,tanks_volume=volume_in_liters)
            else:
                Conical.objects.create(pk=3, diameter1=diameter, height1=height, product=product)
        elif tank_name=='Tank4':
            if Conical.objects.filter(pk=4).exists():
                Conical.objects.filter(pk=4).update(diameter1=diameter,diameter2=diameter2, height1=height, height2=height2, product=product,tanks_volume=volume_in_liters)
            else:
                Conical.objects.create(pk=4, diameter1=diameter, height1=height, product=product)                
        elif tank_name=='Tank5':
            if Conical.objects.filter(pk=5).exists():
                Conical.objects.filter(pk=5).update(diameter1=diameter,diameter2=diameter2, height1=height, height2=height2, product=product,tanks_volume=volume_in_liters)
            else:
                Conical.objects.create(pk=5, diameter1=diameter, height1=height, product=product)
        elif tank_name=='Tank6':
            if Conical.objects.filter(pk=6).exists():
                Conical.objects.filter(pk=6).update(diameter1=diameter,diameter2=diameter2, height1=height, height2=height2, product=product,tanks_volume=volume_in_liters)
            else:
                Conical.objects.create(pk=6, diameter1=diameter, height1=height, product=product)
        elif tank_name=='Tank7':
            if Conical.objects.filter(pk=7).exists():
                Conical.objects.filter(pk=7).update(diameter1=diameter,diameter2=diameter2, height1=height, height2=height2, product=product,tanks_volume=volume_in_liters)
            else:
                Conical.objects.create(pk=7, diameter1=diameter, height1=height, product=product)
        elif tank_name=='Tank8':
            if Conical.objects.filter(pk=8).exists():
                Conical.objects.filter(pk=8).update(diameter1=diameter,diameter2=diameter2, height1=height, height2=height2, product=product,tanks_volume=volume_in_liters)
            else:
                Conical.objects.create(pk=8, diameter1=diameter, height=height, product=product)    

        
    return render(request,'conical.html')

def cylindrical_data(request):
    if request.method == 'GET':
        data = Cylinder.objects.all().order_by('id').values()
        Product_name = [item['product'] for item in data if item['product']]
        print(Product_name)
        return JsonResponse({'Product_name': Product_name})
    
    
def conical_data(request):
    if request.method == 'GET':
        data = Conical.objects.all().order_by('id').values()
        Product_name = [item['product'] for item in data if item['product']]
        print(Product_name)
        return JsonResponse({'Product_name': Product_name})