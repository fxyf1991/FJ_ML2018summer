#!/bin/bash
#!/home/lt/FJ_ML2018summer/venv
#echo $1
chmod +x Q2.py
#echo "path=$1" >> Q2.py
sed -i 1ipath=\'$1\' Q2.py
python Q2.py
