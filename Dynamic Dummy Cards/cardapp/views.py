from django.shortcuts import render
from django.http import HttpResponse
from cardapp.models import Dummycards


def index(request):

    obj1 = Dummycards('Quantum Entanglement','1.jpg')
    obj2 = Dummycards('Astro Physics','2.jpg')
    obj3 = Dummycards('Horse Shoe Nebula','3.jpg')
    obj4 = Dummycards('Europa Supercluster','4.jpg')
    obj5 = Dummycards('Diffussion Layer','5.jpg')
    obj6 = Dummycards('Intent Classification','6.jpg')
    obj7 = Dummycards('Ad Astra','7.jpg')
    obj8 = Dummycards('Neuro Plasticity','8.jpg')
    obj9 = Dummycards('Entity Identification','9.jpg')
    obj10 = Dummycards('Event Horizon','10.jpg')
    obj11 = Dummycards('Cosmic Pulsar','11.jpg')
    obj12 = Dummycards('Neutron Star','12.jpg')
        
    obj = [obj1,obj2,obj3,obj4,obj5,obj6,obj7,obj8,obj9,obj10,obj11,obj12]

    return render(request, "index.html", {'obj':obj})