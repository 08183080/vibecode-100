import hashlib

class Block:
    def __init__(self, data, prev_hash):
        self.data = data
        self.prev_hash = prev_hash # 重点：存着上一个人的指纹
        self.self_hash = self.calculate_hash()

    def calculate_hash(self):
        # 把数据和上一个人的指纹揉在一起，算出自己的指纹
        content = str(self.data) + str(self.prev_hash)
        return hashlib.sha256(content.encode()).hexdigest()

# 模拟链条
b1 = Block("转账100元", "0") # 创始块
b2 = Block("转账50元", b1.self_hash) # 链接到 b1
b3 = Block("转账10元", b2.self_hash) # 链接到 b2

print(f"区块2存的指纹: {b2.self_hash}")
print(f"区块3认的指纹: {b3.prev_hash}")