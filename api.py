# -*- coding: utf-8 -*-
"""
처음에 user_id를 가지고 있다가, API 형식으로 Bot에서 계산한 숫자를 전달하는 역할입니다.
"""

from flask import Flask, request, jsonify

from bot import Bot
from bot import is_valid_format


app = Flask(__name__)
user_history = {}

def message_to_json(message):
    return jsonify({'messages': [{'text': message}]})


@app.route('/question', methods=['GET'])
def question():
    user_id = request.args.get('user', None)
    answer = request.args.get('answer', None)

    if (answer is None) | (answer == '게임 시작하기'):
        user_history[user_id] = Bot()
        return message_to_json(user_history[user_id].get_next_question())

    if not is_valid_format(answer):
        return message_to_json("'{}'는 적절한 답변 형식이 아닙니다. '1S2B'와 같은 형식을 지켜주세요!".format(answer))

    bot = user_history[user_id]

    if not bot.save_answer(bot.current['turn'], int(answer[0]), int(answer[2])):
        if bot.solved:
            user_history[user_id] = Bot()

            return jsonify({
                "messages": [{
                  "attachment": {
                    "type": "template",
                    "payload": {
                      "template_type": "button",
                      "text": "훗 저 대단하죠? 다시 시작하시려면 [게임 시작하기]를 눌러주세요!",
                      "buttons": [
                        {
                          "type": "show_block",
                          "block_names": ["start"],
                          "title": "게임 시작하기"
                        }
                      ]
                    }
                  }
                }]
            })

        user_history[user_id] = Bot()
        return jsonify({
            "messages": [{
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "button",
                        "text": "뭔가가 잘못되었어요. 본인의 답변이 틀린지 확인하신 후 다시 시작해보세요.",
                        "buttons": [
                            {
                                "type": "show_block",
                                "block_names": ["start"],
                                "title": "게임 시작하기"
                            }
                        ]
                    }
                }
            }]
        })

    user_history[user_id] = bot

    return message_to_json(bot.get_next_question())


if __name__ == '__main__':
    app.run(port=8000)

