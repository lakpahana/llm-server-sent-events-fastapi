import openai as client
import asyncio
import os
from openai import Stream
from openai.types.chat import ChatCompletionChunk
import asyncio
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# https://platform.openai.com/docs/api-reference/assistants-streaming
# https://cookbook.openai.com/examples/how_to_stream_completions

# ChatCompletionChunk(id='{}{}{}', choices=[Choice(delta=ChoiceDelta(content='', function_call=None, refusal=None, role='assistant', tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1738176606, model='gpt-4o-mini-2024-07-18', object='chat.completion.chunk', service_tier='default', system_fingerprint='{}{}{}', usage=None)
# ChatCompletionChunk(id='{}{}{}', choices=[Choice(delta=ChoiceDelta(content='Hello', function_call=None, refusal=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1738176606, model='gpt-4o-mini-2024-07-18', object='chat.completion.chunk', service_tier='default', system_fingerprint='{}{}{}', usage=None)
# ChatCompletionChunk(id='{}{}{}', choices=[Choice(delta=ChoiceDelta(content='!', function_call=None, refusal=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1738176606, model='gpt-4o-mini-2024-07-18', object='chat.completion.chunk', service_tier='default', system_fingerprint='{}{}{}', usage=None)
# ChatCompletionChunk(id='{}{}{}', choices=[Choice(delta=ChoiceDelta(content=' How', function_call=None, refusal=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1738176606, model='gpt-4o-mini-2024-07-18', object='chat.completion.chunk', service_tier='default', system_fingerprint='{}{}{}', usage=None)
# ChatCompletionChunk(id='{}{}{}', choices=[Choice(delta=ChoiceDelta(content=' can', function_call=None, refusal=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1738176606, model='gpt-4o-mini-2024-07-18', object='chat.completion.chunk', service_tier='default', system_fingerprint='{}{}{}', usage=None)
# ChatCompletionChunk(id='{}{}{}', choices=[Choice(delta=ChoiceDelta(content=' I', function_call=None, refusal=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1738176606, model='gpt-4o-mini-2024-07-18', object='chat.completion.chunk', service_tier='default', system_fingerprint='{}{}{}', usage=None)
# ChatCompletionChunk(id='{}{}{}', choices=[Choice(delta=ChoiceDelta(content=' assist', function_call=None, refusal=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1738176606, model='gpt-4o-mini-2024-07-18', object='chat.completion.chunk', service_tier='default', system_fingerprint='{}{}{}', usage=None)
# ChatCompletionChunk(id='{}{}{}', choices=[Choice(delta=ChoiceDelta(content=' you', function_call=None, refusal=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1738176606, model='gpt-4o-mini-2024-07-18', object='chat.completion.chunk', service_tier='default', system_fingerprint='{}{}{}', usage=None)
# ChatCompletionChunk(id='{}{}{}', choices=[Choice(delta=ChoiceDelta(content=' today', function_call=None, refusal=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1738176606, model='gpt-4o-mini-2024-07-18', object='chat.completion.chunk', service_tier='default', system_fingerprint='{}{}{}', usage=None)
# ChatCompletionChunk(id='{}{}{}', choices=[Choice(delta=ChoiceDelta(content='?', function_call=None, refusal=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1738176606, model='gpt-4o-mini-2024-07-18', object='chat.completion.chunk', service_tier='default', system_fingerprint='{}{}{}', usage=None)
# ChatCompletionChunk(id='{}{}{}', choices=[Choice(delta=ChoiceDelta(content=None, function_call=None, refusal=None, role=None, tool_calls=None), finish_reason='stop', index=0, logprobs=None)], created=1738176606, model='gpt-4o-mini-2024-07-18', object='chat.completion.chunk', service_tier='default', system_fingerprint='{}{}{}', usage=None)


# data: 

# data: Hello

# data: !

# data:  How

# data:  can

# data:  I

# data:  assist

# data:  you

# data:  today

# data: ?

# data: None

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
                await asyncio.sleep(0.5)
                                    
    except Exception as e:
        print(f"Error during streaming: {str(e)}")
        yield f"Error: {str(e)}"