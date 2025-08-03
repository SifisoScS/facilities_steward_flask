from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.models import db, InventoryItem, Asset, UsageLog, WorkOrder, User
from app.forms import InventoryItemForm, AssetForm, BorrowForm, WorkOrderForm
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Get dashboard metrics
    total_assets = Asset.query.count()
    total_inventory = InventoryItem.query.count()
    active_work_orders = WorkOrder.query.filter_by(status='Pending').count()
    low_stock_items = InventoryItem.query.filter(InventoryItem.quantity <= InventoryItem.min_stock_level).count()
    
    return render_template('index.html', 
                         total_assets=total_assets,
                         total_inventory=total_inventory,
                         active_work_orders=active_work_orders,
                         low_stock_items=low_stock_items)

@main.route('/inventory')
def inventory():
    items = InventoryItem.query.all()
    low_stock_items_count = InventoryItem.query.filter(InventoryItem.quantity <= InventoryItem.min_stock_level).count()
    return render_template("inventory.html", items=items, low_stock_items_count=low_stock_items_count)

@main.route('/inventory/add', methods=['GET', 'POST'])
def add_inventory():
    form = InventoryItemForm()
    if form.validate_on_submit():
        item = InventoryItem(
            name=form.name.data,
            quantity=form.quantity.data,
            location=form.location.data,
            condition=form.condition.data,
            min_stock_level=form.min_stock_level.data or 0
        )
        db.session.add(item)
        db.session.commit()
        flash('Inventory item added successfully!', 'success')
        return redirect(url_for('main.inventory'))
    return render_template('add_inventory.html', form=form)

@main.route('/assets')
def assets():
    assets = Asset.query.all()
    return render_template('assets.html', assets=assets)

@main.route('/assets/add', methods=['GET', 'POST'])
def add_asset():
    form = AssetForm()
    if form.validate_on_submit():
        asset = Asset(
            type=form.type.data,
            room_number=form.room_number.data,
            location_description=form.location_description.data,
            quantity=form.quantity.data,
            condition=form.condition.data,
            purchase_date=form.purchase_date.data
        )
        db.session.add(asset)
        db.session.commit()
        flash('Asset added successfully!', 'success')
        return redirect(url_for('main.assets'))
    return render_template('add_asset.html', form=form)

@main.route('/usage_logs')
def usage_logs():
    logs = UsageLog.query.order_by(UsageLog.borrow_time.desc()).all()
    return render_template('usage_logs.html', logs=logs)

@main.route('/borrow', methods=['GET', 'POST'])
def borrow_item():
    form = BorrowForm()
    
    # Populate choices based on item type
    if form.item_type.data == 'inventory':
        form.item_id.choices = [(item.id, item.name) for item in InventoryItem.query.all()]
    elif form.item_type.data == 'asset':
        form.item_id.choices = [(asset.id, f"{asset.type} - {asset.room_number}") for asset in Asset.query.all()]
    else:
        form.item_id.choices = []
    
    if form.validate_on_submit():
        log = UsageLog(
            item_id=form.item_id.data if form.item_type.data == 'inventory' else None,
            asset_id=form.item_id.data if form.item_type.data == 'asset' else None,
            staff_name=form.staff_name.data,
            purpose=form.purpose.data,
            job_id=form.job_id.data
        )
        db.session.add(log)
        db.session.commit()
        flash('Item borrowed successfully!', 'success')
        return redirect(url_for('main.usage_logs'))
    
    inventory_items = InventoryItem.query.all()
    assets = Asset.query.all()
    return render_template('borrow_item.html', form=form, inventory_items=inventory_items, assets=assets)

@main.route('/return/<int:log_id>', methods=['POST'])
def return_item(log_id):
    log = UsageLog.query.get_or_404(log_id)
    log.return_time = datetime.utcnow()
    db.session.commit()
    flash('Item returned successfully!', 'success')
    return redirect(url_for('main.usage_logs'))

@main.route('/work_orders')
def work_orders():
    orders = WorkOrder.query.order_by(WorkOrder.date.desc()).all()
    return render_template('work_orders.html', orders=orders)

@main.route('/work_orders/add', methods=['GET', 'POST'])
def add_work_order():
    form = WorkOrderForm()
    if form.validate_on_submit():
        order = WorkOrder(
            name=form.name.data,
            location_department=form.location_department.data,
            duration=form.duration.data,
            task_type=form.task_type.data,
            work_description=form.work_description.data,
            requestor=form.requestor.data,
            status=form.status.data,
            supervisor_signature=form.supervisor_signature.data
        )
        db.session.add(order)
        db.session.commit()
        flash('Work order added successfully!', 'success')
        return redirect(url_for('main.work_orders'))
    return render_template('add_work_order.html', form=form)

@main.route('/api/dashboard_data')
def dashboard_data():
    """API endpoint for dashboard metrics"""
    data = {
        'total_assets': Asset.query.count(),
        'inventory_accuracy': 97.3,  # This would be calculated based on actual data
        'active_work_orders': WorkOrder.query.filter_by(status='Pending').count(),
        'low_stock_items': InventoryItem.query.filter(InventoryItem.quantity <= InventoryItem.min_stock_level).count()
    }
    return jsonify(data)