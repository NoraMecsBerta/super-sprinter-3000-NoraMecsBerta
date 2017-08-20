from flask import Flask, render_template, redirect, session, request
import csv

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_index():
    list_of_the_all = []
    with open('supersprinter.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            from_csv = (','.join(row))
            list_csv = from_csv.split(',')
            list_of_the_all.append(list_csv)
    return render_template('list.html', list_of_the_all=list_of_the_all)


@app.route('/story')
def route_story():
    #note_text = None
    #if 'note' in session:
        #note_text = session['note'] 
    return render_template('story.html') #, note=note_text)


@app.route('/save-note', methods=["POST"])
def route_save():
    if request.method == 'POST':
        list_of_the_all = []
        with open('supersprinter.csv', 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                from_csv = (','.join(row))
                list_csv = from_csv.split(',')
                list_of_the_all.append(list_csv)
                iterator = len(list_of_the_all)
        story_title = request.form['story_title']
        user_story = request.form['user_story']
        acceptance_criteria = request.form['acceptance_criteria']
        business_value = request.form['business_value']
        estimation = request.form['estimation']
        status = request.form['status']
        id_ = str(iterator)
        list_to_append = [id_, story_title, user_story, acceptance_criteria, business_value, estimation, status]
        list_of_the_all.append(list_to_append)
        with open('supersprinter.csv', 'w') as csvfile:
            for list_ in list_of_the_all:
                spamwriter = csv.writer(csvfile, delimiter=',')
                spamwriter.writerow(list_)
    return redirect('/list')


@app.route('/delete-note', methods=["GET", "POST"])
def delete_note():
    list_of_the_all = []
    iterator = 0
    iterator_of_list_number = -1
    with open('supersprinter.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            from_csv = (','.join(row))
            list_csv = from_csv.split(',')
            list_of_the_all.append(list_csv)
    for list_ in list_of_the_all:
        iterator_of_list_number += 1
        if list_[0] == request.form["item-to-delete"]:
            del list_of_the_all[iterator_of_list_number]
    for list_ in list_of_the_all:
        list_[0] = str(iterator)
        iterator += 1
    list_of_the_all[0][0] = 'ID'
    with open('supersprinter.csv', 'w') as csvfile:
        for list_ in list_of_the_all:
            spamwriter = csv.writer(csvfile, delimiter=',')
            spamwriter.writerow(list_)
    return redirect('/list')

@app.route('/story2/<int:id_>', methods=["GET", "POST"])
def route_edit(id_):
    list_of_the_all = []
    iterator_of_list_number = 0
    with open('supersprinter.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            from_csv = (','.join(row))
            list_csv = from_csv.split(',')
            list_of_the_all.append(list_csv)
        for list_ in list_of_the_all[1:]:
            iterator_of_list_number += 1
            print(list_[0])
            if int(list_[0]) == int(id_):
                list_to_edit = list_of_the_all[iterator_of_list_number]
                print(list_to_edit)
                break
    return render_template('story2.html', id_=id_, list_to_edit = list_to_edit)


@app.route("/save-edit/<int:id_>", methods=["POST"])
def route_save_edit(id_):
    if request.method == 'POST':
        list_of_the_all = []
        print(id_)
        with open('supersprinter.csv', 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                from_csv = (','.join(row))
                list_csv = from_csv.split(',')
                list_of_the_all.append(list_csv)
        story_title = request.form['story_title']
        user_story = request.form['user_story']
        acceptance_criteria = request.form['acceptance_criteria']
        business_value = request.form['business_value']
        estimation = request.form['estimation']
        status = request.form['status']
        edited_list = [id_, story_title, user_story, acceptance_criteria, business_value, estimation, status]
        for i, list_ in enumerate(list_of_the_all[1:]):
            if int(list_[0]) == int(id_):
                list_of_the_all[i+1] = edited_list
        with open('supersprinter.csv', 'w') as csvfile:
            for list_ in list_of_the_all:
                spamwriter = csv.writer(csvfile, delimiter=',')
                spamwriter.writerow(list_)
    return redirect('/list')


if __name__ == '__main__':
    app.secret_key = 'secret_key_change_this_place'
    app.run(debug = True, port = 5000)