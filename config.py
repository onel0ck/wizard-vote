import random

CONCURRENT_TASKS = 10
MIN_DELAY = 1.5
MAX_DELAY = 3.5

VOTES_PER_ART_MIN = 10
VOTES_PER_ART_MAX = 20

RATINGS = [5] * 80 + [4] * 20

BASE_URL = "https://bitcoinwizards.vercel.app"
CSRF_ENDPOINT = f"{BASE_URL}/api/csrf"
SUBMISSION_ENDPOINT = f"{BASE_URL}/api/submissions"
RATE_ENDPOINT = f"{BASE_URL}/api/submissions/rate"

SUBMISSIONS_FILE = "id_url.txt"
PROXIES_FILE = "proxies.txt"