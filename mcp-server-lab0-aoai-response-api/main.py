def main():
    print("Hello from aoai-response-mcp!")



import os
from openai import OpenAI
import dotenv

dotenv.load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
    default_query={"api-version": "preview"}
)

# response = client.responses.create(   
#   model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
#   input="This is a test.",
# )

response = client.responses.create(
    model="gpt-4.1",
    tools=[
        {
            "type": "mcp",
            "server_label": "deepwiki",
            "server_url": "https://mcp.deepwiki.com/mcp",
            "require_approval": "never",
        },
    ],
    input="What transport protocols are supported in the 2025-03-26 version of the MCP spec?",
)

print(response.model_dump_json(indent=2))

print("Response ID:", response.id)
print(response.output_text)

if __name__ == "__main__":
    main()
