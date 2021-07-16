from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/test'
 
db= SQLAlchemy(app)

class student(db.Model):
   ID = db.Column(db.Integer, primary_key = True)
   Name = db.Column(db.String(100))

   def __init__(self,id, name,marks):
	   self.id = id
	   self.name = name
	   self.marks=marks

@app.route("/student", methods=["GET"])
def get_students():
	result = db.engine.execute("select * from student")
	response = []
	for row in result:
		response.append({
			"Id": row["id"],
			"Name": row["name"],
			"Marks": row["marks"]
			})
	response = {"student": response}
	return response

@app.route("/student", methods=["POST"])
def create_person():
	print(request.json)
	student = Student(request.json["id"], request.json["name"],request.json["marks"])
	db.session.add(student)
	db.session.commit()
	return {"status": "sucess"}

if __name__ == "__main__":
	app.run(host="localhost", port="10000")