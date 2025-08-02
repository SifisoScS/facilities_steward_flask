# DERIVCO DURBAN FACILITIES - Flask Application

A comprehensive facilities management system redesigned using Python Flask framework, specifically tailored for Sifiso Shezi's facilities stewardship role at Derivco Durban.

## Overview

This application provides a complete facilities management solution aligned with ISO 41001 standards, featuring:

- **Inventory Management**: Track tools, equipment, and consumables
- **Asset Management**: Register and monitor furniture and fixed assets
- **Usage Logging**: Borrow/return tracking with accountability
- **Work Order Management**: Create and track maintenance tasks
- **ISO 41001 Compliance**: Built-in compliance features and reporting

## Features

### 🎯 Dashboard

- Personalized welcome for Sifiso Shezi (Facilities Steward | Systems Architect)
- Real-time metrics and KPIs
- ISO 41001:2018 certification badge
- Quick action buttons for common tasks
- Professional corporate design with Derivco branding

### 📦 Inventory Management

- Add, edit, and track inventory items
- Location-based organization
- Condition monitoring (Good, Repair Needed, Obsolete)
- Low stock alerts and reorder management
- Minimum stock level configuration

### 🪑 Asset Management

- Register furniture and equipment by room/location
- Photo documentation support
- Purchase date tracking
- Condition assessment and monitoring
- Room-based asset organization

### 📋 Usage Logs

- Borrow/return tracking system
- Staff accountability with timestamps
- Purpose and job ID linking
- Real-time status monitoring
- Return notifications

### 🔧 Work Order Management

- Create and track maintenance tasks
- Location and department assignment
- Duration estimation and tracking
- Requestor and supervisor signatures
- Status management (Pending/Done)

## Technical Stack

- **Backend**: Python Flask 2.3.3
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Forms**: Flask-WTF with WTForms validation
- **Security**: CSRF protection, CORS enabled
- **Icons**: Font Awesome 6

## Installation

1. **Clone or extract the project**:

   ```bash
   cd facilities_steward_flask
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:

   ```bash
   python app.py
   ```

4. **Access the application**:
   Open your browser and navigate to `http://localhost:5000`

## Project Structure

cd facilities_steward_flask
pip install -r requirements.txt
python app.py

facilities_steward_flask/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models
│   ├── routes.py            # Application routes
│   ├── forms.py             # WTForms definitions
│   └── templates/           # Jinja2 templates
│       ├── base.html        # Base template
│       ├── index.html       # Dashboard
│       ├── inventory.html   # Inventory listing
│       ├── add_inventory.html
│       ├── assets.html      # Asset listing
│       ├── add_asset.html
│       ├── usage_logs.html  # Borrow/return logs
│       ├── borrow_item.html
│       ├── work_orders.html # Work order listing
│       └── add_work_order.html
├── app.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md               # This file

## Database Models

### InventoryItem

- Item name, quantity, location
- Condition and minimum stock level
- Last reorder date tracking

### Asset

- Asset type, room number, location description
- Quantity, purchase date, condition
- Photo path for documentation

### UsageLog

- Staff name, borrow/return timestamps
- Purpose and job ID linking
- Foreign keys to inventory items and assets

### WorkOrder

- Work order details and descriptions
- Location, duration, task type
- Requestor and supervisor information
- Status tracking

### User

- Staff information and access levels
- Role-based permissions

## Design Features

### Color Palette

- **Navy Blue (#003366)**: Authority and reliability
- **Slate Grey (#708090)**: Stability and neutrality
- **Teal (#008080)**: Innovation and clarity
- **Lime Green (#A6CE39)**: Freshness and growth
- **White (#FFFFFF)**: Clean, ISO-compliant design

### UI/UX Elements

- Gradient backgrounds and hover effects
- Card-based layout with shadows
- Responsive design for all devices
- Professional typography (Segoe UI)
- Smooth transitions and micro-interactions

## ISO 41001 Compliance

The application is designed to support ISO 41001:2018 Facilities Management standards:

- **Transparency**: Complete audit trails for all transactions
- **Planning**: Data-driven decision support and reporting
- **Security**: Controlled access and accountability measures
- **Preparedness**: Real-time status monitoring and alerts

## Usage Instructions

### Adding Inventory Items

1. Navigate to Inventory → Add New Item
2. Fill in item details (name, quantity, location, condition)
3. Set minimum stock level for alerts
4. Submit to add to inventory

### Registering Assets

1. Go to Assets → Add New Asset
2. Enter asset type, room number, and location
3. Set quantity and condition
4. Add purchase date if available
5. Submit to register asset

### Borrowing Items

1. Visit Usage Logs → Borrow Item
2. Select item type (Inventory or Asset)
3. Choose specific item from dropdown
4. Enter staff name and purpose
5. Submit to create borrow record

### Creating Work Orders

1. Navigate to Work Orders → Create Work Order
2. Fill in work order details
3. Set location, duration, and task type
4. Add detailed description
5. Submit to create work order

## Development Notes

- The application uses Flask's application factory pattern
- Database is automatically created on first run
- CSRF protection is enabled for all forms
- CORS is configured for API access
- Debug mode is enabled for development

## Future Enhancements

- User authentication and role-based access
- Photo upload for assets and inventory
- Advanced reporting and analytics
- Email notifications for low stock
- Barcode/QR code integration
- Mobile app companion

## Support

For technical support or feature requests, contact the development team or refer to the project documentation.

---

**© Derivco Facilities Intelligence | Sifiso Shezi Methodology**  
*Empowering Excellence in Facilities Management – Aligned to ISO 41001*
