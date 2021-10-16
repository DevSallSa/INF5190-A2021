default: all

export FLASK_APP=app/app.py
export FLASK_ENV=development

.PHONY: all clean html

all: flask

flask:
	npx tailwindcss -i app/styles/tailwind.css -o app/static/styles/styles.css && flask run

