from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to

from models.payments import Payment

@login_required
@render_to('list_payments.html')
def list_payments(request):
    return {
        'payments': Payment.objects.all()
    }