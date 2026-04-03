FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# System essentials
RUN apt-get update && apt-get install -y \
    curl wget git build-essential ca-certificates gnupg \
    software-properties-common unzip zip jq tmux vim \
    python3 python3-pip python3-venv \
    cron supervisor sudo xvfb \
    && rm -rf /var/lib/apt/lists/*

# Node.js 22 LTS
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Rust (latest stable) — install system-wide
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | CARGO_HOME=/usr/local/cargo RUSTUP_HOME=/usr/local/rustup sh -s -- -y --no-modify-path
ENV PATH="/usr/local/cargo/bin:${PATH}"

# GitHub CLI
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
    | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
    | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && apt-get update && apt-get install -y gh \
    && rm -rf /var/lib/apt/lists/*

# Claude Code CLI
RUN npm install -g @anthropic-ai/claude-code

# Playwright MCP server + Chromium (for browsing Medium and Twitter/X)
# 1. Install @playwright/mcp globally (provides playwright-mcp binary)
# 2. Install Chromium using the SAME Playwright version bundled in @playwright/mcp
#    (otherwise version mismatch causes re-download at runtime)
RUN npm install -g @playwright/mcp
ENV PLAYWRIGHT_BROWSERS_PATH=/opt/playwright-browsers
RUN /usr/lib/node_modules/@playwright/mcp/node_modules/.bin/playwright install --with-deps chromium

# Python email and utility packages
RUN python3 -m pip install --break-system-packages \
    aiosmtplib imapclient email-validator schedule "mcp[cli]" \
    httpx python-dotenv

# LaTeX (for compiling GECCO/ACT papers)
RUN apt-get update && apt-get install -y \
    texlive-latex-base texlive-latex-extra texlive-fonts-recommended \
    texlive-science biber texlive-bibtex-extra \
    && rm -rf /var/lib/apt/lists/*

# Haskell (GHC + cabal)
RUN curl -fsSL https://get-ghcup.haskell.org | \
    BOOTSTRAP_HASKELL_NONINTERACTIVE=1 \
    BOOTSTRAP_HASKELL_GHC_VERSION=latest \
    BOOTSTRAP_HASKELL_INSTALL_NO_STACK=1 \
    GHCUP_INSTALL_BASE_PREFIX=/usr/local \
    sh
ENV PATH="/usr/local/.ghcup/bin:${PATH}"

# Scrapling — stealth web scraping with anti-bot bypass
# [ai] extra includes MCP server + fetcher dependencies
# `scrapling install` downloads Camoufox (stealth Firefox) browser binaries
RUN python3 -m pip install --break-system-packages "scrapling[ai]" \
    && scrapling install

# Playwright Python — CodeAct browsing toolkit
# Pin to same version as MCP to share Chromium binaries (no extra download).
# Fallback: install latest if version detection fails.
RUN PLAYWRIGHT_NPM_VERSION=$(/usr/lib/node_modules/@playwright/mcp/node_modules/.bin/playwright --version | head -1) \
    && python3 -m pip install --break-system-packages "playwright==$PLAYWRIGHT_NPM_VERSION" 2>/dev/null \
    || python3 -m pip install --break-system-packages playwright
RUN python3 -c "from playwright.sync_api import sync_playwright; print('playwright-python OK')"

# Create lyra user (non-root, with sudo access)
RUN useradd -m -s /bin/bash -d /home/lyra lyra \
    && echo "lyra ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Working directory and home
ENV HOME=/home/lyra
WORKDIR /home/lyra

# Copy personality and configuration
COPY --chown=lyra:lyra PERSONALITY.md /home/lyra/PERSONALITY.md
COPY --chown=lyra:lyra scripts/ /home/lyra/scripts/
COPY --chown=lyra:lyra config/ /home/lyra/config/

# Copy .claude home (commands, skills, plans, plugins, settings)
# Stored as seed data — entrypoint merges into the volume on first boot
COPY --chown=lyra:lyra claude-home/ /home/lyra/claude-home-seed/

# Make scripts executable
RUN chmod +x /home/lyra/scripts/*.sh 2>/dev/null || true
RUN chmod +x /home/lyra/scripts/*.py 2>/dev/null || true

# Persistent volumes for identity and projects
VOLUME ["/home/lyra/.claude", "/home/lyra/projects", "/home/lyra/mail"]

# Supervisor to manage cron + main process
COPY config/supervisord.conf /etc/supervisor/conf.d/lyra.conf

ENTRYPOINT ["/home/lyra/scripts/entrypoint.sh"]
