docker exec -it geodjango_container python manage.py makemigrations
docker exec -it geodjango_container python manage.py migrate
docker exec -it geodjango_container \
    python manage.py shell \
    -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')"