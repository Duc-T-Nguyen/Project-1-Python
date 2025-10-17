from datetime import datetime
import sys
file_name= sys.argv[1] if len(sys.argv) > 1 else "logs.txt"
cmd = sys.stdin.readline().strip()
msg = sys.stdin.readline().strip()
cur_time = datetime.now()
with open(f'{file_name}', 'a') as log_file:
    log_file.write(f'{cur_time.strftime("%Y-%m-%d %H:%M")} [{cmd}] {msg}\n')
sys.stdout.flush()



        

