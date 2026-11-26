from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from db import init_db, save_url, get_url
from pydantic import BaseModel
from signer import make_code, read_code
from lru_cache import LRUCache
from rate_limiter import RateLimiter

rl = RateLimiter(60, 60)
cache = LRUCache(1000)
click_counts = {}
app = FastAPI()
init_db()


def _request_and_raise(request: Request):
    ip = request.client.host # get ip from address it came from

    if not rl.allow(ip):
        raise HTTPException(status_code=429, detail="Too many requests.")


@app.get("/health")
def health():
    return {"status": "ok"}


class ShortenReq(BaseModel):
    long_url: str


@app.post("/shorten")
def shorten(body: ShortenReq, request: Request): # direct to use the class
    _request_and_raise(request)

    url_id = save_url(body.long_url)
    code = make_code(url_id)

    return {"code": code, "short_url": f"http://127.0.0.1:8000/{code}"}


@app.get("/stats")
def stats():
    total_hits = cache.hits
    total_misses = cache.misses
    entries = len(cache.map) # number of entries cached currently
    total_lookups = total_hits + total_misses
    hit_ratio = (total_hits / total_lookups) if total_lookups else 0.0
    rounded_ratio = round(hit_ratio, 2)

    return {"hits": total_hits, "misses": total_misses, "current_entries": entries, "hit_ratio": rounded_ratio, "click_counts": click_counts}
    

@app.get("/{code}")
def code_getter(code: str, request: Request):
    _request_and_raise(request)

    url_id = read_code(code)
    if url_id is None:
        raise HTTPException(status_code=404, detail="Short link not found.")

    long_url = cache.get(url_id) # reads from memory
    if long_url is None:
        long_url = get_url(url_id) # reads from db
        if long_url is None:
            raise HTTPException(status_code=404, detail="Short link not found.")
        
        cache.put(url_id, long_url)

    click_counts[url_id] = click_counts.get(url_id, 0) + 1
    return RedirectResponse(long_url)



