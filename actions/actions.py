# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         print(" Iam from action py file.")
         dispatcher.utter_message(text="Hello World from my first action python code.")

         return []


class ActionSearchRestaurant(Action):

     def name(self) -> Text:
         return "action_search_hotel"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)


         for e in entities:
             if(e['entity']) == 'food':
                 name = e['value']
            
             if (name == "indian"):
                 message = "marriot, vivanta, liberty"
             if (name == "chinese"):
                 message = "bowl'o'china, Mainland china, sigri"
             if (name == "thai"):
                 message = "seloca, lobola, chensi"
             if (name == "italian"):
                 message = "papajones, nacys, little italy"
         dispatcher.utter_message(text=message)

         return []



class ActionCovidState(Action):

     def name(self) -> Text:
         return "action_covid_tracker"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         

         response = requests.get("https://api.covid19india.org/data.json").json()

         entities = tracker.latest_message['entities']
         print("Last message now",entities)

         
         for e in entities:
             if(e['entity']) == 'state':
                 state = e['value']
         message = "Please enter correct state name"

         if (state == "india"):
             state = "Total"

         for data in response['statewise']:
             if (data['state'] == state.title()):
                 print(data)
                 message = "Active:" + data['active'] + " " + "Confirmed:" + data['confirmed'] + " " + "Deaths:" + data['deaths'] + " " + "Daily cases:" + data['deltaconfirmed'] + " " + "Daily deaths:" + data['deltadeaths'] + " " + "Daily recovered:" + data['deltarecovered']

         print(message)
         dispatcher.utter_message(message)

         return []