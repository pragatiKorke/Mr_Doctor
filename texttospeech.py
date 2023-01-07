import azure.cognitiveservices.speech as speechsdk
import mysql.connector

cnx = mysql.connector.connect(user="Vedant", password="Nogja@2004", host="mysql1249.mysql.database.azure.com", port=3306, database="doctor", ssl_ca="DigiCertGlobalRootCA.crt.pem", ssl_disabled=False)


#cnx = mysql.connector.connect(user="ltrsoft", password="Amol@2019", host="ltrdbserver.mysql.database.azure.com", port=3306, database="question", ssl_ca="DigiCertGlobalRootCA.crt.pem", ssl_disabled=False)
print(cnx)
# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
#speech_key, service_region = "08118a610f8d40cf844e9f0e3d252fbe", "centralindia"
speech_key, service_region = "14c6534add1b4f45bf844624212fa03f", "centralindia"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"

# Creates a speech synthesizer using the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# Receives a text from console input.
print("Type some text that you want to speak...")
#text = input()
mycursor = cnx.cursor()
#sql = "INSERT INTO voice (id,name) VALUES (%s, %s)"
#val = ("1", text)
#mycursor.execute(sql, val)

#cnx.commit()

#print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM medicine")

myresult = mycursor.fetchall()

for x in range(0,len(myresult)):
# Synthesizes the received text to speech.
# The synthesized speech is expected to be heard on the speaker with this line executed.
    result = speech_synthesizer.speak_text_async(str(myresult[x])).get()

# Checks result.
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
      print("Speech synthesized to speaker for text [{}]".format(str(myresult[x])))
    elif result.reason == speechsdk.ResultReason.Canceled:
      cancellation_details = result.cancellation_details
      print("Speech synthesis canceled: {}".format(cancellation_details.reason))
      if cancellation_details.reason == speechsdk.CancellationReason.Error:
          if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
      print("Did you update the subscription info?")
# </code>