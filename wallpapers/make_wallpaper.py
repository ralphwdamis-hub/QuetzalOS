import struct, zlib, math, os

def png_chunk(chunk_type, data):
    c = chunk_type + data
    return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)

width, height = 1920, 1080
cx, cy = width//2, height//2
pixels = []

print('Generation en cours...')

for y in range(height):
    row = [0]
    for x in range(width):
        dx, dy = x-cx, y-cy
        dist = math.sqrt(dx*dx + dy*dy)
        angle = math.atan2(dy, dx)
        r, g, b = 10, 7, 5
        ray = abs(math.sin(angle * 20))
        if dist < 480:
            intensity = ray * 0.15 * (1 - dist/480)
            r = int(r + intensity * 26)
            g = int(g + intensity * 74)
            b = int(b + intensity * 46)
        for radius, thickness, cr, cg, cb in [(480,4,201,162,39),(320,3,61,186,118),(160,2,201,162,39),(80,3,240,192,64),(30,30,201,162,39)]:
            if abs(dist - radius) < thickness:
                blend = 1 - abs(dist - radius) / thickness
                r = int(r*(1-blend) + cr*blend)
                g = int(g*(1-blend) + cg*blend)
                b = int(b*(1-blend) + cb*blend)
        if abs(dx) < 2 and dist < 480:
            r, g, b = 201, 162, 39
        if abs(dy) < 2 and dist < 480:
            r, g, b = 201, 162, 39
        if abs(abs(dx) - abs(dy)) < 2 and dist < 480:
            r, g, b = 26, 74, 46
        row += [min(255,r), min(255,g), min(255,b)]
    pixels.append(bytes(row))

signature = b'\x89PNG\r\n\x1a\n'
ihdr = png_chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0))
idat = png_chunk(b'IDAT', zlib.compress(b''.join(pixels), 1))
iend = png_chunk(b'IEND', b'')

home = os.path.expanduser('~')
with open(home + '/QuetzalOS/wallpapers/sunstone.png', 'wb') as f:
    f.write(signature + ihdr + idat + iend)

print('PNG cree avec succes!')
