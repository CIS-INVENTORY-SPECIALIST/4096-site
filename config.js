/*  4096 — local configuration
 *
 *  This file holds the two things that are yours: your RPC key and, after
 *  deployment, your contract addresses. index.html reads them from here, so you
 *  can replace index.html as often as you like without losing either.
 *
 *  Edit this once. Do not let it get overwritten.
 */
window.CONFIG = {

  // Paste your full Alchemy mainnet URL as the first entry. The public
  // fallbacks keep the canvas readable if your key is throttled; they restrict
  // eth_getLogs ranges, so "Your pixels" needs the Alchemy one.
  RPC_ENDPOINTS: [
    "https://eth-mainnet.g.alchemy.com/v2/alch_3fiqFg8RuxP3NIcBqSEz5",
    "https://cloudflare-eth.com",
    "https://eth.llamarpc.com"
  ],

  // Set these after deployment. While CONTRACT is null the site runs on
  // simulated data and shows the demo banner.
  CONTRACT: null,
  RENDERER: null
};
