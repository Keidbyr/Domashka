from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Главная")

@app.route("/promotion")
def promotion():
    return render_template("promotion.html",title='promotion')

@app.route("/image_mars.html")
def image_mars():
    return render_template("image_mars.html",title='image_mars')
@app.route('/form', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('form.html', title='Регистрация')
    elif request.method == 'POST':
        select['surname'] = request.form['surname']
        select['name'] = request.form['name']
        select['email'] = request.form['email']
        select['education'] = request.form['education']
        select['prof1'] = request.form['prof1']
        select['prof2'] = request.form['prof2']
        select['prof3'] = request.form['prof2']
        select['sex'] = request.form['sex']
        select['about'] = request.form['about']
        select['accept'] = request.form['accept']
        return render_template('form.html', data=select, title="Успешно")



def main():
    app.run(port=5005)


if __name__ == '__main__':
    main()
