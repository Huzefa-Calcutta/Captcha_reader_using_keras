# Captcha_reader_using_keras

This project for captcha reading or recognition.

We use graph model in keras to build a convoluted neural structure for recognising the captcha. 

By calling the api with json request containg the captcha image, the framework will break down the captcha into individual letters and then predict what the letter is actually there.

Since graph model is no longer available in update Keras version we have to juse Kera 1.0.0
