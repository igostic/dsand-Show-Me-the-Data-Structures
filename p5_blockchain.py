import hashlib
from datetime import datetime


class Block:

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

    def __repr__(self):
        return 'I\'m block ' + str(self.index) + ', timestamp: ' + str(self.timestamp) + ', data: \"' + self.data + '\"'


def next_block(last_block):
    if last_block is None or type(last_block) is not Block:
        print("Invalid Last block")
        return
    this_index = last_block.index + 1
    this_timestamp = datetime.now()
    this_data = "I'm block {}".format(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


if __name__ == '__main__':
    chain = [Block(0, datetime.now(), "First Block", "0")]
    for i in range(0, 10):
        block = next_block(chain[-1])
        if block.data is not None and len(block.data) > 0:
            chain.append(block)
    if len(chain) != 0:
        [print(block) for block in chain]
    else:
        print('Block chain empty!')