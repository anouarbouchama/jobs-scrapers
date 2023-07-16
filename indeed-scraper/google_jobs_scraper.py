from utils import google_jobs_scrape
from constants import SEARCH_QUERIES

for search_query in SEARCH_QUERIES:
    google_jobs_scrape(search_query)