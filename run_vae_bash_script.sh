#!/usr/bin/env bash

_now=$(date +"%m_%d_%Y_%T")
out_file_name="local_outs/vae_$_now.out"

python run_vae_py_script.py > $out_file_name 2>&1