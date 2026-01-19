from django.shortcuts import render, get_object_or_404
from .models import Pago
from django.contrib.auth.decorators import login_required

@login_required
def pago_ticket(request, pago_id):
    pago = get_object_or_404(Pago, id=pago_id)
    return render(request, 'ticket/pago_ticket.html', {'pago': pago})