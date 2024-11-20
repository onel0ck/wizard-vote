# Bitcoin Wizards Art Voting Bot
Script for automatic voting on Bitcoin Wizards artworks with proxy support.
Telegram: https://t.me/unluck_1l0ck
X: https://x.com/1l0ck
## Features
- Proxy support with session management
- Random User-Agent rotation for each request  
- Customizable votes per artwork
- Built-in vote weighting (80% 5-star, 20% 4-star ratings)
- Random delays between votes
- Detailed logging system
- Support for both ID and full URL submission formats
## Environment
- Windows 7/8/8.1/10/11 (x64 only)
- macOS Intel/M1/M2
- Linux x64
## Installation
1. Clone the repository
```bash
git clone https://github.com/onel0ck/wizard-vote
cd wizard-vote
```
2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
## Setup
1. Create `id_url.txt` and add artwork IDs or URLs (one per line)
```
25248
25262
```
or
```
https://bitcoinwizards.vercel.app/submissions/25248
https://bitcoinwizards.vercel.app/submissions/25262
```
2. Create `proxies.txt` and add proxies (one per line)
```
http://user:pass@ip:port
```
## Usage
```bash
python main.py or python3 main.py
```
Results will be saved to:
- `votes_YYYYMMDD_HHMMSS.txt` - detailed voting results with proxy information
## Configuration
You can adjust the following parameters in `config.py`:
```python
MIN_DELAY = 1.5        # Minimum delay between votes
MAX_DELAY = 3.5        # Maximum delay between votes
VOTES_PER_ART_MIN = 10 # Minimum votes per artwork
VOTES_PER_ART_MAX = 20 # Maximum votes per artwork
```
## Requirements
- Python 3.8+
- aiohttp==3.9.1
- colorama==0.4.6
- asyncio==3.4.3
## Disclaimer
This script is for educational purposes only. Use at your own risk.
