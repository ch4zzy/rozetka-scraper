# rozetka-scraper
Data collection from rozetka.ua store by category

## Using 

Paste your url category and count of maximum pages for this category. 

```
cd rozetka-scraper

virtualenv --python=/usr/bin/python3.10 venv

source venv/bin/activate

pip install -r requirements.txt

python main.py
```

Once the data is collected, the data file will be in the output folder with the name of the category.
