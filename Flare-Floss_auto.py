import subprocess
import json
import os
import sys

def main():
    if sys.argv[1] == '-h':
        print('Options:\n    -n   Path to floss.exe\n    -i   Path to folder with input files\n    -o   Output file name(optional)\n    -floss   Floss parameters(MUST BE AT THE END!!!)\n')
    else:
        outup_name = 'result'
        for arg in sys.argv:
            if arg == '-n':
                path_to_floss = sys.argv[sys.argv.index(arg)+1]
            elif arg == '-i':
                input_dir = sys.argv[sys.argv.index(arg)+1]
            elif arg == '-o':
                outup_name = sys.argv[sys.argv.index(arg)+1]
            elif arg == '-floss':
                params = ''
                for i in range(sys.argv.index(arg)+1,len(sys.argv)):
                    params += sys.argv[i]+' '
        files = os.listdir(input_dir)
        print(f'Files : {files}')
        print(f'Params: {params}')
        result = []
        for file in files:
            print(f'Processing No {files.index(file)+1}/{len(files)}')
            res = subprocess.check_output(f'floss.exe {params} {input_dir}\\{file}',cwd=path_to_floss,shell=True).decode('cp866').split('\n')
            res = [i.strip('\r') for i in res]
            res = [i for i in res if i != '']
            result.append({file:res})
        with open(f'{outup_name}.json','w') as file:
            json.dump(result, file, indent=4,ensure_ascii=False)

if __name__ == '__main__':
    main()