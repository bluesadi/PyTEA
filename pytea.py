class TEA:

    def __init__(self, key):
        assert isinstance(key,bytes)
        assert len(key) == 16
        self.key = key
        self.k0 = int.from_bytes(self.key[0:4], 'little')
        self.k1 = int.from_bytes(self.key[4:8], 'little')
        self.k2 = int.from_bytes(self.key[8:12], 'little')
        self.k3 = int.from_bytes(self.key[12:16], 'little')

    def encrypt(self, data):
        result = b''
        for i in range(0,len(data),8):
            v0 = int.from_bytes(data[i:i + 4], 'little')
            v1 = int.from_bytes(data[i + 4:i + 8], 'little')
            sum = 0
            delta = 0x9E3779B9
            for j in range(32):
                sum += delta
                v0 += ((v1 << 4) + self.k0) ^ (v1 + sum) ^ ((v1 >> 5) + self.k1)
                v0 &= 0xFFFFFFFF
                v1 += ((v0 << 4) + self.k2) ^ (v0 + sum)  ^ ((v0 >> 5) + self.k3)
                v1 &= 0xFFFFFFFF
                sum &= 0xFFFFFFFF
            result += v0.to_bytes(4,'little')
            result += v1.to_bytes(4,'little')
        return result

    def decrypt(self, data):
        result = b''
        for i in range(0,len(data),8):
            v0 = int.from_bytes(data[i:i + 4], 'little')
            v1 = int.from_bytes(data[i + 4:i + 8], 'little')
            delta = 0x9E3779B9
            sum = (delta << 5) & 0xFFFFFFFF
            for j in range(32):
                v1 -= ((v0 << 4) + self.k2) ^ (v0 + sum) ^ ((v0 >> 5) + self.k3)
                v1 &= 0xFFFFFFFF
                v0 -= ((v1 << 4) + self.k0) ^ (v1 + sum) ^ ((v1 >> 5) + self.k1)
                v0 &= 0xFFFFFFFF
                sum -= delta
            result += v0.to_bytes(4,'little')
            result += v1.to_bytes(4,'little')
        return result