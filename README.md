pearhash
========

Simple [Pearson hashing](http://en.wikipedia.org/wiki/Pearson_hashing) algorithm. Python 3 only.


Instalation
-----------

```
pip install git+https://github.com/ze-phyr-us/pearhash.git
```


Usage
-----

```
>>> from pearhash import PearsonHasher
>>> hasher = PearsonHasher(2) # Set desired hash length in bytes.
>>> hasher.hash(b'ni hao')
bytearray(b'\xb76')
>>> hasher.hash(b'ni hao').hexdigest()
'b736'
```

Hash length can be changed easily:

```
>>> hasher = PearsonHasher(4)
>>> hasher.hash(b'ni hao').hexdigest()
'b73672e9'
```

And you can even change the seed used to generate the pseudorandom table:

```
>>> hasher = PearsonHasher(2, seed = 'whatevs')
>>> hasher.hash(b'ni hao').hexdigest()
'ae0d'
```
