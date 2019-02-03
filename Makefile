start:
	pip install -r requirements.txt
	set FLASK_APP=main.py &&	flask run

deploy-gcp:
	gcloud app deploy
