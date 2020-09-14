# clone core and install
git clone https://github.com/RasaHQ/rasa_core.git
cd rasa_core
pip install -r requirements.txt
pip install -e .

pip install rasa_nlu[tensorflow]

# docs
https://viblo.asia/p/hieu-rasa-qua-quy-trinh-xay-dung-mot-chatbot-giup-ban-tra-loi-cau-hoi-hom-nay-an-gi-WAyK8P4pKxX
https://viblo.asia/p/xay-dung-chatbot-messenger-cap-nhat-thoi-khoa-bieu-cho-sinh-vien-phan-1-phan-tich-thiet-ke-he-thong-OeVKBW8QZkW

# train 
rasa train -c config.yml -o models --verbos

rasa x --debug --enable-api --cors "*" --port 5007 --rasa-x-port 5008