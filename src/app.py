import string, random

from flask import Flask, redirect, render_template, request, make_response, url_for

app = Flask(__name__)


ITEMS = [
    {
        'id': 1,
        'title': 'Orange Power',
        'description': 'If you want other flavours than plain coffee this coffee mix with orange peel will be perfect for you.',
        'image': 'static/img/coffee_p1.jpg',
        'price': '30',
    }, 

    {
        'id': 2,
        'title': 'Double Hit',
        'description': 'A cup of coffee can not get you out of bed? Try this new coffee with doubled dose of coffeine.',
        'image': 'static/img/coffee_p2.jpg',
        'price': '45',
    }, 

    {
        'id': 3,
        'title': 'Three Musketeers',
        'description': 'Normal coffee? Maybe, but you will always get three packages no matter the price.',
        'image': 'static/img/coffee_p3.jpg',
        'price': '35',
    }, 

    {
        'id': 4,
        'title': 'Big Boys',
        'description': 'More coffee. More coffeine. More energy in the morning. Just more.',
        'image': 'static/img/coffee_p4.jpg',
        'price': '60',
    }
    
]

VALID_COUPONS = []

def coupon_generator(size=10, chars=string.ascii_uppercase + string.digits):
    global VALID_COUPONS

    new_coupon = ''.join(random.choice(chars) for _ in range(size))
    VALID_COUPONS.append(new_coupon)
    return new_coupon


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/error")
def error():
    return render_template("error.html")


@app.route("/shop", methods=["GET"])
def shop():
    return render_template("shop.html", items=ITEMS)


@app.route('/transaction/<id>', methods=["GET","POST"])
def transaction(id):
    # get discount from request json
    # set cookie by getting discount value from json
    print(request.json)
    VALID_COUPONS.pop(VALID_COUPONS.index(discount))
    return make_response("OK")

@app.route('/thank_you', methods=["GET"])
def thank_you():
    # get discount from somewhere
    discount = request.cookies.get('discount')
    return render_template("thank_you.html", discount=discount)

@app.route('/buy/<id>', methods=["GET","POST"])
def buy(id):
    discount = request.cookies.get('discount_coupon')
    
    if not discount:
        return redirect("/error")
        
    if discount in VALID_COUPONS:
        discount = 15
        return render_template("transaction.html", discount=discount, id=id)
    else:
        return redirect("/error")


# OK
@app.route("/contact", methods=["GET","POST"])
def discount():
    if request.method == "POST":
        discount_code = "Congratulations! Your 15% discount have been assigned to you!"
        res = make_response(render_template("contact.html", discount_code=discount_code))
        res.set_cookie("discount_coupon", coupon_generator())
        return res
    else:
        return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)