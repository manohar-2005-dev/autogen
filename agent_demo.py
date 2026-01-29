from autogen import AssistantAgent, UserProxyAgent

# 1. Define the config list using the OpenAI-compatible format
config_list = [
    {
        "model": "llama-3.1-8b-instant", # Remove the 'groq/' prefix here
        "api_key": "api key here",  # Replace with your actual Groq API key
        "base_url": "https://api.groq.com/openai/v1", # This tells AutoGen to talk to Groq
        "price": [0, 0], # Optional: Prevents cost calculation errors
    }
]

# 2. Initialize the Assistant
assistant = AssistantAgent(
    name="assistant",
    llm_config={
        "config_list": config_list,
        "temperature": 0.7,
    }
)

# 3. Initialize the User Proxy
user_proxy = UserProxyAgent(
    name="user-proxy",
    human_input_mode="NEVER",
    code_execution_config={"use_docker": False}
)

# 4. Start the chat
user_proxy.initiate_chat(
    assistant,
    message="Hello, can you tell me a joke?",
    max_turns=2,
)