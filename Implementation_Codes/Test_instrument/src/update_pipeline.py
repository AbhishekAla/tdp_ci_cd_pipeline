# Gilead TDP Pipeline update script
# Initial version V.0.0.1 on 19-SEP-2025
# Function 
# 1. [str,str,str] update_pipeline: args-> pipeline_json_file: str, taskscript_file: str

from typing import Tuple

# Add the parent path to sys.path so that parent folders are discoverable
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

pipeline_data = ""
pipeline_folder = "Implementation_Codes/Test_instrument/config"
source_folder = "Implementation_Codes/Test_instrument/src"
pipeline_output_file = "pipeline_out.json"

def update_pipeline(pipeline_json_file: str, taskscript_file: str) -> Tuple[str, str, str]:
    try:
        import json
        taskscript_name = taskscript_file.split('-')[1].split('.')[0]
        path_of_pipeline_file = pipeline_folder + "/" + pipeline_json_file
        path_of_taskscript_file = source_folder + "/" + taskscript_file
        taskscript = ""

        pipeline_id = ""
        pipeline_name = ""
        pipeline_json_string = ""

        with open(path_of_taskscript_file, 'r', encoding='utf-8') as task_file:
            taskscript = task_file.read()

        with open(path_of_pipeline_file, 'r') as p_file:
            pipeline_data = json.load(p_file)
            print(f"Pipeline json is loaded successfully")

            #Fetching pipeline ID
            if 'id' in pipeline_data:
                pipeline_id = pipeline_data['id']

            #Fetching pipeline Name
            if 'name' in pipeline_data:
                pipeline_name = pipeline_data['name']
            
            print("")

            if  taskscript_name in pipeline_data['pipelineConfig']:
                print (f"Taskscript {taskscript_name} already exist: going to update it..")
                pipeline_data['pipelineConfig'][taskscript_name] = taskscript
            else:
                print (f"Taskscript {taskscript_name} is new: going to add it..")
                pipeline_data['pipelineConfig'][taskscript_name] = taskscript
        
        pipeline_json_string = str(pipeline_data)
        
        #Creating pipeline output json file
        path_of_pipeline_output_file = pipeline_folder + "/" + pipeline_output_file
        print(f"Creating output file at {path_of_pipeline_output_file}")
        with open(path_of_pipeline_output_file, 'w') as output_json_file:
            json.dump(pipeline_data, output_json_file, indent=2)

    except Exception as ex:
        print(f"Exception occurred: {str(ex)}")
    finally:
        pass

    return pipeline_id, pipeline_name, pipeline_json_string


if __name__ == '__main__':
    p_id, p_name, p_json_data = update_pipeline('pipeline_test1.json', \
                                                'pipeline_test1-script_step2.py')
    print(f"New pipeline config: ID={p_id}, Name={p_name}, \
          Json_Configuration={p_json_data}")
    #p_id, p_name, p_json_data = update_pipeline('pipeline_test1.json', \
    #                                            'pipeline_test1-script_step3.py')
    #print(f"New pipeline config: ID={p_id}, Name={p_name},\
    #       Json_Configuration={p_json_data}")
