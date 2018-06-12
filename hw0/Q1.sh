#!/bin/bash
#!/home/lt/FJ_ML2018summer/venv/bin
#echo $1
chmod +x Q1.py
#echo "path=$1" >> Q1.py
sed -i 1ipath=\'$1\' Q1.py
python Q1.py
