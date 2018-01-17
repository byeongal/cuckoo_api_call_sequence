import os, pickle
import simplejson

def get_api_call_sequence( json_path ) :
    ret = []
    with open(json_path, 'r') as f :
        json_data = simplejson.loads(f.read())
        if 'behavior' in json_data :
            behavior = json_data['behavior']
            if 'processes' in behavior :
                processes = behavior['processes']
                for each_process in processes :
                    calls = each_process.get('calls', [])
                    for each_call in calls :
                        ret.append( each_call['api'] )
    return ret

def run( json_dir_path ) :
    for path, dir, files in os.walk(json_dir_path) :
        for file in files :
            name, ext = os.path.splitext(file)
            if ext == '.json' :
                save_file = name + '.pickle'
                with open(os.path.join(path, save_file), 'wb')  as f :
                    pickle.dump(get_api_call_sequence(os.path.join(path, file)), f)

if __name__ == '__main__' :
    run('C:/reports')