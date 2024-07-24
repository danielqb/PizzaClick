from django.shortcuts import render, redirect
from .forms import PizzaOrderForm
from .models import PizzaOrder

def order_pizza(request):
    if request.method == 'POST':
        form = PizzaOrderForm(request.POST)
        if form.is_valid():
            pizza_order = PizzaOrder(
                pizza_type=form.cleaned_data['pizza_type'],
                comments=form.cleaned_data['comments']
            )
            pizza_order.save()
            return redirect('order_success')
    else:
        form = PizzaOrderForm()
    return render(request, 'order_pizza.html', {'form': form})

def order_success(request):
    return render(request, 'order_success.html')

def order_list(request):
    orders = PizzaOrder.objects.all()
    return render(request, 'orders.html', {'orders': orders})