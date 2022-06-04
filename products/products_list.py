from math import prod
from application.app import app 
from libs.token import check_auth
from flask import redirect, render_template, request
from products.ProductRepository import ProductRepository

@app.route("/products", methods = ["GET","POST"])
@check_auth
def products_list(user):
    product_repo = ProductRepository()
    if request.method == "POST":
        print(request.form)
        for _ in range(int(request.form['quantity'])):
            product_repo.add_to_cart(int(request.form['product_id']),user.cid)
        return redirect(request.url)
    products = product_repo.get_all()
    by_category = request.args.get("category")
    products_by_cat = product_repo.sort_by_category(by_category)
    if products_by_cat:
        return render_template("products_list.html",user = user.serialize(), products = products_by_cat)
    else:
        return render_template("products_list.html",user = user.serialize(), products = products)