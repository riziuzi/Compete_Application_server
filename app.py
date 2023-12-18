import datetime
from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from flask_cors import CORS  # Import the CORS extension
import os
import applications

app = Flask(__name__)
CORS(app)

uri = "mongodb+srv://riziuzi:GClDGPPK1AZwCcEP@riziuzicluster.ulcokkb.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.compete_database

@app.route("/api/tasks/<string:user_id>",  methods=['GET'])
def get_data(user_id):
    task_collection = db[f"{user_id}_collection"]
    data = list(task_collection.find())  # Convert cursor to a list of documents
    for task in data:
        task['_id'] = str(task['_id'])
    # print(user_id)
    return data

@app.route("/api/submit",  methods=['POST'])
def submit_task():
    try:
        data = request.json
        # print(data)
        usr_name = "rishiSIR"                                   # ??????????????????????????
        task_collection = db[f"{usr_name}_collection"]
        answer = applications.Summarize(data["message"])
        # print(answer)                       # Heavy time consumer!!!!!!!!!!!!
        # print(applications.QnA("Today, I spent 2 hours working on the project. I started by reviewing the project requirements and then moved on to creating a rough outline of the project. I also spent some time researching the best tools to use for the project. I ran into a few issues with the tools, but I was able to resolve them after some troubleshooting. Overall, I feel like I made good progress today and I’m looking forward to continuing to work on the project tomorrow."))
        if(answer["task"]==""):
            answer["task"] = "Unknown Task"
        task_document = {
            "task": answer["task"],
            "message": data["message"],
            "date": datetime.datetime.now(),
        }
        post_id = task_collection.insert_one(task_document).inserted_id
        
        
        
        response = {"message": "Data received successfully"}
        return jsonify(response), 200

    except Exception as e:
        # print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500
@app.route("/api/blogs/", methods=["GET"])
def get_blogs():
    return [{"blog" : "Ye le nikaal photu |( ^  ^ )|"}]


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)



















# task_no = 1
# message = "Hello tha dhaba"

# usr_name = "rishiSIR"
# task_collection = db[f"{usr_name}_collection"]

# task_document = {
#     "task_no.": task_no,
#     "message": message,
#     "date": datetime.datetime.now(),
# }

# post_id = task_collection.insert_one(task_document).inserted_id
# post_id = task_collection.find()
# for i in post_id:
#     print(i)