import os
import azure.cognitiveservices.speech as speechsdk
import mysql.connector


#cnx = mysql.connector.connect(user="ltrsoft", password="Amol@2019", host="ltrdbserver.mysql.database.azure.com", port=3306, database="question", ssl_ca="DigiCertGlobalRootCA.crt.pem", ssl_disabled=False)
cnx = mysql.connector.connect(user="Vedant", password="Nogja@2004", host="mysql1249.mysql.database.azure.com", port=3306, database="doctor", ssl_ca="DigiCertGlobalRootCA.crt.pem", ssl_disabled=False)
print(cnx)
def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    print("Speak  Madicine  name")
    mname = speech_recognizer.recognize_once_async().get()
    print("Speak into your microphone.")
    print("Speak  Medicine company name")
    cname = speech_recognizer.recognize_once_async().get()
    print("Speak into your microphone.")
    print("Speak  Medicine Context")
    context = speech_recognizer.recognize_once_async().get()
    print("Speak into your microphone.")
    print("Speak  Medicine used for")
    used = speech_recognizer.recognize_once_async().get()
   # mycursor = cnx.cursor()
    mycursor = cnx.cursor()
    sql = "INSERT INTO medicine (id,mname,cname,context,usedfor) VALUES (%s,%s,%s,%s, %s)"
    val = ("2",mname.text,cname.text,context.text,used.text)
   # sql = "INSERT INTO voice (id,name,city) VALUES (%s, %s,%s)"
    #val = ("3", name_result.text,city_result.text)
    mycursor.execute(sql, val)

    cnx.commit()

    print(mycursor.rowcount, "record inserted.")

    if mname.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(mname.text))
    elif mname.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(mname.no_match_details))
    elif mname.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = mname.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

    if cname.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(cname.text))
    elif cname.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(cname.no_match_details))
    elif cname.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = cname.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

    if context.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(context.text))
    elif context.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(context.no_match_details))
    elif context.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = context.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")


    if used.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(used.text))
    elif used.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(used.no_match_details))
    elif used.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = used.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

recognize_from_microphone()