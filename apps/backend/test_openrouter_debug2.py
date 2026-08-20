"""Debug what URL is actually hit for each api_base variant."""
import asyncio
import httpx
import os

async def test_url(api_base: str, description: str):
    """Directly test what URL responds for OpenRouter."""
    print(f"\n=== {description} ===")
    print(f"api_base: {api_base}")
    url = f"{api_base}/chat/completions"
    print(f"Constructed URL: {url}")
    try:
        async with httpx.AsyncClient(timeout=10.0, follow_redirects=False) as client:
            resp = await client.post(
                url,
                json={
                    "model": "tencent/hy3:free",
                    "messages": [{"role": "user", "content": "Hi"}],
                    "max_tokens": 5,
                },
                headers={
                    "Authorization": "Bearer sk-or-invalid-key",
                    "HTTP-Referer": "http://localhost",
                    "X-Title": "Resume Matcher",
                    "Content-Type": "application/json",
                },
            )
        body = resp.text[:300]
        print(f"Status: {resp.status_code}")
        print(f"Location header: {resp.headers.get('location', 'none')}")
        print(f"Body (first 300): {body}")
        if "<!doctype html" in body.lower() or "<html" in body.lower():
            print(">>> HTML response detected!")
    except Exception as e:
        print(f"Exception: {type(e).__name__}: {e}")

async def main():
    # What LiteLLM uses when no api_base is given
    await test_url("https://openrouter.ai/api/v1", "DEFAULT (no api_base)")
    # What our code sends after stripping /v1
    await test_url("https://openrouter.ai/api", "STRIPPED /v1")
    # What happens with double v1
    await test_url("https://openrouter.ai/api/v1/v1", "DOUBLE v1")

asyncio.run(main())
