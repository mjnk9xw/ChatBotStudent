from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class ActionIntroduce(Action):

    def name(self) -> Text:
        return 'utter_school_introduce'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="Em là con bot được tạo ra từ Nguyễn Văn Minh thuộc trường Học viện kỹ thuật quân sự , nếu muốn biết thêm chi tiết về trường xin vui lòng vào trang mta.edu.vn"
        )

        return []