#!/usr/bin/env python

"""Google Cloud Text-To-Speech API sample application .

Example usage:
    python synthesize_text.py --text "hello"
    python synthesize_text.py --ssml "<speak>Hello there.</speak>"
"""

from google.cloud import texttospeech
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--text',
                       help='The text from which to synthesize speech.')
    group.add_argument('--ssml',
                       help='The ssml string from which to synthesize speech.')

    args = parser.parse_args()

    client = texttospeech.TextToSpeechClient()
    response = None

    if args.text:
        """Synthesizes speech from the input string of text."""
        input_text = texttospeech.types.SynthesisInput(text=text)

        # Note: the voice can also be specified by name.
        # Names of voices can be retrieved with client.list_voices().
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        response = client.synthesize_speech(input_text, voice, audio_config)
    else:
        """Synthesizes speech from the input string of ssml.

        Note: ssml must be well-formed according to:
            https://www.w3.org/TR/speech-synthesis/

        Example: <speak>Hello there.</speak>
        """
        input_text = texttospeech.types.SynthesisInput(ssml=ssml)

        # Note: the voice can also be specified by name.
        # Names of voices can be retrieved with client.list_voices().
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        response = client.synthesize_speech(input_text, voice, audio_config)

    if response is not None:
        # The response's audio_content is binary.
        with open('output.mp3', 'wb') as out:
            out.write(response.audio_content)
            print('Audio content written to file "output.mp3"')
