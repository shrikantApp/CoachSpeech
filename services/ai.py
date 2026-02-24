from openai import OpenAI
import json
from core.config import settings
from schemas.situation import SituationCreate

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_coach_response(context: SituationCreate) -> dict:
    prompt = f"""
    You are an expert sports coach responding to a situation.
    Sport: {context.sport_type}
    Athlete Age Group: {context.athlete_age_group}
    Situation: {context.situation_type} - {context.description}
    Parent Behavior: {context.parent_behavior}
    Desired Channel: {context.channel}
    Desired Tone: {context.tone}
    Urgency: {context.urgency}
    
    Please provide:
    1. A calm, professional, and empathetic primary response suitable for the desired channel.
    2. Two alternative responses (one slightly shorter, one slightly more structured).
    3. 3-5 keywords that emphasize empathy and professionalism in this context.
    
    Format the response as a valid JSON object matching this schema:
    {{
        "primary_response": "string",
        "alternate_responses": ["string", "string"],
        "keywords": ["string", "string", "string"]
    }}
    Ensure your output is strictly valid JSON without any markdown formatting blocks like ```json.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert sports coach and communicator. Always respond in valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )
        content = response.choices[0].message.content.strip()
        # Clean markdown code block if present
        if content.startswith("```json"):
            content = content[7:-3]
        elif content.startswith("```"):
            content = content[3:-3]
            
        data = json.loads(content)
        return data
    except Exception as e:
        error_str = str(e)
        # Fallback if AI fails or key is missing
        if "429" in error_str or "quota" in error_str.lower() or "incorrect api key" in error_str.lower():
            return {
                "primary_response": f"Dear Parent/Guardian,\n\nI understand your concern regarding the recent {context.situation_type.lower()} involving our {context.athlete_age_group} athletes. Our priority is always the well-being and development of the team.\n\nRegarding the situation: {context.description}\n\nI want to assure you that we are handling this {context.tone.lower()} and following our club policies. We appreciate your continued support and communication.\n\nBest regards,\nCoach",
                "alternate_responses": [
                    f"Hi there. I wanted to briefly address the {context.situation_type.lower()}. We are looking into '{context.description}' and will manage it appropriately. Thanks.",
                    f"Thank you for bringing this up. For the {context.athlete_age_group} group, we take these matters seriously. Let's discuss this further if needed."
                ],
                "keywords": ["understand", "priority", "support", "development"]
            }
        
        return {
            "primary_response": f"Error generating response: {error_str}\n\nPlease ensure OPENAI_API_KEY is configured correctly.",
            "alternate_responses": [],
            "keywords": ["error", "api-failure"]
        }
