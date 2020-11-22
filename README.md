# install
pip install underthesea
pip install rasa_nlu
pip3 install rasa
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
rasa init --no-prompt

# train
rasa train nlu
rasa shell nlu
rasa train

# run 
rasa x
rasa run actions

# luồng chat bot
https://images.viblo.asia/e2016b18-7197-4eb0-91a2-abe95e55b2e8.PNG

# chỉnh vi tokenizer cho chat bot 
path: /home/mjnk9xw/anaconda3/envs/chatbotenv/lib/python3.6/site-packages/rasa/nlu
copy thư mục + chỉnh file registry.py để nhận namespace.