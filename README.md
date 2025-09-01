
# Minimal reproducible example

'python main.py' leads to two different outputs depending on the machine used

- outputs on the local machine:

        15 equations with complexity: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
        
        with loss list=[6.198518  4.32883   3.8636668 3.750623  3.39009   3.289885  3.241478, 3.1636322 3.1257544 3.0748663 3.0191448 2.8005235 2.7345803 2.6894233 2.631853 ]


- outputs on the remote cluster
    
        15 equations with complexity: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
        
        with loss list=[6.198518  4.3288293 3.7714171 3.1500976 2.8432245 2.7298524 2.5652432 2.5203614 2.379923  2.3448064 2.262234  2.1551318 2.1292088 2.122846 2.1172836]

Notes: 

- Environments seem the same on the two machines:
  - same output for 'pip freeze' in the python virtual environment (which matches requirements.txt)
  - same content for the Manifest.toml file in the venv/julia_env folder
- Both outputs remain the same (the code is deterministic) if I re-run this script on the machines. 
- Running 'JULIA_NUM_THREADS=1 python main.py' does not change the outputs