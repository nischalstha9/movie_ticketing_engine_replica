from Engine.models import seat, Order

def action():
    list = [1,2]
    for i in list:
        order = Order.objects.get(id=1)
        seat_ = seat.objects.get(id=i)
        seat_.order = order
        seat_.save()

action()