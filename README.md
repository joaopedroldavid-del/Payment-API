# Payment-API

## Overview

This repository contains the source code for a Payment API built using Python, the Flask microframework, and WebSocket protocols. This API aims to provide a real-time and efficient way to handle payment processing and notifications.

This project is part of my portfolio to demonstrate my skills in backend development, API design, and real-time communication technologies.

## Features

* **Payment Initiation:** Allows clients to initiate payment requests.
* **Real-time Status Updates:** Utilizes WebSockets to provide instant feedback on the payment processing status to connected clients.
* **Simple and RESTful Interface:** Offers a straightforward Flask-based REST API for initiating payments.

## Technologies Used

* **Python:** The primary programming language.
* **Flask:** A lightweight and flexible web framework for building the REST API.
* **Flask-Sockets:** A Flask extension to handle WebSocket connections.

## API Endpoints

### REST API (for Payment Initiation)

* **`POST /payments`**: Initiates a new payment request.
    * **Request Body (example JSON):**
        ```json
        {
            "value": 10.00
        }
        ```
    * **Response (example JSON - success):**
        ```json
        {
            "message": "The payment has been created",
            "payment": {
                "bank_payment_id": "ca2910ae-c4e8-44d3-b510-e573e9be9a58",
                "expiration_date": "Tue, 08 Apr 2025 15:45:25 GMT",
                "id": 6,
                "paid": false,
                "qr_code": "qr_code_payment_ca2910ae-c4e8-44d3-b510-e573e9be9a58",
                "value": 254.3
            }
        }
        ```
    * **Response (example JSON - error 400):**
        ```json
        {
            "message": "Invalid value"
        }
        ```
* **`POST /payments/pix/confirmation`**: Confirming payment
    * **Request Body (example JSON):**
        ```json
            {
                "bank_payment_id" : "ca2910ae-c4e8-44d3-b510-e573e9be9a58",
                "value" : 254.3
            }
        ```
    * **Response (example JSON - success):**
        ```json
            {
                "message": "The payment has been confirmed"
            }
        ```
    * **Response (example JSON - error 404):**
        ```json
        {
            "message": "Payment not found"
        }
        ```
    * **Response (example JSON - erro 400):**
        ```json
        {
            "message": "Invalid payment data"
        }
        ```