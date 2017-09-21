#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
import speech_recognition as sr
import time

"""TODO: Set up offline speech recogniton
thorugh pocketsphynx"""
class STT:
    def __init__(self):
        # obtain audio from the microphone
        self.r = sr.Recognizer()
        # recognize speech using Google Cloud Speech
        # GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
        #   "type": "service_account",
        #   "project_id": "lucy-162104",
        #   "private_key_id": "28bac3d2375121f3e7beb6dda107938056541cb1",
        #   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDPml5PZYAY+TdG\nhF4o+85KeenNIOuCT7RJpgkXiKaVpVz9ZVbeZ1ErKDciJXtPQiQaWzO+9NTQSbvD\nV8TxgOW66QTuyCg5WVBZb/TbeUck/GJ6M1fzYN4wEI5vSES+bg5Tzrx98Dfah308\nRzaZvQTI9IzmuKri8AT7INo+5/zn+dzMd7YnFqAj6y+iDYeV39SgfcA2u7Zy8Yw4\nMML3TIlUG5zZM3utxERdZBxGpZAh89CS6dRMn8Rux8UgsGIslIPpQX1pGN/QG8P+\nzMtreZFy1yYV2K+PMoLYQGAjuva/Ethoa6f9uBl46X3DyPLjlxjYd5Nm4ft71iFE\necw/g9lNAgMBAAECggEAOXWVYs5KDR91MBxU320KZMynbHIPHQsocDX3UD8vND4H\npc7Vo0rfSV2hHN9Y6M/6pBzYDqM+/8NYp7F0Pg+aBgiWp+xYTb8toQN+tvwzN8Zv\nDzmEv0TxWkZK1fwfosFdT87plsXU/7P+cp+XOif52hDtqrI0AgnCpyspnL2i3yVm\nTvslPs3bw5lKuDwpf7MhybW8x2S8a8KNTn1mf+O+4CI09Y+aYZo+665RNqdxD9lq\n1EY58PEtXocEeK2mqe8cA2yb73fx0P07vxMxMK2dLKX6ch1mEScCSdQ5+kp17mPW\nN+fceaPAY6jvN9WA5SOJ3kk+mSsHmcWM200gCmnk4QKBgQDtZ9ySm7oC6o6uojP7\n8et/1BOHT8QZMFijrvlLB4Owr+44VAie5YZJs+VWWRTx4tT99MzHdvShV5ItwqJK\njO2kkJuIj1LrEHtEWF3wszu3YjsLtnRpqEXDUTL9M3H3rMn4xs6lH19qgL9NFtBb\nmNENje/ZiF8fvKpmdAMh60H8hQKBgQDf3PFzw8VaxcJP8s+SOBs00fQ6jTbCcQe9\nGElkeGzqe25lnDTXX7mIfK6syu+XEqvKTy1ngoL7A2OO4CKQ1X8+Q65rWCUW4BKU\nZGmEDVjheHsltEj2HLWSwzzsLrrjFkSTFbGOAP3AYRs0H2B7et2K5DGJw/SO0XzY\nAKkWTUlIKQKBgQDKwb2caOvAudsKQvXq436iOdpD4lg0uxm5EiNPdSd/q4HlEcAb\nFSRPphjkWkiNHZGTI5QRdwMPGN97vZMl4J7FwctUIjRLFlRw1pfEjw8dXAPZyQY7\nhr+uRJcrsNhRE32bvw+V7ulq6HJ5wFZLJITG8sY6H0I+tL9DqSlTur0skQKBgQC/\nLHCqGvKL7TxeiA4JYY6iUfYOlo/AB0TDkF0Exu7EY/pIHdjmYGISE+AbwgZPbmt0\njp9IuSTf9enslq4OH7TVWHk4RIMQAPT88q9FTRytF/WaolZ4jtXk6oQ5ckK5MUgI\nj8scaO5KfuL7ZRxA9xEAzpUbgFN2L6I82HuNhxzg2QKBgQCaR9wWMWx44A+RuHdW\nP/tfechTzVvmtKlZHxsQWqrsO3iCgeeuoTidJWGkoZ6YDqdB+3Qp1Lpztkpmsx0m\ng22Wptx00HlpoJSP+apR09XQf9+BSvfXxCTGjSJrymtZeXXMokjmomayCBYgkSKC\nGrjedBO8gVAf7u2M9eeRnl4Iog==\n-----END PRIVATE KEY-----\n",
        #   "client_email": "shashemipour@lucy-162104.iam.gserviceaccount.com",
        #   "client_id": "117387720082577780834",
        #   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        #   "token_uri": "https://accounts.google.com/o/oauth2/token",
        #   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        #   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/shashemipour%40lucy-162104.iam.gserviceaccount.com"
        # }
        # """

    def phrase_spoken(self):  # Waits for user speech returns speech text
        with sr.Microphone() as source:
            audio = self.r.listen(source)  # Listens to user
            try:
                word_said = self.r.recognize_google(audio)  # Turn audio into text
            except sr.UnknownValueError:
                return None
            except TypeError:
                return None
            return word_said  # Return the speech as text
