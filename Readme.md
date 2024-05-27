# Melp Api

This API allows you to manage restaurant information and perform geographic queries.

## How to run it locally

 1. Clone the project.
 2. Create Venv:
````
python -m venv env
````
3. Install Dependencies:

```
pip install -r requirements.txt
```
4. Apply Migrations:
```
python manage.py makemigrations 
python manage.py migrate
```
5. Import CSV:
```
python import_restaurants.py
```
6. Run it
```
python manage.py runserver
```

## Endpoints

### `/api/restaurants/`  (GET, POST, PUT, PATCH, DELETE)

-   **GET:**  Retrieve a list of all restaurants or a specific restaurant by its ID (UUID).
-   **POST:**  Create a new restaurant.
-   **PUT:**  Fully update an existing restaurant by its ID.
-   **PATCH:**  Partially update an existing restaurant by its ID.
-   **DELETE:**  Delete a restaurant by its ID.


### `/restaurants/statistics/`  (GET)

Get statistics of restaurants within a specific radius.

#### Query Parameters:

-   `latitude`  (float): Latitude of the circle's center.
-   `longitude`  (float): Longitude of the circle's center.
-   `radius`  (float, optional): Radius of the circle in meters (default: 1000 meters).

#### Example:

    restaurants/statistics/?latitude=19.7006&longitude=-101.1843&radius=5000

