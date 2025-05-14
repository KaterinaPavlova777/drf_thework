import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):
    title = f"{instance.course}" if instance.course else instance.lesson
    stripe_product = stripe.Product.create(name=f"{title}")
    return stripe_product.id


def create_stripe_price(payment, stripe_product_id):
    price = stripe.Price.create(
        currency="rub", unit_amount=int(payment.amount * 100), product=stripe_product_id
    )
    return price.id


def create_stripe_session(price):
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price, "quantity": 1}],
        mode="payment",
    )
    return session.id, session.url
