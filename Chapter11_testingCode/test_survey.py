"""
Program Name: A Class to Test (Survey)
Description:
    This program is focused on testing the Class in 'survey.py'.
Name: Michael Taufa
Date: 2025-04-22
"""

from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""

    # NOTE: When building a test, think of building a mini program to test
    # the function/ method by intializing variables, passing arguments, 
    # and then 'assert' conclusion as a conditional to check if TRUE.

    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_responses('English')
    assert 'English' in language_survey.responses


def test_store_three_response():
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']

    # NOTE: Store values in list into "store_responses"

    for response in responses:
        language_survey.store_responses(response)

    # NOTE: For response in responses, check if values is in list

    for response in responses:
        assert response in language_survey.responses
