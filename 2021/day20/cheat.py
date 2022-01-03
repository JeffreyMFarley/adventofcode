# https://topaz.github.io/paste/#XQAAAQBpAwAAAAAAAAA0mUhJsSKTvmdez3EzeTpEiVVJ4Jw44YpkAJakP2mENLW8r1N526n5XUSw1X7uxM2oDFkgdqk8oThIcrO6VHvUqhVCXudUOqtynk6pQm/Psfwmt4fk4eHxfO6Vi4a+vRoC78H05dPN6Y3E67ULmpaI2VBt7uUcirA/r73sMt4mdymH0CufE+jzpUZXwJqG5JrVNys3AqnJRiwhV2k/tQnATN9eGKmcOcQaN71xlJbDy/eChJwhf658WnHK7X3Kic8V1DO2VZOrq35/e3dO9xxGg0ZFznRl627LARhQQKAuSBv6T9yBQncHMcLIKLNn7RgHxEGv8Pyf+pkEz+U2Y/p6GqhTaJCM5H2kVWZmfPUjghvIP16tBdQG6eGbM2d52uxygqfEfaDOLhhQgLtY6poKo+eTzQBLu6NtxPsoIM1i6hNQ6WUk6xjJFFRtamzLjp7CPbGj1vqyqNSTx3/CtZihbwlTLpmaNrvtkcjawAUyHDht16KDk3/ALe8PLdaaCB4nmjGefRCAAHlgr0r9iBF9+I6IZEPMveNNfaAthwFj9hu27qj7JBzBvp2R4HffuEIb2wGMVcd1wSvlOpfFGDcnzwN8ZCV6dSACPKsqhat+dD374iq2

INPUT = 'input1.txt'

ieas = open(INPUT).readline().replace('\n','')
im = open(INPUT).read().split()[1:]

def countlightpixels(im):
    c = 0
    for s in im:
        c += s.count('#')
    return c

def tostring(im):
    return ''.join(s+'\n' for s in im)

def enhance(im,b): #im is image (less border). b is border symbol '.' or '#'
    bim = [b*(len(im[0])+4)]*2 + [b*2+s+b*2 for s in im] + [b*(len(im[0])+4)]*2
    im2 = []
    for y in range(1,len(bim)-1):
        im2 += ['']
        for x in range(1,len(bim)-1):
          s = bim[y-1][x-1:x+2] + bim[y][x-1:x+2] + bim[y+1][x-1:x+2]
          k = int(s.replace('.','0').replace('#','1'),2)
          im2[-1] += ieas[k] # look it up on the image enhancement string
    return im2

for i in range(50):
    im = enhance(im,'.') if i%2 == 0 else enhance(im,'#')

print('light pixels after 50 iters:',countlightpixels(im))
