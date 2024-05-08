# FATMUG API DOCS

Welcome to the FATMUG API documentation. This guide will help you get your local development environment set up and explain how to interact with the API.

## Installation

Follow these steps to install the required packages for the FATMUG API.

### Step 1: Clone the repository

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/fatmug-api.git
cd fatmug-api
pip install -r req.txt

```

## Step 2 : Creating and Configuring the .env File

  Create a file named .env in the root of your project.
  Open the .env file with a text editor and add the following content:
  
  # Environment variables for Django
    KEY='your_django_secret_key_here'  # Replace with your actual Django secret key
    MODE=True  # Use True for development and False for production


## Step 3 : Using the API Endpoints 
  Easiest way to test this API , install postman collections .

  # Base URL 
    http://127.0.0.1:8000/api/

  **Vendors**
  
    GET /vendors/: Retrieve a list of all vendors.
    POST /vendors/: Create a new vendor.
    
        Pass Json Data , It should be in the given format. 
        {
          "user": {
              "name": "vicky",
              "email": "vicky@demo.com",
              "password" : "pass@123"
          },
          "contact_details": "9874563210",
          "address": "Mumbai,India"
        }
          
    GET /vendors/<int:pk>: Retrieve details of a specific vendor.
    PUT /vendors/<int:pk>: Update a specific vendor.
        
        Pass Json Data  , It  should be in the given format. 
        
        {
            "user" : {
                "email" : "vp@hm.com"
            },
            "contact_details": "987456321" , // Update Details
            "address": "Mumbai,India" // Update Address
        }
    
    DELETE /vendors/<int:pk>: Delete a specific vendor.
    GET /vendors/<int:pk>/performance: Get performance data for a specific vendor.

  **Authentication**
  
    POST /login/: Authenticate a user.
    
    Pass Json Data  , It  should be in the given format. 
    
    {
      "email" : "vicky@demo.com",
      "password" : "pass@123"
    }

  **Purchase Orders**
  
  GET /purchase_orders/: Retrieve all purchase orders.
  POST /purchase_orders/: Create a new purchase order.
    
    Pass Json Data  , It  should be in the given format. 
      {
        
        "items" :
             {
            "id": 584,
            "name": "Whole Wheat Bread",
            "category": "groceries",
            "price": 56,
            "description": "Healthy whole wheat bread."
        },  
        "quantity" : 5,
        "vendor" : 1 
     }
  GET /purchase_orders/<int:pk>/: Retrieve details of a specific purchase order.
  PUT /purchase_orders/<int:pk>/: Update a specific purchase order.
     
     Pass Json Data  , It  should be in the given format. 
      
      {
        "items" :
             {
            "id": 584,
            "name": "Whole Wheat Bread",
            "category": "groceries",
            "price": 56,
            "description": "Healthy whole wheat bread."
        },  
        "quantitsy" : 2
      }
    
  DELETE /purchase_orders/<int:pk>/: Delete a specific purchase order.
  POST /purchase_orders/<int:pk>/acknowledge/: Acknowledge a specific purchase order.
    
    There are 4 Types of Acknowledgement
    In the query_params , order_type must pass 

    1. Order Approved
       Type: order_approved

    2. Order Delivered
      Type: order_delivered

    3. Order Rated
      Type: order_rate
      Additional Parameter: rating (integer, typical scale 1-5)

    4. Order Canceled
      Type: order_cancel

  **Products**
  
   GET /randomproducts/: Generate and retrieve random products.



  


