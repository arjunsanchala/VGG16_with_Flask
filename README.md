# VGG19 with Flask

This project is a complete mixture of transfer learning and web development. I have used here Tensorflow's VGG19 model and deploy it on web. The web app gives an option to upload an image and the model predicts what is in the image.

## Images:
<img src="https://user-images.githubusercontent.com/40913151/100567992-f9073780-331d-11eb-9c0d-6191390fd780.png" width="300"/> <img src=https://user-images.githubusercontent.com/40913151/100568185-96fb0200-331e-11eb-898f-8266d58b6006.png width="300"/><img src="https://user-images.githubusercontent.com/40913151/100567886-b9405000-331d-11eb-9e6f-41e00dd5a37c.png" width="300"/> 


# #Work flow:
First of all, we have to store the weights of the give VGG19 model. Subsequently, we have to make a flask structure. I have made two routes: Index and upload. The Index function calls the index.html file and and index.html file then extends base.html file (which will be useful when user hits the predict button). In addition, I have used here some available templets of CSS and JavaScript for UI of the app. There will be few machine learning steps while user hits the "predict" button. The ML steps include: preprocessing ofthe image, decode the prediction and return the predicted word.      




