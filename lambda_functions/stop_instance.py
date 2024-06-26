import boto3

def lambda_handler(event, context):
    
    ec2 = boto3.resource('ec2')
    
    #CHECKING STOPPED INSTANCES
    for instance in ec2.instances.all():
        
        state = instance.state['Name']
        
        if state == 'running':
            
            #Stop instance
            try:
                
                instance.stop()
                
            except:
                
                print('Something went wrong!')
            
        
    
