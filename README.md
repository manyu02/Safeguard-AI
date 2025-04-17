# SafeGuard AI 🚨
A chatbot system emphasising importance of quick measures in times of emergencies. It provides assistance in tackling the emrgency situation using modern technologies.
An AI-powered personal safety chatbot that can initiate emergency calls and detect your location in real time. Built using *Rasa, **Twilio, and **OpenCage/IP Geolocation APIs*.

---

## 🌐 Features

- ⚡ Emergency call feature using Twilio
- 📌 Location tracking:
  - Based on user input (e.g., "I am at Delhi")
  - Real-time fallback using IP geolocation
- 🔍 Smart response suggestions for safety tips
- ✉ Intent detection and entity extraction using Rasa NLU

---

## 📂 Project Structure


CHATBOT/
├── actions.py              # Custom actions (call, location)
├── location_tracker.py     # Coordinates using OpenCage
├── twilio_caller.py        # Twilio emergency call script
├── domain.yml              # Intents, entities, slots, actions
├── nlu.yml                 # Training examples
├── stories.yml             # Conversational stories
├── rules.yml               # Rules for triggering actions
├── config.yml              # NLU and core pipeline settings
├── endpoints.yml           # Action server endpoint
├── models/                 # Trained Rasa models
└── safeguard_env/          # Virtual environment


---

## 🚀 How to Run

### Step 1: Activate Virtual Environment
bash
cd CHATBOT
.\safeguard_env\Scripts\activate


### Step 2: Start Rasa Action Server
bash
rasa run actions


### Step 3: Train Rasa Model (if needed)
bash
rasa train


### Step 4: Start Rasa Shell
bash
rasa shell


---

## 🌍 Emergency Call Setup (Twilio)
- Set your *Twilio SID, **Auth Token, and **phone numbers* in twilio_caller.py
- Test with call_emergency intent

---

## 🌐 Location Tracking Setup
- User input tracked via location entity
- If location is not provided, fallback to IP-based detection (using http://ip-api.com/json)
- Coordinates fetched and stored in slots: user_location, user_latitude, user_longitude

---

## 📓 Sample Intents
yaml
- I am at [Delhi](location)
- Pin my location
- Share my location
- Where am I?
- Call my emergency contact!


---

## 🔎 Next Steps
- [ ] Integrate frontend UI (web app)
- [ ] Add WhatsApp/TG integration
- [ ] Store emergency contact info per user

---

## 📄 License
MIT

---

> Built with care ❤ to keep people safe.
