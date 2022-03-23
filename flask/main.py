from flask import Flask, render_template, request
import os, shutil, random
from VITON_HD import test
from upload_cloth_segmention import seg
from mysql import mysql

UPLOAD_DIR = 'D:/CP2/CP-VTON-HD_with_Recommendation_System/flask/static/upload_image'

app = Flask(__name__)
app.config['UPLOAD_DIR'] = UPLOAD_DIR


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/fileUpload', methods=['GET', 'POST'])
def cp_vton():
    image = request.files['file']
    image_name = image.filename
    random_image_number = random.randint(0, 99999)
    path = os.path.join(app.config['UPLOAD_DIR'], image_name).replace("\\", '/')
    image.save(path)
    new_path = os.path.join(app.config['UPLOAD_DIR'], f'{random_image_number}.jpg').replace("\\", '/')
    image_rename = shutil.move(path, new_path)
    for i in range(len(image_rename)-1, 0, -1):
        if image_rename[i] == '/':
            image_name = image_rename[i+1:]
            break
    seg(image_name)  # input_image segmention 함수

    model_list = ['00891_00.jpg', '03615_00.jpg', '07445_00.jpg', '07573_00.jpg', '08909_00.jpg', '10549_00.jpg']
    number = random.randint(0, len(model_list)-1)
    model = model_list[number]

    txt_file = open('D:/CP2/CP-VTON-HD_with_Recommendation_System/flask/VITON_HD/datasets/test_pairs.txt', 'w')
    txt_file.write(f'{model} {image_name}')
    txt_file.close()

    test.main()  # CP-VTON-HD 실행 함수
    return render_template('view.html', image_file='convert/'+image_name)


@app.route('/end', methods=['GET', 'POST'])
def db():
    rating = request.form['만족도']
    mysql(rating)
    return render_template('end.html')


if __name__ == "__main__":
    app.run(debug=True)