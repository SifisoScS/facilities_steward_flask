from app import db
from datetime import datetime

class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    condition = db.Column(db.String(50), nullable=False)
    min_stock_level = db.Column(db.Integer, default=0)
    last_reorder_date = db.Column(db.DateTime)

    def __repr__(self):
        return f'<InventoryItem {self.name}>'

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    room_number = db.Column(db.String(50), nullable=False)
    location_description = db.Column(db.String(200))
    quantity = db.Column(db.Integer, nullable=False)
    purchase_date = db.Column(db.DateTime)
    condition = db.Column(db.String(50), nullable=False)
    photo_path = db.Column(db.String(200))

    def __repr__(self):
        return f'<Asset {self.type}>'

class UsageLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('inventory_item.id'))
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'))
    staff_name = db.Column(db.String(100), nullable=False)
    borrow_time = db.Column(db.DateTime, default=datetime.utcnow)
    return_time = db.Column(db.DateTime)
    purpose = db.Column(db.String(200))
    job_id = db.Column(db.String(100))

    inventory_item = db.relationship('InventoryItem', backref='usage_logs')
    asset = db.relationship('Asset', backref='usage_logs')

    def __repr__(self):
        return f'<UsageLog {self.staff_name}>'

class WorkOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    location_department = db.Column(db.String(100))
    duration = db.Column(db.String(50))
    task_type = db.Column(db.String(100))
    work_description = db.Column(db.Text)
    requestor = db.Column(db.String(100))
    status = db.Column(db.String(50), nullable=False)
    supervisor_signature = db.Column(db.String(100))

    def __repr__(self):
        return f'<WorkOrder {self.name}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    access_level = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'


