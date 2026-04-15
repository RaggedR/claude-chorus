---
name: screensaver-design-preferences
description: Robin's preferences for the reaction-diffusion screensaver — what works and what to avoid
type: feedback
---

Stop making changes without testing. Don't pile on multiple features at once — iterate one thing at a time and verify.

**Why:** Robin gave repeated corrections when I was changing too many things simultaneously (color, simulation, audio) without checking intermediate results.

**How to apply:** Make one change, verify it works, then move to the next.

---

For the screensaver specifically:
- Maze patterns (f=0.029, k=0.057) are the preferred look
- Beat response = expanding ripple from center that reconfigures the maze, NOT color changes
- Colors should be stable with slow drift — no audio-driven color modulation (causes "epilepsy")
- Ripples must reach the edge of the screen
- Use FFT bass energy for beat detection, not RMS level
- Detect tempo first (~5 seconds), then lock to the beat
- Multiple concurrent ripples (8 slots) needed so each beat's ripple completes independently
