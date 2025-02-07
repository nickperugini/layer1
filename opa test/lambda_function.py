import json
from opa_wasm import OPAPolicy

# Lambda handler function
def lambda_handler(event, context):
    try:
        policy = OPAPolicy('policy.wasm')
        data_file = open('data.json')
        data = json.load(data_file)
        
        # Optional: Set policy data
        policy.set_data(data)
        
        # load the input
        input_file = open('input_object.json')
        input = json.load(input_file)
        
        # Evaluate the policy
        result = policy.evaluate(input)
        print(result)
        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }

    except Exception as e:
        # Handle any errors and return an error response
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
