import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

def generate_conversation(meeting_notes):
    # Generate conversation context using OpenAI's GPT-3.5 model
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=meeting_notes,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
    )
    
    return response.choices[0].text.strip()

# Example usage
meeting_notes = """
Meeting Notes:

- Discussing project updates and milestones.
- Reviewing the marketing strategy for the upcoming product launch.
- Brainstorming ideas for improving customer engagement.
"""

conversation_context = generate_conversation(meeting_notes)
print(conversation_context)
