from application.app import app
from flask import redirect, render_template, request, url_for
from libs.token import check_admin_auth
from products.ProductRepository import ProductRepository
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'application/static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'jfif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/admin/addproducts", methods=['GET', 'POST'])
@check_admin_auth
def all_products(user):
    template = "admin_product_list.html"
    prod_repo = ProductRepository()
    all_prods = prod_repo.get_all()
    products_category = prod_repo.get_product_category()
    if request.method == "POST":
        if "delete_product" in request.form:
            data_deleted = prod_repo.delete(request.form['delete_product'])
            if data_deleted:
                return redirect(request.url)
        if "add_new_prod_category" in request.form:
            data_inserted = prod_repo.add_new_category(
                request.form.get("prod_category_value"))
            if data_inserted:
                return redirect(request.url)
        if "update_prod" in request.form:
            new_product_name = request.form['new_prod_name']
            new_product_category = request.form['new_prod_cate']
            new_product_price = request.form['new_prod_price']
            new_product_guaranty = " ".join(
                request.form['new_prod_gua'].split("T"))
            new_product_details = request.form['new_prod_details']
            product_id = request.form['update_prod']
            if request.files.get("new_prod_img").filename == "":
                # update without img
                updated_data = prod_repo.update(
                    new_product_name, new_product_category, new_product_price, new_product_guaranty, new_product_details, product_id)
                if updated_data:
                    return redirect(request.url)
            else:
                # update with img
                file = request.files['new_prod_img']

                if file.filename == '':
                    return redirect(request.url)
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(UPLOAD_FOLDER, filename))
                if not allowed_file(file.filename):
                    return redirect(request.url)
                file_db = "/static/"+file.filename
                updated_data = prod_repo.update(new_product_name, new_product_category, new_product_price,
                                                new_product_guaranty, new_product_details, product_id, file_db)
                if updated_data:
                    return redirect(request.url)
        if "add_new_product" in request.form:
            new_product_name = request.form['new_prod_name']
            new_product_category = request.form['new_prod_cate']
            new_product_price = request.form['new_prod_price']
            new_product_guaranty = " ".join(
                request.form['new_prod_gua'].split("T"))
            new_product_details = request.form['new_prod_details']
            product_id = request.form['add_new_product']
            # update with img
            file = request.files['new_prod_img']

            if file.filename == '':
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
            file_db = "/static/"+file.filename
            if not allowed_file(file.filename):
                return redirect(request.url)
            inserted_data = prod_repo.add(new_product_name, new_product_category,
                                          new_product_price, new_product_guaranty, new_product_details, file_db)
            if inserted_data:
                return redirect(request.url)

    return render_template(template, user=user, all_prods=all_prods, prod_category=products_category)
