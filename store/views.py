from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Product
from django.contrib import messages

def product_list(request):
    products = Product.objects.all()
    return render(request, "store/product_list.html", {"products": products})

def cart_view(request):
    cart = request.session.get("cart", {})
    items = []
    total = 0
    if cart:
        product_ids = cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        product_map = {str(p.id): p for p in products}
        for pid, qty in cart.items():
            prod = product_map.get(pid)
            if not prod:
                continue
            subtotal = prod.price * qty
            items.append({"product": prod, "qty": qty, "subtotal": subtotal})
            total += subtotal
    return render(request, "store/cart.html", {"items": items, "total": total})

@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get("cart", {})
    pid = str(product_id)
    cart[pid] = cart.get(pid, 0) + 1
    request.session["cart"] = cart
    messages.success(request, f"Added {product.name} to cart.")
    # stay on product list (redirect back)
    return redirect(request.META.get("HTTP_REFERER", "/"))