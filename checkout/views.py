from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
    publish_key = settings.STRIPE_PUBLISHABLE_KEY
    customer_id = request.user.userstripe.stripe_id
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            customer = stripe.Customer.retrieve(customer_id)
            print customer
            customer.sources.create(card=token)
            stripe.Charge.create(
                amount=1000,  # amount in cents, again
                currency="usd",
                customer=customer,
                description="payinguser@example.com"
            )
        except stripe.CardError, e:
            pass
    context = {'publish_key': publish_key}
    template = 'checkout.html'
    return render(request, template, context)