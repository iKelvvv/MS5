from django.shortcuts import render, redirect, reverse, HttpResponse


# Create your views here.
def view_bag(request):
    """A view that renders the bag contents page"""
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    weight = None
    if 'product_weight' in request.POST:
        weight = request.POST['product_weight']
    bag = request.session.get('bag', {})

    if weight:
        if item_id in list(bag.keys()):
            if weight in bag[item_id]['items_by_weight'].keys():
                bag[item_id]['items_by_weight'][weight] += quantity
            else:
                bag[item_id]['items_by_weight'][weight] = quantity
        else:
            bag[item_id] = {'items_by_weight': {weight: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust quantity of items from the shopping bag"""
    
    quantity = int(request.POST.get('quantity'))
    weight = None
    if 'product_weight' in request.POST:
        weight = request.POST['product_weight']
    bag = request.session.get('bag', {})

    if weight:
        if quantity > 0:
            bag[item_id]['items_by_weight'][weight] = quantity
        else:
            del bag[item_id]['items_by_weight'][weight]
            if not bag[item_id]['items_by_weight']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove items from the shopping bag"""
    
    try:
        weight = None
        if 'product_weight' in request.POST:
            weight = request.POST['product_weight']
        bag = request.session.get('bag', {})

        if weight:
            del bag[item_id]['items_by_weight'][weight]
            if not bag[item_id]['items_by_weight']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
