from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired, Optional

class InventoryItemForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    condition = SelectField('Condition', choices=[
        ('good', 'Good'),
        ('repair_needed', 'Repair Needed'),
        ('obsolete', 'Obsolete')
    ], validators=[DataRequired()])
    min_stock_level = IntegerField('Minimum Stock Level', validators=[Optional()])
    submit = SubmitField('Add Item')

class AssetForm(FlaskForm):
    type = StringField('Asset Type', validators=[DataRequired()])
    room_number = StringField('Room Number', validators=[DataRequired()])
    location_description = StringField('Location Description', validators=[Optional()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    condition = SelectField('Condition', choices=[
        ('good', 'Good'),
        ('repair_needed', 'Repair Needed'),
        ('obsolete', 'Obsolete')
    ], validators=[DataRequired()])
    purchase_date = DateField('Purchase Date', validators=[Optional()])
    submit = SubmitField('Add Asset')

class BorrowForm(FlaskForm):
    item_type = SelectField('Item Type', choices=[
        ('inventory', 'Inventory Item'),
        ('asset', 'Asset')
    ], validators=[DataRequired()])
    item_id = SelectField('Item', coerce=int, validators=[Optional()])
    staff_name = StringField('Staff Name', validators=[DataRequired()])
    purpose = StringField('Purpose', validators=[Optional()])
    job_id = StringField('Job ID', validators=[Optional()])
    submit = SubmitField('Borrow Item')

class WorkOrderForm(FlaskForm):
    name = StringField('Work Order Name', validators=[DataRequired()])
    location_department = StringField('Location/Department', validators=[Optional()])
    duration = StringField('Duration', validators=[Optional()])
    task_type = StringField('Task Type', validators=[Optional()])
    work_description = TextAreaField('Work Description', validators=[Optional()])
    requestor = StringField('Requestor', validators=[Optional()])
    status = SelectField('Status', choices=[
        ('pending', 'Pending'),
        ('done', 'Done')
    ], default='pending', validators=[DataRequired()])
    supervisor_signature = StringField('Supervisor Signature', validators=[Optional()])
    submit = SubmitField('Add Work Order')

