from django.shortcuts import render
from .models import seat, Order
from django.http import HttpResponse
from .forms import SeatBookingForm

# Create your views here.
def seatview(request, *args, **kwargs):
    seat_ = seat.objects.all()
    context = {}
    context['seats'] = seat_
    form = SeatBookingForm()
    context['form'] = form
    Order_ = Order.objects.filter(user = request.user)
    my_seat = seat.objects.filter(order__in = Order_)
    print(my_seat)
    context['my_seats'] = my_seat
    if request.method=='POST':
        form = SeatBookingForm(data=request.POST)
        if form.is_valid():
        # getting the list of ngos
            _data__ = form.cleaned_data['seats']
            print(_data__)
            for i in _data__:
                selected_seat = seat.objects.get(id=int(i))
                print(selected_seat)
                order = Order.objects.get(user = request.user)
                print(order)
                selected_seat.order = order
                selected_seat.save()
            print("Booking saved")
    else:
        print(form.errors)
    return render(request, template_name='main.html', context=context)
