import subprocess

res_2 = subprocess.call(['/home/zhenyue/.conda/envs/vae/bin/python', 'demo.py',
                         '--dataset', 'mnist',
                         '--network-structure', 'Infogan',
                         '--exp-name', 'init_exp',
                         '--gpu', '0',
                         '--epochs', '400',
                         '--epochs2', '800'])
