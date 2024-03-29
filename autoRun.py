import pynvml 
import time 
import subprocess

pynvml.nvmlInit()


def taskTrafficPrediction():
    cmd_list = []
    for ds in ['PeMS04','PeMS07','PeMS08']:
        for m in ['BGCN', 'GWNET']:
            cmd = 'python run_model.py --task traffic_state_pred --model %s --dataset %s' % (m,ds)
            cmd_list.append(cmd)
    return cmd_list

cmd = taskTrafficPrediction()

while cmd:
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    memoinfo = pynvml.nvmlDeviceGetMemoryInfo(handle)

    if memoinfo.used / 1e6 < 14 * 100: # 1.4GB
        print(memoinfo.used / 1e6)
        c = cmd.pop(0)
        subprocess.call(c, shell=True)
        time.sleep(15)
    else:
        time.sleep(300)



