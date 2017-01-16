$ cd /path/to/myapp

$ zappashell

$ yum install python27-devel python27-pip gcc

$ yum install libjpeg-devel zlib-devel

$ pip install -r ./requirements.txt --no-cache-dir

$ zappa deploy dev_brand_video

$ zappa invoke dev_brand_video 'app.lambda_handler'

$ zappa tail dev_brand_video