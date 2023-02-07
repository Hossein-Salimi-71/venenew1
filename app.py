

from flask import Flask, render_template, request,send_from_directory,session
from keras_preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import matplotlib.image as mpimg

model=load_model("net4.h5")

PEOPLE_FOLDER ='static\people_photo'

app=Flask(__name__)
app.config['SECRET_KEY']='Supersecret'
#app.config['UPLOAD_FOLDER']='static/files'
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
app.config['UPLOADED_PHOTOS_DEST']='uploads'


@app.route('/',methods=['GET'])
@app.route('/home',methods=['GET'])
def home():
    full_filename3="static\people_photo\Logo.jpg"
    return render_template('home.html',user_image3 = full_filename3)

@app.route('/about',methods=['GET'])

def about():
    full_filename="static\people_photo\Picture1.jpg"
    full_filename1="static\people_photo\Picture2.jpg"
    full_filename2="static\people_photo\Picture3.jpg"
    full_filename3="static\people_photo\Logo.jpg"
    return render_template("about.html", user_image = full_filename, user_image1 = full_filename1,user_image2 = full_filename2, user_image3 = full_filename3)

@app.route('/news',methods=['GET'])
def news():
    full_filename3="static\people_photo\Logo.jpg"
    return render_template('news.html',user_image3 = full_filename3)

@app.route('/contact',methods=['GET'])
def contact():
    full_filename3="static\people_photo\Logo.jpg"
    full_filename4="static\people_photo\mail.jpg"
    return render_template('contact.html',user_image3 = full_filename3,user_image4 = full_filename4)

@app.route('/demo')
def index():
    full_filename3="static\people_photo\Logo.jpg"
    return render_template('demo.html',user_image3 = full_filename3)

@app.route('/demo',methods=("POST", "GET"))
def predict():
        full_filename3="static\people_photo\Logo.jpg"
        if request.method == 'POST':
            uploaded_img = request.files['photo']
            uploaded_img.save("hoss.jpg")
            session['uploaded_img_file_path'] = "hoss.jpg"
            img_file_path = session.get('uploaded_img_file_path', None)
            img_file_path1="hoss.jpg"
            image = mpimg.imread('hoss.jpg')
            image=img_to_array(image)
            image=np.average(image,axis=2)
            image=image.reshape(1, len(image), len(image[0]))
            yhat=model.predict([1])
            #yhat=model.predict(image)
        return render_template('demo.html',user_image3 = full_filename3,aa=img_file_path)
'''
            yhat = np.argmax(yhat, axis=1)+1
            print(yhat)
            if yhat==0:
                C1=0
                C2=1
            if yhat==1:
                C1=0
                C2=2
            if yhat==2:
                C1=2
                C2=5
            if yhat==3:
                C1=5
                C2=7.5
            if yhat==4:
                C1=7.5
                C2=10
            if yhat==5:
                C1=10
                C2=25
            if yhat==6:
                C1=25
                C2=50
            classification=yhat
        else:
            file_url=None
            classification=0
            C1=0
            C2=0
'''
        #return render_template('demo.html',user_image3 = full_filename3,aa=img_file_path)
'''

'''
        #return render_template('demo.html',user_image3 = full_filename3,file_url=img_file_path,Con1=C1, Con2=C2,)

        #return render_template('demo.html',form=form,file_url=file_url,prediction=classification,Con1=C1, Con2=C2,user_image3 = full_filename3)


if __name__=='__main__':
    app.run(debug = True)




















