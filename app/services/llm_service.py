import openai as client
import asyncio
import os
from openai import Stream
from openai.types.chat import ChatCompletionChunk

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# https://platform.openai.com/docs/api-reference/assistants-streaming
# https://cookbook.openai.com/examples/how_to_stream_completions
async def openai_stream(prompt: str):
    try:
        response = client.chat.completions.create(
        model='gpt-4o-mini',
         messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        temperature=0,
        stream=True
        )

        for chunk in response:
            print(chunk)
            if isinstance(chunk, ChatCompletionChunk):
                yield f"data: {chunk.choices[0].delta.content}\n\n" 
                                    
    except Exception as e:
        print(f"Error during streaming: {str(e)}")
        yield f"Error: {str(e)}"