from flask import Flask, render_template,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_socketio import SocketIO,emit, join_room, leave_room
from flask import session, redirect, url_for, render_template, request


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://gezstvxitlpjjp:9e209d4f9ea2528cd8d986f9032ac70aa6ff73715ba858bc5442fa9a0bb606d1@ec2-75-101-232-85.compute-1.amazonaws.com/djue0lbbc387d'
db = SQLAlchemy(app)
app.secret_key= "wafhoohhioohsdfa"
socketio = SocketIO(app)
class HELPDESK(db.Model):
    __tablename__="Helpdesk"
    id = db.Column(db.String,primary_key=True)
    name = db.Column(db.String)
    availability = db.Column(db.Integer)
    def __init__(self,id,name,availability):
        self.id = id
        self.name = name
        self.availability = availability



#client
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ignore/<id>')
def ignore(id):
    helpDesk = HELPDESK.query.get(id)
    print(helpDesk.name)
    room=helpDesk.availability
    helpDesk.availability=0
    db.session.commit()

    return redirect(url_for('server'))

@app.route('/chat/<NAME>/<ROOM>')
def chat(NAME,ROOM):
    session['name'] = NAME
    session['room'] = ROOM
    if session['name'] == '' or session['room'] == '':
        return redirect(url_for('index'))
    helpDesk = HELPDESK.query.filter_by(availability=0).all()
    if(HELPDESK.query.filter_by(availability=0).all()):
        for x in helpDesk:
          x.availability=ROOM 
          db.session.commit()
          break 
        return redirect(url_for('chatting'))

    else :
       flash("Sorry for the Inconvinience")    
       return redirect(url_for('index'))  
   
#server
@app.route('/server')
def server():
    HelpDesk = HELPDESK.query.all()
    return render_template('server.html',serv=HelpDesk)

@socketio.on('joined', namespace='/chat')
def joined(message):
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': 'Chat Active!'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    emit('message', {'msg': message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    leave_room(room)
    if(HELPDESK.query.filter_by(availability=room).first()) :
     helpDesk = HELPDESK.query.filter_by(availability=room).first()
     helpDesk.availability=0
     db.session.commit()
    emit('status', {'msg':'Terminated Chat'}, room=room)


@app.route('/serverchat/<NAME>/<ROOM>')
def serverchat(NAME,ROOM):
    session['name'] = NAME
    session['room'] = ROOM
    return redirect(url_for('schatting'))

@app.route('/chatting')
def chatting():
  name = session.get('name', '')
  room = session.get('room', '')
  if name == '' or room == '':
    return redirect(url_for('index'))
  return render_template('chat.html', name=name, room=room)


@app.route('/schatting')
def schatting():
  name = session.get('name', '')
  room = session.get('room', '')
  if name == '' or room == '':
    return redirect(url_for('index'))
  return render_template('serverchat.html', name=name, room=room)

if __name__ == '__main__':
    socketio.run(app,debug=True)
