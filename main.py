from flask import Flask, render_template, request

app = Flask(__name__)

def walkingOne30Min(daysOfService):
  if daysOfService < 6:
    return 20
  else:
    return 18
  
def walkingOne1Hr(daysOfService):
  if daysOfService < 6: 
    return 30
  else:
    return 28

def walkingTwo(daysOfService):
  if daysOfService < 4: 
    return 38
  elif daysOfService < 6:
    return 36
  else:
    return 34

def walkingThree(daysOfService):
  if daysOfService < 4: 
    return 42
  elif daysOfService < 6:
    return 40
  else:
    return 38

def sitting30Min(daysOfService):
  if daysOfService < 6:
    return 20
  else:
    return 18

def sitting1Hr(daysOfService):
  if daysOfService < 6:
    return 30
  else:
    return 28

def calculateCost(service, dogsOnWalk, times, daysOfService):  
  dogsOnWalk = int(dogsOnWalk)
  times = float(times)
  daysOfService = int(daysOfService)
  
  if service == "walking":
    if dogsOnWalk == 1 and times == 0.5:
      return walkingOne30Min(daysOfService) * daysOfService
    elif dogsOnWalk == 1 and times == 1:
      return walkingOne1Hr(daysOfService) * daysOfService
    elif dogsOnWalk == 2:
      return walkingTwo(daysOfService) * daysOfService
    elif dogsOnWalk == 3:
      return walkingThree(daysOfService) * daysOfService
  else:
    if times == 0.5:
      return sitting30Min(daysOfService) * daysOfService
    else:
      return sitting1Hr(daysOfService) * daysOfService
  

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/checkout')
def about():
  return render_template('checkout.html')

@app.route('/purchase-data', methods=['POST'])
def purchaseData():
  if request.get_json:
    # get content
    content = request.json
    # print cost
    print("cost is: " + str(calculateCost(
    content["service-select"], 
    content["dogs-on-walk"], 
    content["times"], 
    content["days-of-service"])))
    return {'status': '200'}
  else:
    return {'status': '500'}
if __name__ == '__main__':
  app.run(debug=True)


