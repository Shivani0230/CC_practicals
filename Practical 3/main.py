from openai import AzureOpenAI

# Correct Azure OpenAI resource details
client = AzureOpenAI(
    api_key="DVJjHWs1ynnxYmgKIfaiPcUpErk2YrGkJNZ6WkvGzx1Kvcy2F7O2JQQJ99BDACHYHv6XJ3w3AAAAACOGNUTU",  # Replace with your actual Azure key
    azure_endpoint="https://syada-m9n3d8s8-eastus2.cognitiveservices.azure.com",  # Base endpoint only
    api_version="2024-12-01-preview"
)

# Chat completion call
response = client.chat.completions.create(
    model="ShivaniPracticalCC",  # Deployment name from Azure
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "I am going to Delhi, what should I see?"}
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0
)

# Print the assistant's reply
print(response.choices[0].message.content)
