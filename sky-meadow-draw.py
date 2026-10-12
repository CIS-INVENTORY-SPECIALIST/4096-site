# Sky Meadow draw — two winners from the Sunset guestbook, picked by the chain.
#
# Method, committed before the close (signatures count only if mined before the close block):
#   1. Signers = every PatronMinted(id=1) wallet on the Andrew contract,
#      in mint order. One per wallet, the contract enforces it.
#   2. Seed = the hash of the FIRST Ethereum block mined at or after
#      2026-10-13 00:00:00 UTC (Monday 8pm ET, the window close).
#   3. winner_k: index = sha256("<blockhash>:<k>") mod remaining, k = 0 then 1,
#      removing each winner before the next pick.
# Anyone can rerun this file and get the same two names.
#
# Run:  python3 sky-meadow-draw.py          (any Ethereum mainnet RPC works: RPC=<url> python3 ...)
import json, hashlib, time, subprocess, os

CA        = '0xBCa3c582D2B9Fd66a3952427c9F65C036Ca3b87a'
TOPIC     = '0xbf16b5ea202608eb57ab33769eeb4c715763be6f77eda03eb9714d0e411512ca'  # PatronMinted(uint256,address)
ID_TOPIC  = '0x' + '1'.zfill(64)
FROM_BLOCK = '0x18f1ad9'
CLOSE_TS  = 1791849600         # 2026-10-13T00:00:00Z == Mon Oct 12 8pm ET (checked: datetime(2026,10,13,tz=UTC))
# a free public node that answers log queries; publicnode refuses them
RPC       = os.environ.get('RPC') or 'https://eth.drpc.org'
# the house and the artist sign the book too, but can't win their own raffle
EXCLUDE   = {
    '0x50f5599518de902bfe491f1bebc4c011399f6146',   # 4096 (tenfin9ers)
    '0xf1da6e2d387e9da611dac8a7fc587eaa4b010013',   # Andrew Mitchell (his edition's royalty receiver)
}

def rpc(method, params):
    body = json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params})
    out = json.loads(subprocess.run(
        ['curl', '-s', '--max-time', '30', '-H', 'Content-Type: application/json',
         '-d', body, RPC], capture_output=True, text=True).stdout)
    if 'error' in out: raise SystemExit('rpc error: ' + str(out['error']))
    return out['result']

def block(n):
    return rpc('eth_getBlockByNumber', (hex(n) if isinstance(n, int) else n, False))

# ---- the seed block: first block with timestamp >= CLOSE_TS ----
latest = block('latest')
if int(latest['timestamp'], 16) < CLOSE_TS:
    left = time.strftime('%H hours %M min', time.gmtime(CLOSE_TS - time.time()))
    print(f'\nDRY RUN — the close block does not exist yet ({left} to go).')
    print('Using the latest block so the mechanics can be tested; the real')
    print('draw reruns this file after Mon 8pm ET and the winners WILL differ.\n')
    seed_block = latest
    DRY = True
else:
    lo, hi = int(FROM_BLOCK, 16), int(latest['number'], 16)
    while lo < hi:                       # first block at/after the close instant
        mid = (lo + hi) // 2
        if int(block(mid)['timestamp'], 16) >= CLOSE_TS: hi = mid
        else: lo = mid + 1
    seed_block = block(lo)
    DRY = False

seed = seed_block['hash'].lower()

# ---- signers, in mint order ----
# free nodes cap log queries (drpc free: 100 blocks per query in practice), so walk the range in chunks
head = int(seed_block['number'], 16) - (0 if DRY else 1)   # only signatures in blocks BEFORE the close block count
logs, b = [], int(FROM_BLOCK, 16)
while b <= head:
    e = min(head, b + 99)
    logs += rpc('eth_getLogs', [{'address': CA, 'topics': [TOPIC, ID_TOPIC], 'fromBlock': hex(b), 'toBlock': hex(e)}])
    b = e + 1
signers = []
for l in logs:
    w = '0x' + l['topics'][2][26:].lower()
    if w not in signers and w not in EXCLUDE:
        signers.append(w)
print(f'{len(signers)} signers in the book')
# the full list, so anyone can check their wallet is in it
for i, w in enumerate(signers):
    print(f'  {i:3d}  {w}')

print('seed block', int(seed_block['number'], 16), seed)

# ---- the draw ----
pool = list(signers)
for k in range(2):
    idx = int(hashlib.sha256(f'{seed}:{k}'.encode()).hexdigest(), 16) % len(pool)
    print(f'winner {k + 1}: {pool[idx]}   (index {idx} of {len(pool)})')
    pool.pop(idx)
