from application.app import app
from libs.token import check_auth
from flask import flash, redirect, render_template, request
from products.ProductRepository import ProductRepository

@app.route("/cart",methods=['GET','POST'])
@check_auth
def cart(user):
    product_repo = ProductRepository()
    total_price = 0
    for element in user.cart:
        total_price += element.product_price
    if request.method == "POST":
        if 'remove' in request.form:
            cart_p_id = int(request.form['remove'])
            product_repo.delete_from_cart(cart_p_id)
            return redirect(request.url)
        if 'send_order' in request.form:
            if total_price > user.deposit:
                flash("No money in account!") 
    return render_template("cart.html",user = user.serialize(), total_price = total_price)