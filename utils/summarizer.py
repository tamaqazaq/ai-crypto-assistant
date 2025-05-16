import requests

def summarize(context, query):
    print("🧠 Sending request to Ollama...")  
    prompt = f"Answer briefly: {query}. Info: {context}"
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            },
            timeout=10
        )
        print("Got response!") 

        if response.status_code == 200:
            return response.json()["response"].strip()
        else:
            return f"Model error: {response.status_code} — {response.text}"

    except Exception as e:
        return f"Error: {str(e)}"
