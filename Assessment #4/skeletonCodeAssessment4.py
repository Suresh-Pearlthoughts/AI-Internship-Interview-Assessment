import random
import os
from gtts import gTTS

# Sample patient database with language preference, preferred communication channel, and age
patients = [
    {"id": 1, "name": "Ravi Kumar", "language": "Tamil", "age": 65},
    {"id": 2, "name": "Ananya Rao", "language": "Telugu", "age": 25},
    {"id": 3, "name": "Joseph Mathew", "language": "Malayalam", "age": 70},
    {"id": 4, "name": "Rahul Sharma", "language": "Hindi", "age": 45},
    {"id": 5, "name": "David Thomas", "language": "English", "age": 22},
]

# Predefined multi-language messages
messages = {
    "Tamil": "உங்கள் நேரம் உறுதிசெய்யப்பட்டது. தயவுசெய்து வருக!",
    "Telugu": "మీ నియామకం నిర్ధారించబడింది. దయచేసి రండి!",
    "Malayalam": "നിങ്ങളുടെ അപോയിന്റ്മെന്റ് സ്ഥിരീകരിച്ചിരിക്കുന്നു. ദയവായി വരൂ!",
    "Hindi": "आपका अपॉइंटमेंट कन्फर्म हो गया है। कृपया आएं!",
    "English": "Your appointment is confirmed. Please visit!"
}

# Simulated NLP Translation Function
def ai_translate(text, target_language):
    """Simulates AI-based translation (replace with actual NLP API if needed)"""
    return messages.get(target_language, text)

# Convert text to speech using Google Text-to-Speech (TTS)
def generate_voice_message(text, language, patient_name):
    """Generate and play voice message for IVR calls"""
    tts = gTTS(text=text, lang='ta' if language == "Tamil" else 'te' if language == "Telugu" else 'ml' if language == "Malayalam" else 'hi' if language == "Hindi" else 'en')
    current_dir = os.path.dirname(os.path.abspath(__file__))
       
     # Define the file path in the script directory
    file_name = f"{patient_name.replace(' ', '_')}_ivr_message.mp3"
    file_path = os.path.join(current_dir, file_name)  # Save in the script's directory
    
    # Save the audio file
    tts.save(file_path)
    
    if os.name == "nt":
        os.system(f'start wmplayer "{file_path}"')  
    else:
        os.system(f'mpg321 "{file_path}"') 

# Determine communication channel dynamically
def determine_channel(patient):
    if patient["age"] >= 60:
        return "IVR"  # Elderly patients prefer IVR
    elif patient["age"] < 30:
        return "WhatsApp"  # Younger patients prefer WhatsApp
    return "SMS"  # Default channel

# Simulated AI-enhanced message sending
def send_message(patient):
    language = patient["language"]
    message = ai_translate(messages.get(language, messages["English"]), language)
    channel = determine_channel(patient)
    
    if channel == "IVR":
        print(f"📞 Calling {patient['name']} ({language}) with voice message...")
        generate_voice_message(message, language, patient['name'])
    else:
        print(f"📩 Sending via {channel} to {patient['name']} ({language}): {message}")

# Simulating message sending to all patients
for patient in patients:
    send_message(patient)

# Effectiveness simulation with weighted confirmation probabilities
def measure_effectiveness():
    """Simulates confirmation tracking with A/B testing and channel effectiveness"""
    channel_effectiveness = {"WhatsApp": 0.85, "SMS": 0.65, "IVR": 0.75}  # Probabilities based on effectiveness
    confirmed = sum(random.choices([0, 1], weights=[1 - channel_effectiveness[determine_channel(p)], channel_effectiveness[determine_channel(p)]], k=1)[0] for p in patients)
    confirmation_rate = (confirmed / len(patients)) * 100
    
    # Simulating A/B testing with different languages
    lang_effectiveness = {lang: random.uniform(60, 90) for lang in messages.keys()}  # Random effectiveness rates
    
    print(f"✅ Confirmation Rate: {confirmation_rate:.2f}%")
    print("📊 A/B Testing Results:")
    for lang, rate in lang_effectiveness.items():
        print(f"   - {lang}: {rate:.2f}% success rate")
    
    # Simulated Patient Feedback based on channel effectiveness
    feedback_options = {
        "WhatsApp": "Users appreciate real-time notifications.",
        "SMS": "Some users find text messages easy to read.",
        "IVR": "Elderly patients prefer voice messages over text."
    }
    print("📝 Patient Satisfaction Survey:")
    for channel, feedback in feedback_options.items():
        print(f"   - {channel}: {feedback}")

measure_effectiveness()
