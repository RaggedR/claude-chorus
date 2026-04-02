# Astronomy N-Body & KAM Theory Project

## Overview
A multi-agent system for orbital mechanics simulation and stability analysis, with focus on KAM (Kolmogorov-Arnold-Moser) theory. Combines Fortran numerical core with Python analysis and MCP server for Claude integration.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    MCP Server (Python)                  │
│  Tools: simulate, analyze_stability, poincare_section   │
└─────────────────────┬───────────────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Data Agent   │ │ Sim Agent    │ │ Analysis     │
│              │ │              │ │ Agent        │
│ - Gaia       │ │ - Run Fortran│ │ - Lyapunov   │
│ - JPL        │ │ - Parameters │ │ - Frequency  │
│ - Exoplanet  │ │ - Output     │ │ - Poincaré   │
└──────────────┘ └──────┬───────┘ └──────────────┘
                        │
                        ▼
              ┌──────────────────┐
              │  Fortran Core    │
              │                  │
              │ - Symplectic     │
              │   integrator     │
              │ - N-body forces  │
              │ - High precision │
              └──────────────────┘
```

## Components

### 1. Fortran Core (`/fortran/`)
- **integrator.f90** - Symplectic integrator (Yoshida 4th/6th order)
- **nbody.f90** - Gravitational N-body force computation
- **io.f90** - Binary output for trajectories
- **Makefile** - Compilation with gfortran, optimization flags

### 2. Python Layer (`/python/`)
- **runner.py** - Compile and execute Fortran, manage I/O
- **analysis.py** - KAM-specific analysis:
  - Frequency analysis (Laskar's NAFF method)
  - Lyapunov exponent computation
  - Action-angle variable extraction
- **visualization.py** - Poincaré sections, phase portraits, frequency maps
- **data_fetch.py** - Astroquery interface for real orbital data

### 3. MCP Server (`/mcp_server/`)
- **server.py** - FastMCP-based server
- **Tools exposed:**
  - `simulate_system` - Run N-body simulation with parameters
  - `fetch_orbital_data` - Get real data from Gaia/JPL/NASA
  - `analyze_kam` - Frequency analysis, detect invariant tori
  - `compute_lyapunov` - Measure chaos
  - `poincare_section` - Generate section plot
  - `frequency_map` - 2D stability map (action space)

### 4. Sub-Agents (`/agents/`)
- **data_agent.py** - Fetches and formats astronomical data
- **simulation_agent.py** - Orchestrates Fortran runs
- **analysis_agent.py** - Interprets results, detects resonances

## KAM Theory Focus

### Key Analyses
1. **Frequency Analysis (NAFF)** - Detect quasi-periodic orbits by extracting fundamental frequencies
2. **Frequency Maps** - Plot frequency ratios in action space, identify resonance gaps
3. **Poincaré Sections** - Visualize invariant tori vs chaotic seas
4. **Perturbation Studies** - Vary mass ratios to watch tori break down

### Example Investigations
- Kirkwood gaps in asteroid belt (Jupiter resonances)
- Stability of exoplanet systems under perturbation
- Restricted 3-body problem: find stable/unstable regions
- Solar system long-term stability (inner planets)

## Directory Structure

```
/Users/robin/git/astronomy/
├── fortran/
│   ├── src/
│   │   ├── integrator.f90
│   │   ├── nbody.f90
│   │   └── io.f90
│   ├── Makefile
│   └── bin/
├── python/
│   ├── runner.py
│   ├── analysis.py
│   ├── visualization.py
│   ├── data_fetch.py
│   └── requirements.txt
├── mcp_server/
│   ├── server.py
│   └── tools/
├── agents/
│   ├── data_agent.py
│   ├── simulation_agent.py
│   └── analysis_agent.py
├── data -> /Users/robin/data/astronomy/
│   └── (symlink to external data directory)
├── examples/
│   └── (example scripts)
└── README.md
```

## Data Storage

Simulation outputs and cached astronomical data stored in:
```
/Users/robin/data/astronomy/
├── simulations/    # Fortran output files
├── cache/          # Cached API responses (Gaia, JPL)
└── results/        # Analysis outputs, plots
```

Project directory will contain a symlink: `data -> /Users/robin/data/astronomy/`

## Dependencies

### Fortran
- gfortran (via Homebrew: `brew install gcc`)

### Python
- numpy, scipy (numerics)
- astropy, astroquery (astronomical data)
- matplotlib (visualization)
- fastmcp (MCP server)

## Implementation Order

1. **Fortran integrator** - Get symplectic N-body working
2. **Python runner** - Wrap Fortran execution
3. **Basic analysis** - Lyapunov, simple frequency extraction
4. **MCP server** - Expose core tools
5. **NAFF implementation** - Proper frequency analysis for KAM
6. **Sub-agents** - Orchestration layer
7. **Frequency maps** - Full KAM visualization

## Verification

1. **Fortran core**: Integrate known 2-body problem, verify Kepler ellipse
2. **Symplectic check**: Verify energy conservation over long integrations
3. **KAM analysis**: Reproduce known results (e.g., standard map, Hénon-Heiles)
4. **MCP server**: Test tools via Claude Code
5. **End-to-end**: "Analyze stability of Jupiter's Trojans" workflow
