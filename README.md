# FAQ Project

A Django application for managing Frequently Asked Questions (FAQs) with multilingual support. This project automatically translates FAQ content from English to Hindi and Bengali using the `googletrans` library, supports rich text editing via CKEditor, and exposes RESTful API endpoints using Django REST Framework.

---

## Features

- **FAQ Management:** Create, update, and delete FAQs through the Django admin interface.
- **Automatic Translations:** Automatically translates FAQ content from English to Hindi and Bengali during save operations.
- **Rich Text Support:** Utilize CKEditor for rich text formatting in FAQ answers.
- **REST API:** Access FAQ data through a RESTful API with language-specific content.
- **Caching:** Uses Redis to cache translations for 1 hour to improve performance.

---

## Prerequisites

- **Python 3.7+**
- **Redis:** Ensure a Redis server is running on `127.0.0.1:6379` (default configuration).
- **Pip:** Package installer for Python.

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/officialasishkumar/faq-django
   cd faq-django
   ```

2. **Set Up a Virtual Environment:**

   Create and activate a virtual environment to manage dependencies.

   ```bash
   python -m venv env
   source env/bin/activate   # For Linux/macOS
   env\Scripts\activate      # For Windows
   ```

3. **Install Dependencies:**

   Install the required packages. Ensure your `requirements.txt` includes:

   - Django
   - djangorestframework
   - django-ckeditor
   - django-redis
   - googletrans

   Run:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Redis (if needed):**

   The project is configured to use Redis at `redis://127.0.0.1:6379/1`. Adjust the settings in `faq_project/settings.py` if your Redis server runs on a different host/port.

---

## Database Setup

1. **Create Migrations:**

   ```bash
   python manage.py makemigrations faq
   ```

2. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

3. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

---

## Running the Application

Start the development server with:

```bash
python manage.py runserver
```

- **Admin Interface:**  
  Access the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

- **API Endpoints:**  
  Access the FAQ API at [http://127.0.0.1:8000/api/faqs/](http://127.0.0.1:8000/api/faqs/).

  You can add a query parameter `lang` (e.g., `?lang=hi` or `?lang=bn`) to the API endpoint URL to fetch the FAQ in Hindi or Bengali respectively.

---

## Testing the Application

### Using Django's Test Framework

Run the tests using the following command:

```bash
python manage.py test
```

### Manual Testing via Browser or API Tools

1. **Browser:** (preferred)
   - Visit the API endpoint in your browser: [http://127.0.0.1:8000/api/faqs/](http://127.0.0.1:8000/api/faqs/).
   - Append `?lang=hi` or `?lang=bn` to the URL to test multilingual support. For example:  
     [http://127.0.0.1:8000/api/faqs/?lang=hi](http://127.0.0.1:8000/api/faqs/?lang=hi)

2. **cURL:**
   - Test the default (English) FAQ list:
   
     ```bash
     curl http://127.0.0.1:8000/api/faqs/
     ```
   
   - Test for Hindi FAQs:
   
     ```bash
     curl http://127.0.0.1:8000/api/faqs/?lang=hi
     ```
   
   - Test for Bengali FAQs:
   
     ```bash
     curl http://127.0.0.1:8000/api/faqs/?lang=bn
     ```
---

## Additional Notes

- **Caching:** FAQ translations are cached for 1 hour using Redis. If the translation is already cached, it will be served from the cache.
- **Translation Fallback:** In case of translation failures, the original English text is used as a fallback.
- **CKEditor Configuration:** The CKEditor toolbar and dimensions can be customized in the `CKEDITOR_CONFIGS` in `faq_project/settings.py`.
