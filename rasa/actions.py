# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from database_connectivity import DataUpdate
# from exel_data_store_read import DataStore

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import webbrowser

class ActionVideo(Action):
    def name(self) -> Text:
        return "action_video"

    async def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        video_url="https://youtu.be/hoNb6HuNmU0"
        dispatcher.utter_message("wait... Playing your video.")
        webbrowser.open(video_url)
        return []


#  store the name number in csv..................................................................
# class ActionSaveData(Action):
#     def name(self) -> Text:
#         return "action_save_data"

#     async def run(
#         self,
#         dispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         # store the data in csv
#         DataStore(
#             tracker.get_slot("name"),
#             tracker.get_slot("number"))

#         dispatcher.utter_message("Data Added successfully...... !")
      
#         return []

# ......................................................................................

# class ValidateRestaurantForm(Action):
#     def name(self) -> Text:
#         return "user_details_form"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         required_slots = ["name", "number"]

#         for slot_name in required_slots:
#             if tracker.slots.get(slot_name) is None:
#                 # The slot is not filled yet. Request the user to fill this slot next.
#                 return [SlotSet("requested_slot", slot_name)]

#         # All slots are filled.
#         return [SlotSet("requested_slot", None)]

# class ActionSubmit(Action):
#     def name(self) -> Text:
#         return "action_save_data"

#     def run(
#         self,
#         dispatcher,
#         tracker: Tracker,
#         domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         #  for showing the message ...
#         # dispatcher.utter_message(template="utter_details_thanks",
#         #                          Name=tracker.get_slot("name"),
#         #                          Mobile_number=tracker.get_slot("number"))

#         DataUpdate(tracker.get_slot("name"),tracker.get_slot("number"))
#         dispatcher.utter_message("Thanks Now you can ask your question ....!")

#         return[]