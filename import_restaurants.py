import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'melp_api.settings')  # Reemplaza con el nombre de tu proyecto
django.setup()

from restaurants.models import Restaurant
from uuid import UUID

def import_restaurants_from_csv(csv_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                # Convertir el ID a UUID
                row['id'] = UUID(row['id'])

                # Crear o actualizar el restaurante
                restaurant, created = Restaurant.objects.update_or_create(
                    id=row['id'],
                    defaults={
                        'rating': int(row['rating']),
                        'name': row['name'],
                        'site': row['site'],
                        'email': row['email'],
                        'phone': row['phone'],
                        'street': row['street'],
                        'city': row['city'],
                        'state': row['state'],
                        'lat': float(row['lat']),
                        'lng': float(row['lng'])
                    }
                )
                if created:
                    print(f"Restaurante creado: {restaurant.name} (ID: {restaurant.id})")
                else:
                    print(f"Restaurante actualizado: {restaurant.name} (ID: {restaurant.id})")
            except Exception as e:
                print(f"Error al procesar fila: {row} - {e}")


if __name__ == '__main__':
    csv_file_path = 'restaurantes.csv'  # Reemplaza con la ruta real
    import_restaurants_from_csv(csv_file_path)
