# 构建环境
docker build -t myflask-env:v2.4 .


# 运行开发环境
docker run -itd -v  /Users/zhaoyun/python/code/myflask:/myflask -p 5004:5000 --name myflask-env2.4 myflask-env:v2.4

docker run -itd -v /Users/zhaoyun/python/code/myflask:/myflask --net=host --name myflask-env2.4 myflask-env:v2.4
`