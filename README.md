# Food Tracker Analytics Server

This repository contains the backend server for a food tracking application. The server is built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Overview

The server is responsible for handling analytics data from the client application. It provides endpoints to log events and to check the server's status. The analytics data is stored in Google BigQuery for further analysis.

### Endpoints

1. **POST /analytics**
   - **Description:** Accepts analytics data from the client and inserts it into a Google BigQuery table.
   - **Request Body:**
     ```json
     {
       "user_id": "string",
       "name": "string",
       "parameters": "string",
       "timestamp": 123456789,
       "appVersion": "string"
     }
     ```
   - **Response:** No content (HTTP 200 OK) if successful.

2. **GET /ping**
   - **Description:** Checks if the server is running.
   - **Response:**
     ```json
     {
       "ping": "pong!"
     }
     ```

### Setup and Running the Server

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up Google Cloud BigQuery:**
   - Ensure you have a Google Cloud account and have enabled the BigQuery API (it is free).
   - Create a BigQuery dataset and table with the appropriate schema.
     ```json
     {
       "fields": [
         {
           "name": "userId",
           "type": "STRING",
           "mode": "REQUIRED"
         },
         {
           "name": "name",
           "type": "STRING",
           "mode": "REQUIRED"
         },
         {
           "name": "parameters",
           "type": "STRING",
           "mode": "NULLABLE"
         },
         {
           "name": "timestamp",
           "type": "INTEGER",
           "mode": "REQUIRED"
         },
         {
           "name": "appVersion",
           "type": "STRING",
           "mode": "NULLABLE"
         }
       ]
     }
     ```
   - Set up authentication by creating a service account key and setting the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of the key file.

3. **Run the Server:**
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8080
   ```
   - The server will start and be accessible at `http://127.0.0.1:8080`.
   - API documentation will be available at `http://127.0.0.1:8080/docs`.

### Interaction with `analytics.dart`

The `analytics.dart` file in the [Dart project](www.example.com) sends analytics data to this server. Key points of interaction include:

- The `Analytics` class in `analytics.dart` is responsible for logging events.
- Events are sent to the server using the `addEventToServer` method of a `Backend` class.
- The server receives these events via POST requests to the `/analytics` endpoint.

## License

The Food Tracker Application is released under the GNU General Public License v3.0. You are free to use, modify, and distribute the software under the terms of this license. For more details, please refer to the [LICENSE](LICENSE) file.