# 概要

サブネットを計算して対象のセグメントを出力します。

# 使用例

python3系です。

### windows

```sh
> python --version
Python 3.7.2
```

* 24bit

```python
> python .\create_subnet.py 192.168.0.12/24
192.168.0.0 255.255.255.0 Network Address
192.168.0.1 255.255.255.0 Usable host
…
192.168.0.253 255.255.255.0 Usable host
192.168.0.254 255.255.255.0 Usable host
192.168.0.255 255.255.255.0 Broadcast Address
```

* 28bit

```python
>  python .\create_subnet.py 192.168.0.100/28
192.168.0.96 255.255.255.240 Network Address
192.168.0.97 255.255.255.240 Usable host
…
192.168.0.111 255.255.255.240 Broadcast Address
```

* 30bit

```python
> python .\create_subnet.py 192.168.0.222/31
192.168.0.222 255.255.255.254 Network Address
192.168.0.223 255.255.255.254 Broadcast Address
```