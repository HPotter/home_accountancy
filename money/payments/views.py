from datetime import datetime, timedelta

from annoying.decorators import render_to
from django.contrib.auth.models import User

from models.payments import Payment
from payments.models.stores import StoreType, Store


@render_to('payments.html')
def payments(request):
    from_date = datetime.now() - timedelta(days=30)

    return {
        'from_date': from_date,
        'payments': Payment.objects
            .filter(date__gte=from_date)
            .order_by('-date')
    }

@render_to('my_payments.html')
def my_payments(request):
    if request.method == "POST":
        store_type, created = StoreType.objects.get_or_create(name=request.POST.get('store_type'))

        store, created = Store.objects.get_or_create(name=request.POST.get('store_name'), type=store_type)

        amount = float(
            request.POST.get('amount', '0')
            .replace(',', '.')
            .replace(' ', '')
        )

        date = datetime.now()

        contents = request.POST.getlist('contents')

        payment = Payment(user=request.user, amount=amount, date=date, place=store)
        payment.save()
        payment.contents.add(*contents)

    from_date = datetime.now() - timedelta(days=30)

    return {
        'names_suggestlist': set(Store.objects.values_list('name', flat=True)),
        'store_types': StoreType.objects.all(),
        'from_date': from_date,
        'payments': Payment.objects
            .filter(date__gte=from_date, user=request.user)
            .order_by('-date')
    }

@render_to('deal_payment.html')
def deal_payment(request, payment_id):
    return {
        'payment': Payment.objects.get(id=payment_id),
        'users': User.objects.all()
    }