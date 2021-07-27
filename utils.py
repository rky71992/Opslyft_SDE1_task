def validate_ec2_schedule_request_data(data):
    '''Check if the required keys are present in data'''
    if not data:
        return False
    if not data.get("instance_id"):
        return False
    if not data.get('schedule_config'):
        return False
    return True
    