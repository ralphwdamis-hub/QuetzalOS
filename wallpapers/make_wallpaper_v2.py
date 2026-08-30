import struct, zlib, math, os

def png_chunk(t, d):
    c = t + d
    return struct.pack('>I', len(d)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)

W, H = 1920, 1080
cx, cy = W//2, H//2
pixels = []

print('Génération roue solaire v2...')

for y in range(H):
    row = [0]
    for x in range(W):
        dx, dy = x-cx, y-cy
        dist = math.sqrt(dx*dx + dy*dy)
        angle = math.atan2(dy, dx)
        r, g, b = 10, 7, 5

        # Fond dégradé radial jade
        if dist < 520:
            fade = 1 - dist/520
            r = int(10 + fade*8)
            g = int(7 + fade*15)
            b = int(5 + fade*8)

        # Rayons du soleil (20 rayons comme Tonalpohualli)
        ray_angle = (angle % (math.pi/10))
        ray = abs(ray_angle - math.pi/20) / (math.pi/20)
        if dist > 80 and dist < 500 and ray > 0.85:
            intensity = (ray - 0.85) / 0.15
            r = int(r + intensity * 40)
            g = int(g + intensity * 25)
            b = int(b + intensity * 5)

        # Triangles rayonnants alternés
        seg = int((angle + math.pi) / (math.pi/10)) % 2
        if dist > 200 and dist < 320 and seg == 0:
            r = int(r * 0.6 + 30)
            g = int(g * 0.6 + 20)
            b = int(b * 0.6 + 5)

        # Cercles concentriques
        for radius, thick, cr, cg, cb in [
            (490, 5, 201, 162, 39),
            (440, 2, 201, 162, 39),
            (390, 8, 26, 74, 46),
            (340, 2, 201, 162, 39),
            (280, 5, 201, 162, 39),
            (220, 3, 61, 186, 118),
            (160, 5, 201, 162, 39),
            (100, 3, 240, 192, 64),
            (55, 3, 201, 162, 39),
            (30, 28, 201, 162, 39),
        ]:
            if abs(dist - radius) < thick:
                blend = 1 - abs(dist - radius) / thick
                r = int(r*(1-blend) + cr*blend)
                g = int(g*(1-blend) + cg*blend)
                b = int(b*(1-blend) + cb*blend)

        # Croix cardinale
        if (abs(dx) < 3 or abs(dy) < 3) and dist < 490:
            r, g, b = 201, 162, 39

        # Diagonales
        if abs(abs(dx) - abs(dy)) < 3 and dist < 490:
            r, g, b = 26, 74, 46

        # Glyphes des 20 jours — points sur le cercle extérieur
        for i in range(20):
            ga = i * math.pi / 10
            gx = cx + 460 * math.cos(ga)
            gy = cy + 460 * math.sin(ga)
            if math.sqrt((x-gx)**2 + (y-gy)**2) < 8:
                r, g, b = 240, 192, 64

        # Points des 4 directions cardinales
        for ga in [0, math.pi/2, math.pi, 3*math.pi/2]:
            gx = cx + 390 * math.cos(ga)
            gy = cy + 390 * math.sin(ga)
            if math.sqrt((x-gx)**2 + (y-gy)**2) < 12:
                r, g, b = 61, 186, 118

        row += [min(255,max(0,r)), min(255,max(0,g)), min(255,max(0,b))]
    pixels.append(bytes(row))
    if y % 100 == 0:
        print(f'{y}/{H}')

sig = b'\x89PNG\r\n\x1a\n'
ihdr = png_chunk(b'IHDR', struct.pack('>IIBBBBB', W, H, 8, 2, 0, 0, 0))
idat = png_chunk(b'IDAT', zlib.compress(b''.join(pixels), 1))
iend = png_chunk(b'IEND', b'')

home = os.path.expanduser('~')
out = home + '/QuetzalOS/wallpapers/sunstone_v2.png'
with open(out, 'wb') as f:
    f.write(sig + ihdr + idat + iend)
print('PNG créé :', out)
