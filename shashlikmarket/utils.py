#get cart
def get_cart(request):
    cart = request.session.get('cart', {})
    return cart

#save cart in session
def save_cart(request, cart):
    request.session['cart'] = cart
    request.session.modified = True