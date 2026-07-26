/*  4096 — mainnet configuration (swap in AFTER mainnet deploy) */
window.CONFIG = {
  CHAIN_ID: "0x1",
  RPC_ENDPOINTS: [
    "https://eth-mainnet.g.alchemy.com/v2/alch_3fiqFg8RuxP3NIcBqSEz5",
    "https://cloudflare-eth.com",
    "https://eth.llamarpc.com"
  ],
  // Set these after deployment.
  CONTRACT: null,
  RENDERER: null
};
