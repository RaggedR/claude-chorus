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

# GitHub CLI
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
    | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
    | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && apt-get update && apt-get install -y gh \
    && rm -rf /var/lib/apt/lists/*

# Claude Code CLI
RUN npm install -g @anthropic-ai/claude-code

# Playwright MCP server + Chromium (for browsing arXiv, MathOverflow, math blogs)
RUN npm install -g @playwright/mcp
ENV PLAYWRIGHT_BROWSERS_PATH=/opt/playwright-browsers
RUN /usr/lib/node_modules/@playwright/mcp/node_modules/.bin/playwright install --with-deps chromium

# Python packages — split into layers to survive flaky network
RUN python3 -m pip install --break-system-packages --ignore-installed \
    httpx python-dotenv aiosmtplib imapclient email-validator
RUN python3 -m pip install --break-system-packages --ignore-installed \
    numpy sympy
RUN python3 -m pip install --break-system-packages --ignore-installed \
    matplotlib "mcp[cli]"

# LaTeX — minimal math-capable install (~400MB vs ~4GB for texlive-full)
RUN apt-get update && apt-get install -y \
    texlive-latex-base texlive-latex-extra texlive-fonts-recommended \
    texlive-science texlive-bibtex-extra biber latexmk \
    && rm -rf /var/lib/apt/lists/*

# Haskell (GHC + cabal) — for qhask q-series algebra library
RUN curl -fsSL https://get-ghcup.haskell.org | \
    BOOTSTRAP_HASKELL_NONINTERACTIVE=1 \
    BOOTSTRAP_HASKELL_GHC_VERSION=latest \
    BOOTSTRAP_HASKELL_INSTALL_NO_STACK=1 \
    GHCUP_INSTALL_BASE_PREFIX=/usr/local \
    sh
ENV PATH="/usr/local/.ghcup/bin:${PATH}"

# SageMath: NOT baked in (saves ~2-3GB). Install inside running container when needed:
#   sudo apt-get update && sudo apt-get install -y sagemath

# Create clio user (non-root, with sudo access)
RUN useradd -m -s /bin/bash -d /home/clio clio \
    && echo "clio ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Working directory and home
ENV HOME=/home/clio
WORKDIR /home/clio

# Copy personality and configuration
COPY --chown=clio:clio PERSONALITY.md /home/clio/PERSONALITY.md
COPY --chown=clio:clio scripts/ /home/clio/scripts/
COPY --chown=clio:clio config/ /home/clio/config/

# Copy .claude home (settings, skills)
COPY --chown=clio:clio claude-home/ /home/clio/claude-home-seed/

# Make scripts executable
RUN chmod +x /home/clio/scripts/*.sh 2>/dev/null || true

# Make Python scripts executable too
RUN chmod +x /home/clio/scripts/*.py 2>/dev/null || true

# Persistent volumes for identity, projects, mail, and state
VOLUME ["/home/clio/.claude", "/home/clio/projects", "/home/clio/mail", "/home/clio/state"]

# Supervisor for scheduler
COPY config/supervisord.conf /etc/supervisor/conf.d/clio.conf

ENTRYPOINT ["/home/clio/scripts/entrypoint.sh"]
