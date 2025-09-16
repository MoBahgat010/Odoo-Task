# Odoo 18 Enterprise Custom Module for Sales Order Enhancements

This repository contains the setup and customizations for an Odoo 18 Enterprise environment, focusing on the Sales Order module with specific enhancements to mirror top-section fields (like customer and payment terms) into the order lines for real-time synchronization. The project builds on a previous Odoo Community database, upgraded for Enterprise features, and includes configurations for addons like `account_3way_match`.

## Project Overview

The goal of this project is to set up an Odoo 18 Enterprise environment and implement a custom module (`sales_order_enhancement`) that modifies the Sales Order page. The customizations ensure that key fields from the top section of the Sales Order (e.g., customer and payment terms) are mirrored into the order lines and updated in real-time. This repository also includes configurations for integrating Enterprise addons and troubleshooting steps for common issues like field visibility and syncing problems.

## Features

- **Odoo 18 Enterprise Setup**: Configured environment with Enterprise addons like `account_3way_match`.
- **Custom Module**: A module named `sales_order_enhancement` that extends the Sales Order functionality.
- **Field Mirroring**: Mirrors fields such as customer and payment terms from the Sales Order header to order lines.
- **Real-Time Sync**: Ensures updates to header fields reflect in order lines dynamically.
- **Developer Mode**: Instructions for enabling Developer Mode to access advanced customization options.
- **Troubleshooting**: Steps to resolve issues like missing fields, 404 errors, and syncing problems.

## Prerequisites

- **Odoo 18 Enterprise**: Ensure you have a valid Enterprise subscription and license.
- **PostgreSQL**: A running PostgreSQL database (version compatible with Odoo 18, typically 12 or higher).
- **Python**: Version 3.10 or higher.
- **Operating System**: Linux (Ubuntu recommended) or Windows.
- **Git**: For cloning the repository and managing version control.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Set Up Odoo 18 Enterprise**:
   - Clone the Odoo 18 Enterprise repository or use the packaged installer.
   - Example for source installation on Ubuntu:
     ```bash
     git clone https://github.com/odoo/enterprise.git ~/odoo-enterprise
     ```
   - Install dependencies:
     ```bash
     pip install -r ~/odoo-enterprise/requirements.txt
     ```

3. **Configure PostgreSQL**:
   - Reuse an existing Odoo Community database or create a new one:
     ```bash
     createdb odoo18_enterprise
     ```
   - Backup your existing database before upgrading:
     ```bash
     pg_dump odoo_community_db > backup.sql
     ```

4. **Update Odoo Configuration**:
   - Modify `odoo.conf` to include the Enterprise addons path and your custom module:
     ```ini
     [options]
     addons_path = ~/odoo-enterprise/addons,~/odoo-enterprise/enterprise,~/your-repo-name/custom_addons
     db_name = odoo18_enterprise
     admin_passwd = your_secure_password
     ```

5. **Run Odoo**:
   - Start Odoo with the configuration file:
     ```bash
     ~/odoo-enterprise/odoo-bin -c ~/your-repo-name/odoo.conf
     ```

6. **Install the Custom Module**:
   - Access the Odoo interface (default: `http://localhost:8069`).
   - Enable Developer Mode (via User Menu > About > Activate Developer Mode).
   - Go to Apps, search for `sales_order_enhancement`, and install it.

## Directory Structure

```
your-repo-name/
├── custom_addons/
│   └── sales_order_enhancement/
│       ├── __init__.py
│       ├── __manifest__.py
│       ├── models/
│       │   └── sale_order.py
│       ├── views/
│       │   └── sale_order_view.xml
│       └── data/
│           └── sale_order_data.xml
├── odoo.conf
└── README.md
```

## Custom Module Details

### `__manifest__.py`
- Defines the module metadata and dependencies.
- Ensures the module appears in the Apps menu.
- Depends on the `sale` module for Sales Order functionality.

### `models/sale_order.py`
- Extends the `sale.order` and `sale.order.line` models.
- Adds fields like `customer_name` and `payment_term_id` to order lines.
- Implements logic for real-time synchronization of header fields to order lines.

### `views/sale_order_view.xml`
- Defines custom views for the Sales Order page.
- Adds mirrored fields to the order lines table.
- Inherits and extends the default Sales Order form view.

### `data/sale_order_data.xml`
- Optional sample data for testing the module.

## Usage

1. **Access the Sales Order Page**:
   - Navigate to the Sales module in Odoo.
   - Create or edit a Sales Order to see the header (customer, payment terms) and order lines (product, quantity, price).

2. **Verify Field Mirroring**:
   - Update the customer or payment terms in the header.
   - Check that the order lines reflect these changes in real-time.

3. **Troubleshooting**:
   - If fields are not visible, ensure the module is installed and views are correctly defined.
   - Check Odoo logs (`odoo.log`) for errors related to XML or Python code.
   - Verify the `addons_path` in `odoo.conf` includes your custom module.

4. **Enable Developer Mode**:
   - Go to User Menu > About > Activate Developer Mode (requires admin rights).
   - Use Developer Mode to inspect view definitions and debug issues.

## Troubleshooting Common Issues

- **Fields Not Syncing**:
  - Verify the `onchange` methods in `sale_order.py`.
  - Ensure the XML view inherits the correct form view ID.

- **404 Errors on API or Module**:
  - Check the `addons_path` in `odoo.conf`.
  - Restart Odoo and update the module list (`-u base`).

- **Enterprise Features Not Visible**:
  - Confirm the Enterprise addons path is included in `odoo.conf`.
  - Verify your subscription license is active.

- **Database Issues**:
  - Ensure PostgreSQL is running and the database name matches `odoo.conf`.
  - Reset the master password in `odoo.conf` if admin access is lost.

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes. Ensure that your code follows Odoo’s coding guidelines and includes appropriate tests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Resources

- [Odoo 18 Documentation](https://www.odoo.com/documentation/18.0/)
- [Odoo Community Forums](https://www.odoo.com/forum)
- [Odoo Enterprise Support](https://www.odoo.com/help)