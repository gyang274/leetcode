import random

class Codec:

  def __init__(self):
    self.urls = {}
    self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

  def keygen(self) -> str:
    # key generator
    return "".join(random.choices(self.alphabet, k = 8))
    
  def encode(self, longUrl: str) -> str:
    """Encodes a URL to a shortened URL.
    """
    key = self.keygen()
    while key in self.urls:
      key = self.keygen()
    self.urls[key] = longUrl
    return "http://tinyurl.com/" + key

  def decode(self, shortUrl: str) -> str:
    """Decodes a shortened URL to its original URL.
    """
    return self.urls.get(shortUrl.replace("http://tinyurl.com/", ""))
