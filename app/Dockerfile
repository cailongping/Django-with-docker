#拉取官方基础镜像
FROM python:3.8.3-alpine

#设置工作目录
WORKDIR /usr/src/app

#设置环境变量
#防止python将pyc文件写入光盘，等效于python -B选项
ENV PYTHONDONTWRITEBYTECODE 1

#防止python缓冲stdout和stderr
ENV PYTHONUNBUFFERED 1

#安装依赖
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

#复制项目(两点之间有空格)
COPY . .



