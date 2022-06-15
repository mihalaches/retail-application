from application.app import app
from flask import render_template, request
from orders.OrdersRepository import OrdersRepository
from libs.token import check_admin_auth


@app.route("/admin/orders",methods=['GET','POST'])
@check_admin_auth
def view_orders(user):
    order_repo = OrdersRepository()
    all_orders = order_repo.get_all()
    all_orders.sort(key = lambda x : x.ordered_date, reverse=True)
    orders_lengts = len(all_orders)
    start = 0
    step = 7
    page = request.args.get("page")
    if page:
        page = int(page)
        if page <= 1:
            all_orders = all_orders[start:step]
        else:
            start = (page-1) * step
            stop = start + step
            all_orders = all_orders[start:stop]
    print(all_orders)
    return render_template("admin_orders.html",orders = all_orders, pages = (orders_lengts // 7)+1, user = user)