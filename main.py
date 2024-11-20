import asyncio
import aiohttp
from typing import List
from datetime import datetime
from colorama import init, Fore
from config import *
from utils import VotingSession, read_proxies, read_submissions

init(autoreset=True)

async def vote_with_proxy(proxy: str, submission_urls: List[str], votes_needed: dict) -> dict:
   result = {
       "proxy": proxy,
       "submission": None,
       "vote_value": None,
       "error": None
   }
   
   try:
       async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
           voting_session = VotingSession(proxy, submission_urls)
           
           if not await voting_session.initialize_session(session):
               result["error"] = "Failed to initialize session"
               return result

           available_submissions = [url for url, votes in votes_needed.items() if votes > 0]
           if not available_submissions:
               result["error"] = "No submissions available"
               return result

           submission = random.choice(available_submissions)
           if await voting_session.vote_for_submission(session, submission):
               result["submission"] = submission
               votes_needed[submission] -= 1
               print(f"{Fore.GREEN}[Success] {proxy} voted for {submission.split('/')[-1]}")
           else:
               result["error"] = "Voting failed"
               
   except Exception as e:
       result["error"] = f"Error: {str(e)}"
       
   return result

async def main():
   proxies = read_proxies()
   submission_urls = read_submissions()
   
   if not submission_urls:
       print(f"{Fore.RED}No submissions found in {SUBMISSIONS_FILE}")
       return
   
   if not proxies:
       print(f"{Fore.RED}No proxies found in {PROXIES_FILE}")
       return
   
   print(f"Starting Art Voting Bot...")
   print(f"Total proxies: {len(proxies)}")
   print(f"Total submissions: {len(submission_urls)}\n")
   
   votes_needed = {
       url: random.randint(VOTES_PER_ART_MIN, VOTES_PER_ART_MAX)
       for url in submission_urls
   }
   
   total_votes_needed = sum(votes_needed.values())
   print(f"Total votes to be cast: {total_votes_needed}\n")
   
   for url, votes in votes_needed.items():
       print(f"Submission {url.split('/')[-1]}: {votes} votes planned")
   
   tasks = []
   for proxy in proxies:
       if any(votes > 0 for votes in votes_needed.values()):
           task = asyncio.create_task(vote_with_proxy(proxy, submission_urls, votes_needed))
           tasks.append(task)
           await asyncio.sleep(random.uniform(MIN_DELAY, MAX_DELAY))
   
   results = await asyncio.gather(*tasks, return_exceptions=True)
   
   timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
   with open(f"votes_{timestamp}.txt", "w") as f:
       successful_votes = 0
       failed_votes = 0
       
       for r in results:
           if isinstance(r, dict):
               if r["error"]:
                   f.write(f"Proxy: {r['proxy']} | Error: {r['error']}\n")
                   failed_votes += 1
               else:
                   submission_id = r["submission"].split('/')[-1] if r["submission"] else "Unknown"
                   f.write(f"Proxy: {r['proxy']} | Voted for: {submission_id}\n")
                   successful_votes += 1

       f.write(f"\nTotal successful votes: {successful_votes}")
       f.write(f"\nTotal failed votes: {failed_votes}")
       
   print(f"\n{Fore.CYAN}=== Voting Complete ===")
   print(f"Successful votes: {successful_votes}")
   print(f"Failed votes: {failed_votes}")
   print(f"Results saved to: votes_{timestamp}.txt")

if __name__ == "__main__":
   asyncio.run(main())