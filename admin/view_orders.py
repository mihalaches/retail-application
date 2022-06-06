from application.app import app
from flask import render_template, request
from orders.OrdersRepository import OrdersRepository


@app.route("/admin/orders",methods=['GET','POST'])
def view_orders():
    order_repo = OrdersRepository()
    all_orders = order_repo.get_all()
    all_orders.sort(key = lambda x : x.order_id)
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
    return render_template("admin_orders.html",orders = all_orders, pages = (orders_lengts // 7)+1)