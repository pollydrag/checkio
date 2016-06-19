# Solution for "The Hamming Distance"
# https://checkio.org/mission/hamming-distance2/

checkio = lambda n, m: bin(n ^ m).count('1')
