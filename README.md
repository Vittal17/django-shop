```markdown
# Simple Django Store (Products + Cart)

This is a minimal Django project (shop) with an app (store) that lists products in a Bootstrap card grid and provides a simple session-based cart.

Quick start
1. Create and activate a virtualenv:
   - python3 -m venv venv
   - source venv/bin/activate   (Windows: venv\Scripts\activate)

2. Install Django:
   - pip install django

3. Make migrations and migrate:
   - python manage.py makemigrations
   - python manage.py migrate

4. Load sample products:
   - python manage.py loaddata store/fixtures/products.json

5. Run the dev server:
   - python manage.py runserver

6. Open http://127.0.0.1:8000/ to view the product list.

Notes
- Images in the fixtures are remote URLs. Update products in the admin after creating a superuser if needed.
- Cart is session-based for simplicity.
- For production: set DEBUG=False, secure SECRET_KEY, configure allowed hosts, and host static/media properly.

What's next
- Add product detail pages.
- Add quantity adjustments / remove-from-cart functionality.
- Persist carts for logged-in users / add checkout integration.
```