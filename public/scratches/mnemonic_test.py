from mnemonic import Mnemonic

mnemo = Mnemonic("english")
words = mnemo.generate(strength=256)
seed = mnemo.to_seed(words, passphrase="")
entropy = mnemo.to_entropy(words)

print(words)
