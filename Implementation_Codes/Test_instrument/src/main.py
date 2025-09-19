def process_file(input: dict, context: object):
  	"""
    Logic:
    1. Get input file length
    2. Get offset from pipeline config
    3. Write a text file to Data Lake

    Args:
        input (dict): input dict passed from master script
        context (object): context object

    Returns:
        None
    """
    print("Starting task")
    
    input_data = context.read_file(input["inputFile"])
    length = len(input_data["body"])
    offset = int(input["offset"])                      
    context.write_file(                                
        content=f"length + offset is {length + offset}",
        file_name="len.txt",
        file_category="PROCESSED"
    )
    
    print("Task completed")
