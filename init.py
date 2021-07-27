import logging
import flask
from flask import request
from utils import *
from constants import *
import boto3

logging.basicConfig(filename="data_log.log", format='%(asctime)s %(message)s' ,level=logging.DEBUG)
app = flask.Flask(__name__)


@app.route("/EC2/schedule/create", methods=['POST'])
def create_ec2_schedule():
    '''Create a new schedule of a EC2 instance, 
    input: {instance_id, schedule_config}'''
    
    if not validate_ec2_schedule_request_data(request.json):
        logging.debug("Create new EC2 schedule requested, Invalid data recieved")
        return 'Invalid data recieved', 400
    
    schedule_request_data = request.json
    logging.info("New EC2 schedule requested:%s",schedule_request_data)

    

    
@app.route("/EC2/schedule/update", methods=['PUT'])
def update_ec2_schedule():
    pass

@app.route("/EC2/schedule/delete", methods=['DELETE'])
def delete_ec2_schedule():
    pass

@app.route("/EC2/schedule/get_schedule", methods=['GET'])
def get_ec2_schedule_details():
    pass

@app.route("/EC2/all_scheduled", methods=['GET'])
def all_scheduled_instances():    
    client = boto3.client('ec2',region_name= AWS_REGION, aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

    scheduled_instances = {'Name': 'tag:scheduled','Values': ["True"]}
    response = client.describe_instances(Filters=[scheduled_instances])
    scheduled_instance_list = []
    for reservation in response.get("Reservations",[]):
        for instance in reservation.get("Instances",[]):
            scheduled_instance_list.append(instance["InstanceId"])

    return {"scheduled_instances":scheduled_instance_list}

if __name__ == '__main__':
    app.run(host='localhost', port=8000)