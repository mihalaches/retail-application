from application.app import app
from libs.token import check_auth
from flask import redirect, render_template, request
from products.ProductRepository import ProductRepository
import random

@app.route("/products", methods=["GET", "POST"])
@check_auth
def products_list(user):
    product_repo = ProductRepository()
    if request.method == "POST":
        if request.form.get("quantity"):
            for _ in range(int(request.form['quantity'])):
                product_repo.add_to_cart(int(request.form['product_id']), user.cid)
            return redirect(request.url)
    products = product_repo.get_all()
    if request.method == "POST" and not request.args.get("category"):
        if "sort_asc" in request.form:
            products.sort(key= lambda prod:prod.product_price)
            return render_template("products_list.html", user=user.serialize(), products=products, sorty_by="ALL")
        if "sort_desc" in request.form:
            products.sort(key= lambda prod:prod.product_price, reverse=True)
            return render_template("products_list.html", user=user.serialize(), products=products, sorty_by="ALL")
    by_category = request.args.get("category")
    products_by_cat = product_repo.sort_by_category(by_category)
    if products_by_cat:
        if request.method == "POST":
            if "sort_asc" in request.form:
                products_by_cat.sort(key= lambda prod:prod.product_price)
                return render_template("products_list.html", user=user.serialize(), products=products_by_cat, sorty_by=by_category)
            if "sort_desc" in request.form:
                products_by_cat.sort(key= lambda prod:prod.product_price,reverse=True)
                return render_template("products_list.html", user=user.serialize(), products=products_by_cat, sorty_by=by_category)
        return render_template("products_list.html", user=user.serialize(), products=products_by_cat, sorty_by=by_category)
    else:
        return render_template("products_list.html", user=user.serialize(), products=products, sorty_by="ALL")
