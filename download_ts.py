import argparse
import subprocess
import random
import string
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url')
parser.add_argument('-o', '--out_dir')
parser.add_argument('--m3u8')
args = parser.parse_args()


iid = ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(12))
print(f'[FILEID] {iid}')
cmd = 'youtube-dl ' + args.url + ' -o "' + args.out_dir + '/' + iid + '.%(ext)s"'
#subprocess.check_output(cmd, shell=True)
subprocess.check_call(cmd, stdout=sys.stdout, stderr=subprocess.STDOUT, shell=True)

#TODO: make a uniform preview.mp4
if not args.m3u8:
	exit()

import os
from glob import glob

ext = glob(f'{args.out_dir}/{iid}*')[0].split('.')[-1]
os.makedirs(f'{args.out_dir}/{iid}', exist_ok=True)

#ffmpeg -i fLkgKfvqhUiZ.mp4 -hls_time 3 -hls_list_size 0 -hls_segment_filename "fLkgKfvqhUiZ/%04d.ts" -hls_base_url fLkgKfvqhUiZ/ -strict -2 output.m3u8
cmd = f'ffmpeg -i {args.out_dir}/{iid}.{ext} -hls_time 3 -hls_list_size 0 -hls_segment_filename "{args.out_dir}/{iid}/%04d.ts" -hls_base_url "{iid}/" -strict -2 {args.out_dir}/{iid}.m3u8'
subprocess.check_call(cmd, stdout=sys.stdout, stderr=subprocess.STDOUT, shell=True)
cmd = f'rm {args.out_dir}/{iid}.{ext}'
subprocess.check_call(cmd, stdout=sys.stdout, stderr=subprocess.STDOUT, shell=True)
cmd = f'touch {args.out_dir}/{iid}/completed'
subprocess.check_call(cmd, stdout=sys.stdout, stderr=subprocess.STDOUT, shell=True)

print('stdout: Done!')
