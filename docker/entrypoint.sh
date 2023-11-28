set +e 
echo "==> Django setup, executing: makemigrations "
python3 manage.py makemigrations
echo "==> Django setup, executing: migrate pro"
python3 manage.py migrate
echo "==> Django Run Server"
python3 manage.py runserver 0.0.0.0:8000