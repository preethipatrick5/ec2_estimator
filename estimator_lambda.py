import random


def lambda_handler(event, context):
    number_of_shots = int(event['number_of_shots'])
    reporting_rate = int(event['reporting_rate'])
    in_circle_count = 0
    response = {}
    for i in range(0, number_of_shots):
        dart_x = random.uniform(-1, 1)
        dart_y = random.uniform(-1, 1)
        if (dart_x * dart_x + dart_y * dart_y) < 1:
            in_circle_count += 1
        if i % reporting_rate == 0 and i > 0:
            response[i] = in_circle_count
    return {
        'statusCode': 200,
        'body': response
    }
