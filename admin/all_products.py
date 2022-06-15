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
    if request.method == "POST":
        print(request.form)
        if "delete_product" in request.form:
            data_deleted = prod_repo.delete(request.form['delete_product'])
            if data_deleted:
                return redirect(request.url)
        if not request.form['new_prod_img']:
            print("sadsa")
        
    return render_template(template, user=user, all_prods = all_prods)