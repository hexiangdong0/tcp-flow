# tcp-flow
创建一个TCP连接

iperf不会建立多条子流，使用该仓库就可以建立多个子流
某次实验时发现iperf会创建两个MPTCP连接，于是使用该脚本

## 使用说明
数据的流动方向为sender->receiver，所以测试拥塞控制算法也是在sender上
```
# 先启动发送端
python3 tcp_sender.py

# 再启动接受端
python3 tcp_receiver.py [发送端的IP地址]
```

## 注意
未测试多个进程同时使用时的正确性
