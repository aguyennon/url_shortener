from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from db import init_db, save_url, get_url
from pydantic import BaseModel
from signer import make_code, read_code
from lru_cache import LRUCache

cache = LRUCache(1000)
app = FastAPI()
init_db()

@app.get("/health")
def health():
    return {"status": "ok"}


class ShortenReq(BaseModel):
    long_url: str


@app.post("/shorten")
def shorten(request: ShortenReq): # direct to use the class
    get_id = save_url(request.long_url)
    code = make_code(get_id)

    return {"code": code, "short_url": f"http://127.0.0.1:8000/{code}"}


@app.get("/stats")
def stats():
    total_hits = cache.hits
    total_misses = cache.misses
    entries = len(cache.map) # number of entries cached currently
    total_lookups = total_hits + total_misses
    hit_ratio = (total_hits / total_lookups) if total_lookups else 0.0
    rounded_ratio = round(hit_ratio, 2)

    return {"hits": total_hits, "misses": total_misses, "current_entries": entries, "hit_ratio": rounded_ratio}
    

@app.get("/{code}")
def code_getter(code: str):
    new_id = read_code(code)
    if new_id is None:
        raise HTTPException(status_code=404, detail="Short link not found.")

    long_url = cache.get(new_id) # reads from memory
    if long_url is None:
        long_url = get_url(new_id) # reads from db
        if long_url is None:
            raise HTTPException(status_code=404, detail="Short link not found.")
        
        cache.put(new_id, long_url)


    return RedirectResponse(long_url)




    
