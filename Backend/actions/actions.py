# import requests
# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet
# from rasa_sdk.executor import CollectingDispatcher
# from twilio_caller import make_emergency_call
# from location_tracker import get_coordinates



# class ActionCallEmergencyContact(Action):
#     def name(self):
#         return "action_call_emergency_contact"

#     def run(self, dispatcher, tracker, domain):
#         call_status = make_emergency_call()
#         dispatcher.utter_message(text="Emergency call initiated successfully.")
#         return [SlotSet("call_status", call_status)]

# class ActionGetLocation(Action):
#     def name(self):
#         return "action_get_location"

#      def fetch_ip_based_location(self):
#         """Fetch user's location using IP address via ip-api.com"""
#         url = "http://ip-api.com/json"
#         response = requests.get(url)

#         if response.status_code == 200:
#             data = response.json()
#             location_info = f"{data['city']}, {data['regionName']}, {data['country']}"
#             latitude = data['lat']
#             longitude = data['lon']
#             return location_info, latitude, longitude
#         return None, None, None

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
#         user_location = next(tracker.get_latest_entity_values("location"), None)

#         # Case 1: If the user mentions an Indian state, use predefined coordinates
#          if user_location:
#             coordinates = get_coordinates(user_location)
#             if coordinates:
#                 latitude, longitude = coordinates
#                 message = f"Your location is recorded: {user_location} (Lat: {latitude}, Long: {longitude})"
#             else:
#                 message = f"I couldn't find the coordinates for {user_location}."
#                 latitude, longitude = None, None
#         else:
#             # Use IP-based location if user doesn't mention location
#             user_location, latitude, longitude = self.fetch_ip_based_location()
#             if user_location:
#                 message = f"I detected your location as {user_location} (Lat: {latitude}, Long: {longitude})"
#             else:
#                 message = "I couldn't detect your location. Please try again."

#         dispatcher.utter_message(text=message)

#         return [
#             SlotSet("user_location", user_location),
#             SlotSet("user_latitude", latitude),
#             SlotSet("user_longitude", longitude)
#         ]


# import requests
# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet
# from rasa_sdk.executor import CollectingDispatcher
# from twilio_caller import make_emergency_call
# from location_tracker import get_coordinates


# class ActionCallEmergencyContact(Action):
#     def name(self):
#         return "action_call_emergency_contact"

#     def run(self, dispatcher, tracker, domain):
#         call_status = make_emergency_call()
#         dispatcher.utter_message(text="Emergency call initiated successfully.")
#         return [SlotSet("call_status", call_status)]


# class ActionGetLocation(Action):
#     def name(self):
#         return "action_get_location"

#     def fetch_ip_based_location(self):
#         """Fetch user's location using IP address via ip-api.com"""
#         url = "http://ip-api.com/json"
#         response = requests.get(url)

#         if response.status_code == 200:
#             data = response.json()
#             location_info = f"{data['city']}, {data['regionName']}, {data['country']}"
#             latitude = data['lat']
#             longitude = data['lon']
#             return location_info, latitude, longitude
#         return None, None, None

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
#         user_location = next(tracker.get_latest_entity_values("location"), None)

#         if user_location:
#             # If the user mentions an Indian state/city, get coordinates using OpenCage
#             coordinates = get_coordinates(user_location)
#             if coordinates:
#                 latitude, longitude = coordinates
#                 message = f"Your location is recorded: {user_location} (Lat: {latitude}, Long: {longitude})"
#             else:
#                 message = f"I couldn't find the coordinates for {user_location}."
#                 latitude, longitude = None, None
#         else:
#             # Use IP-based location if user doesn't mention location
#             user_location, latitude, longitude = self.fetch_ip_based_location()
#             if user_location:
#                 message = f"I detected your location as {user_location} (Lat: {latitude}, Long: {longitude})"
#             else:
#                 message = "I couldn't detect your location. Please try again."

#         dispatcher.utter_message(text=message)

#         return [
#             SlotSet("user_location", user_location),
#             SlotSet("user_latitude", latitude),
#             SlotSet("user_longitude", longitude)
#         ]

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from twilio_caller import make_emergency_call
from location_tracker import get_coordinates


class ActionCallEmergencyContact(Action):
    def name(self):
        return "action_call_emergency_contact"

    def run(self, dispatcher, tracker, domain):
        call_status = make_emergency_call()
        dispatcher.utter_message(text="Emergency call initiated successfully.")
        return [SlotSet("call_status", call_status)]


class ActionGetLocation(Action):
    def name(self):
        return "action_get_location"

    def fetch_ip_based_location(self):
        """Fetch user's location using IP address via ip-api.com"""
        url = "http://ip-api.com/json"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            location_info = f"{data['city']}, {data['regionName']}, {data['country']}"
            latitude = data['lat']
            longitude = data['lon']
            return location_info, latitude, longitude
        return None, None, None

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        user_location = next(tracker.get_latest_entity_values("location"), None)

        # DEBUG: Log extracted location from user
        print(f"DEBUG: Extracted location entity = {user_location}")

        if user_location:
            # If the user mentions a location, get coordinates using OpenCage
            coordinates = get_coordinates(user_location)
            if coordinates:
                latitude, longitude = coordinates
                message = f"Your location is recorded: {user_location} (Lat: {latitude}, Long: {longitude})"
            else:
                message = f"I couldn't find the coordinates for {user_location}."
                latitude, longitude = None, None
        else:
            # Use IP-based location if user doesn't mention location
            user_location, latitude, longitude = self.fetch_ip_based_location()
            if user_location:
                message = f"I detected your location as {user_location} (Lat: {latitude}, Long: {longitude})"
            else:
                message = "I couldn't detect your location. Please try again."

        dispatcher.utter_message(text=message)

        return [
            SlotSet("user_location", user_location),
            SlotSet("user_latitude", latitude),
            SlotSet("user_longitude", longitude)
        ]
