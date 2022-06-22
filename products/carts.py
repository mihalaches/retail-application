from application.app import app
from libs.token import check_auth
from flask import flash, redirect, render_template, request
from products.ProductRepository import ProductRepository
from users.UserRepository import UserRepository
from libs.messages import Messages


@app.route("/cart", methods=['GET', 'POST'])
@check_auth
def cart(user):
    product_repo = ProductRepository()
    user_repository = UserRepository()
    total_price = 0
    address = user_repository.check_customer_address(user.cid)
    for element in user.cart:
        total_price += element.product_price
    if request.method == "POST":
        if "delete_address" in request.form:
            print(request.form['delete_address'])
            address_deleted = user_repository.delete_address(request.form['delete_address'])
            if address_deleted:
                return redirect(request.url)
        if not address:
            country = request.form['address_country']
            city = request.form['address_city']
            phone_number = request.form['address_phone_number']
            full_address = request.form['full_address']
            if "add_address" in request.form:
                user_repository.add_address(user.cid,country,city,phone_number,full_address)
                return redirect(request.url)
        if 'remove' in request.form:
            cart_p_id = int(request.form['remove'])
            product_repo.delete_from_cart(cart_p_id)
            return redirect(request.url)
        if 'empty_cart' in request.form:
            product_repo.delete_cart_products_by_cid(user.cid)
            flash(Messages.EMPTY_CART)
            return redirect(request.url)
        if 'send_order' in request.form:
            if total_price > user.deposit:
                flash(Messages.NO_MONEY_ACCOUNT)
            else:
                new_amount = user.deposit - total_price
                update_amount = user_repository.update_deposit(
                    user.cid, new_amount)
                if update_amount:
                    flash(Messages.SUCCESS_ORDER.format(
                        new_deposit_amount=new_amount))
                    product_repo.delete_cart_products_by_cid(
                        user.cid, ordered=True)
                    return redirect(request.url)
    return render_template("cart.html", user=user.serialize(), total_price=total_price,address = address)
