import csv
from django.core.management.base import BaseCommand
from django.db import transaction
from dandd_app.models import Category, Product

class Command(BaseCommand):
    help = 'Import products from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            
            # Print column names for debugging
            self.stdout.write(f"CSV columns: {reader.fieldnames}")
            
            with transaction.atomic():
                for row in reader:
                    try:
                        category, _ = Category.objects.get_or_create(name=row.get('Category', 'Uncategorized'))
                        
                        product, created = Product.objects.update_or_create(
                            sku=row['SKU'],
                            defaults={
                                'upc': row.get('UPC', ''),
                                'category': category,
                                'brand': row.get('Brand', ''),
                                'product_name': row.get('Product Name', ''),
                                'title_english': row.get('Title English', ''),
                                'color_english': row.get('Color English', ''),
                                'size_english': row.get('Size English', ''),
                                'images_link': row.get('images link', ''),
                                'english_description': row.get('ENGLISH DESCRIPTION', ''),
                                'msrp': float(row.get(' MSRP ', '0').replace('$', '').strip() or 0),
                                'net_weight': float(row.get('Net Weight', '0') or 0),
                                'net_weight_unit': row.get('Net Weigth Unit', ''),
                                'case_width': float(row.get('Case Width', '0') or 0),
                                'case_length': float(row.get('Case Length', '0') or 0),
                                'case_height': float(row.get('Case Height', '0') or 0),
                                'case_unit': row.get('Case Unit', ''),
                                'pieces_per_case': int(row.get('# of pcs/case', '0') or 0)
                            }
                        )
                        
                        if created:
                            self.stdout.write(self.style.SUCCESS(f'Created product: {product}'))
                        else:
                            self.stdout.write(self.style.SUCCESS(f'Updated product: {product}'))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Error processing row: {row}'))
                        self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))

        self.stdout.write(self.style.SUCCESS('Data import completed successfully'))