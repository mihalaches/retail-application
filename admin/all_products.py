from application.app import app
from flask import redirect, render_template, request
from libs.token import check_admin_auth
from products.ProductRepository import ProductRepository

@app.route("/admin/addproducts",methods=['GET','POST'])
@check_admin_auth
def all_products(user):
    template = "admin_product_list.html"
    prod_repo = ProductRepository()
    all_prods = prod_repo.get_all()
    products_category = prod_repo.get_product_category()
    if request.method == "POST":
        print(request.form)
        if "delete_product" in request.form:
            data_deleted = prod_repo.delete(request.form['delete_product'])
            if data_deleted:
                return redirect(request.url)
        if "add_new_prod_category" in request.form:
            data_inserted = prod_repo.add_new_category(request.form.get("prod_category_value"))
            if data_inserted:
                return redirect(request.url)
        if not request.form.get("new_prod_img"):
            print("sadsa")
        
    return render_template(template, user=user, all_prods = all_prods, prod_category = products_category)