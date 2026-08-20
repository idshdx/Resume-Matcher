"""Temporary debug script for OpenRouter health check."""
import asyncio
import litellm
import os

litellm.set_verbose = True

async def test_no_base():
    """Test with no api_base (should use default openrouter.ai/api/v1)."""
    print("\n=== TEST 1: No api_base ===")
    try:
        r = await litellm.acompletion(
            model="openrouter/tencent/hy3:free",
            messages=[{"role": "user", "content": "Hi"}],
            max_tokens=5,
            api_key="sk-or-invalid-key",
            api_base=None,
            extra_headers={
                "HTTP-Referer": "http://localhost",
                "X-Title": "Resume Matcher",
            },
            timeout=10,
        )
        print("ok:", r)
    except Exception as e:
        print("ERROR TYPE:", type(e).__name__)
        msg = str(e)
        print("ERROR MSG (first 800):", msg[:800])
        if "<!doctype html" in msg.lower() or "<html" in msg.lower():
            print(">>> DETECTED: HTML response!")

async def test_with_base():
    """Test with explicit api_base stripped of /v1."""
    print("\n=== TEST 2: api_base = https://openrouter.ai/api (stripped /v1) ===")
    try:
        r = await litellm.acompletion(
            model="openrouter/tencent/hy3:free",
            messages=[{"role": "user", "content": "Hi"}],
            max_tokens=5,
            api_key="sk-or-invalid-key",
            api_base="https://openrouter.ai/api",
            extra_headers={
                "HTTP-Referer": "http://localhost",
                "X-Title": "Resume Matcher",
            },
            timeout=10,
        )
        print("ok:", r)
    except Exception as e:
        print("ERROR TYPE:", type(e).__name__)
        msg = str(e)
        print("ERROR MSG (first 800):", msg[:800])
        if "<!doctype html" in msg.lower() or "<html" in msg.lower():
            print(">>> DETECTED: HTML response!")

async def test_with_full_base():
    """Test with full api_base including /v1."""
    print("\n=== TEST 3: api_base = https://openrouter.ai/api/v1 (full) ===")
    try:
        r = await litellm.acompletion(
            model="openrouter/tencent/hy3:free",
            messages=[{"role": "user", "content": "Hi"}],
            max_tokens=5,
            api_key="sk-or-invalid-key",
            api_base="https://openrouter.ai/api/v1",
            extra_headers={
                "HTTP-Referer": "http://localhost",
                "X-Title": "Resume Matcher",
            },
            timeout=10,
        )
        print("ok:", r)
    except Exception as e:
        print("ERROR TYPE:", type(e).__name__)
        msg = str(e)
        print("ERROR MSG (first 800):", msg[:800])
        if "<!doctype html" in msg.lower() or "<html" in msg.lower():
            print(">>> DETECTED: HTML response!")

async def main():
    await test_no_base()
    await test_with_base()
    await test_with_full_base()

asyncio.run(main())
