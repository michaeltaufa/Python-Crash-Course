"""
Program Name: Language Survey
Description:
    This program is focused on creating a language survey while utilizing
    'survey.py' to import classes and conduct Pytest.
Name: Michael Taufa
Date: 2025-04-22
"""

from survey import AnonymousSurvey

video_game_question = "What is your favorite video game?"
video_game_Survey = AnonymousSurvey(video_game_question)

video_game_Survey.show_question()
print("Press and type 'q' to exit program.")

while True:
    user_response = input("Video Game: ")
    if user_response == 'q':
        break
    video_game_Survey.store_responses(user_response)


print("\nResults:")
video_game_Survey.show_results()
