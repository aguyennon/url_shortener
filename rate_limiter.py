from collections import deque
import time


class RateLimiter:

    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {} # each key = ip, each value = collection of that ip's request times


    def allow(self, ip, now=None):
        if now is None:
            now = time.time() 

        if ip not in self.requests:
            self.requests[ip] = deque()

        queue = self.requests[ip]

        while queue and now - queue[0] >= self.window_seconds:
            queue.popleft()

        if len(queue) >= self.max_requests:
            return False

        queue.append(now)
        return True

    def cleanup(self, now):

        for ip in list(self.requests):
            queue = self.requests[ip]
            if not queue or now - queue[-1] >= self.window_seconds:
                del self.requests[ip]



if __name__ == "__main__":
    rl = RateLimiter(2, 60)

    print(rl.allow("1.2.3.4"))
    print(rl.allow("1.2.3.4"))
    print(rl.allow("1.2.3.4"))
        


