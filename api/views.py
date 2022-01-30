import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render

from .models import Customer
from .models import SaleOrder
from .models import SaleOrderLine

from .froms import FormSaleOrder


# Create your views here.
class CustomerView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            customers = list(Customer.objects.filter(id=id).values())
            if len(customers) > 0:
                customers = customers[0]
                datos = {"message":"Success", 'customers':customers}
            else:
                datos = {"message":"customers not found..."}
            return JsonResponse(datos)
        else:
            customers = list(Customer.objects.values())
            if len(customers)>0:
                datos = {"message":"Success", 'customers':customers}
            else:
                datos = {"message":"customers not found..."}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Customer.objects.create(name=jd['name'], comment=jd['comment'])
        datos = {"message":"Success"}

        return JsonResponse(datos)

    def put(self, request, id):

        jd = json.loads(request.body)
        customers = list(Customer.objects.filter(id=id).values())

        if len(customers)>0:
            customers = Customer.objects.get(id=id)
            customers.name = jd ['name']
            customers.comment = jd ['comment']
            customers.save()   
            datos = {"message":"Success"}
        else:
            datos = {"message":"Customer not found..."}
        return JsonResponse(datos)


    def delete(self, request, id):

        customers = list(Customer.objects.filter(id=id).values())
        
        if len(customers)>0:
            Customer.objects.filter(id=id).delete()
            datos = {"message":"Success"}
        else:
            datos = {"message":"Customer not found..."}
        return JsonResponse(datos)


class SaleOrderView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            saleorders = list(SaleOrder.objects.filter(id=id).values())
            if len(saleorders) > 0:
                saleorders = saleorders[0]
                datos = {"message":"Success", 'saleorders':saleorders}
            else:
                datos = {"message":"saleorders not found..."}
            return JsonResponse(datos)
        else:
            saleorders = list(SaleOrder.objects.values())
            if len(saleorders)>0:
                datos = {"message":"Success", 'saleorders':saleorders}
            else:
                datos = {"message":"saleorders not found..."}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        SaleOrder.objects.create(customer_id=jd['customer_id'],
        comment=jd['comment'], date=jd['date'], total=jd['total'])
        
        datos = {"message":"Success"}

        return JsonResponse(datos)

    def put(self, request, id):

        jd = json.loads(request.body)
        saleorders = list(SaleOrder.objects.filter(id=id).values())

        if len(saleorders)>0:
            saleorders = SaleOrder.objects.get(id=id)
            saleorders.customer_id = jd ['customer_id']
            saleorders.comment = jd ['comment']
            saleorders.date = jd ['date']
            saleorders.total = jd ['total']
            saleorders.save()   
            datos = {"message":"Success"}
        else:
            datos = {"message":"SaleOrder not found..."}
        return JsonResponse(datos)


    def delete(self, request, id):

        saleorders = list(SaleOrder.objects.filter(id=id).values())
        
        if len(saleorders)>0:
            SaleOrder.objects.filter(id=id).delete()
            datos = {"message":"Success"}
        else:
            datos = {"message":"saleorders not found..."}
        return JsonResponse(datos)



class SaleOrderLineView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            saleordersline = list(SaleOrderLine.objects.filter(id=id).values())
            if len(saleordersline) > 0:
                saleordersline = saleordersline[0]
                datos = {"message":"Success", 'saleordersline':saleordersline}
            else:
                datos = {"message":" saleordersline not found..."}
            return JsonResponse(datos)
        else:
            saleordersline = list(SaleOrderLine.objects.values())
            if len(saleordersline)>0:
                datos = {"message":"Success", 'saleordersline':saleordersline}
            else:
                datos = {"message":"saleordersline not found..."}
            return JsonResponse(datos)

    def price_total(quantity, price):
        price_total = (quantity * price)
        print (price_total)
        return price_total
  
   


    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        SaleOrderLine.objects.create(sale_order_id = jd['sale_order_id'], product_id = jd['product_id'],
        quantity = jd['quantity'], price = jd ['price'],)
        
        datos = {"message":"Success"}

        return JsonResponse(datos)

    def put(self, request, id):

        jd = json.loads(request.body)
        saleordersline = list(SaleOrderLine.objects.filter(id=id).values())

        if len(saleordersline)>0:
            saleordersline = SaleOrderLine.objects.get(id=id)
            saleordersline.sale_order_id = jd ['sale_order_id']
            saleordersline.product_id = jd ['product_id']
            saleordersline.quantity = jd ['quantity']
            saleordersline.price = jd ['price']
            saleordersline.price_total = jd ['price_total']
            saleordersline.save()   
            datos = {"message":"Success"}
        else:
            datos = {"message":"saleordersline not found..."}
        return JsonResponse(datos)


    def delete(self, request, id):

        saleordersline = list(SaleOrder.objects.filter(id=id).values())
        
        if len(saleordersline)>0:
            SaleOrderLine.objects.filter(id=id).delete()
            datos = {"message":"Success"}
        else:
            datos = {"message":"saleordersline not found..."}
        return JsonResponse(datos)


def create(request):
    form = FormSaleOrder

    return render(request, 'froms.html', {'form' : form})