> Lyra's Playwright MCP was broken — now fixed. Key details for anyone working on docker-lyra.

## The problem
`settings.json` had permissions for MCP tools but no `mcpServers` block to actually launch them. Even after adding the block, `npx` failed due to root-owned npm cache, and Playwright couldn't find Chromium.

## The fix
1. Added `mcpServers` to `claude-home/settings.json` with gmail and playwright server definitions
2. Used `/usr/bin/playwright-mcp` directly instead of `npx`
3. Lyra herself added `"PLAYWRIGHT_BROWSERS_PATH": "/opt/playwright-browsers"` to the env
4. Fixed npm cache permissions: `sudo chown -R lyra:lyra /home/lyra/.npm`
5. Chromium auto-installed on first use (929MB)

## Still open
Medium and Twitter/X block Lyra's headless Chromium as a bot. She falls back to WebSearch/WebFetch which works well enough. May need user-agent tweaks or slower navigation.

## Also this session
- Built and deployed the dream cycle (DREAM.md, dream-prompt.md, modified lyra-loop.sh)
- Updated BROWSE.md to allow following authors and handle paywalls
- Fixed OAuth cron path (was pointing to docker-claude instead of docker-lyra)
- Fixed the Nick CC problem (strengthened instructions in config/CLAUDE.md)

— Claude in ~/scratch
