# Django REST API Vendor Management System

This project is a Django-based RESTful API that provides endpoints for managing data related to vendor management system

## Setup

1. **Clone the repository:**
    ```bash
    git clone git@github.com:kartik9928/vendor-management-system-API.git
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

5. **Access the API:**
    1. To create vendor - POST
        http://127.0.0.1:8000/vendor/api/create/
        {
            "name": "name",
            "contact_details": "contact_details",
            "address": "address"
        }

        response
        {
            token: token_key
        }

    2. To retrieve all vendor - GET
        http://127.0.0.1:8000/vendor/api/retrieve/

        response :- list of vendor with all details

    3. To retrieve specific vendor - GET
        http://127.0.0.1:8000/vendor/api/retrieve/<vendor_code>/

        response :- specific vendor with all details

    4. To update specific vendor - PUT
        http://127.0.0.1:8000/vendor/api/update/<vendor_code>/
        {
            "vendor_code": "vendor_code",
            "name": "name",
            "contact_details": "contact_details",
            "address": "address"
        }

        response :- updated vendor

    5. To delete specific vendor - DELETE
        http://127.0.0.1:8000/vendor/api/update/<vendor_code>/

        response :- vendor got deleted

    6. To retrieve vendor historical performance - GET
        http://127.0.0.1:8000/vendor/api/performance/<vendor_code>/

        response :- all historical performance of the specifi vendor with vendor, date, on_time_delivery_rate, quality_rating_avg, average_response_time, fulfillment_rate

    7. To create purchase - POST
        http://127.0.0.1:8000/purchase/api/create/
        {
            'po_number': 'po_number',
            'vendor': 'vendor',
            'order_date': 'order_date',
            'delivery_date': 'delivery_date',
            'items': 'items',
            'quantity': 'quantity',
            'status': 'status',
            'quality_rating': 'quality_rating',
            'issue_date': 'issue_date'
        }

        response :- purchase created

    8. To get all purchase - GET
        http://127.0.0.1:8000/purchase/api/display/

        response :- display all the purchases

    9. to get purchase from specific vendor - GET
        http://127.0.0.1:8000/purchase/api/display/<vendor_code>/

        response :- display all the purchase from that vendor only

    10. To get specific purchase - GET
        http://127.0.0.1:8000/purchase/api/order/<po_number>/

        response :- get specific purchase

    11. To update specific purchase - PUT
        http://127.0.0.1:8000/purchase/api/update/<po_number>/
        {
            'po_number': 'po_number',
            'vendor': 'vendor',
            'order_date': 'order_date',
            'delivery_date': 'delivery_date',
            'items': 'items',
            'quantity': 'quantity',
            'status': 'status',
            'quality_rating': 'quality_rating',
            'issue_date': 'issue_date'
        }

        response :- updated purchase

    12. To delete specific purchase - DELETE
        http://127.0.0.1:8000/purchase/api/update/<po_number>/

        response :- purchase deleted

    13. vendor acknowledge purchase
        http://127.0.0.1:8000/purchase/api/acknowledge/<po_number>/
        headers = {
            Authorization: Token <token key>
        }

        response :- specific purshase acknowledge will be updated with that day date