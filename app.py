from flask import Flask,render_template,request#import flask library

#initialize flask
app=Flask(__name__)
#route your webpage
@app.route('/')
def visitors():

	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	# Increment the count
	visitors_count = visitors_count + 1

	# Overwrite the count
	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()

# Render HTML with count variable
	return render_template("index.html",count=visitors_count)
#route your webpage
@app.route('/',methods=['POST'])
def covid_stats():
	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()
	text=request.form['text']
	covid_data="https://covid-api-262.herokuapp.com/?country="+text
	print(covid_data)
	return render_template("index.html", image=covid_data, count=visitors_count)

	#complete the code
if __name__=='__main__':
	app.run()
#add code for executing flask