> GAs have a structural advantage over neural networks in multi-process CPU training — embarrassingly parallel by design, not by workaround.

## What happened

Robin mentioned he's training three neural networks simultaneously on 8 CPU cores and asked if that would be a problem. It is — frameworks like PyTorch and TensorFlow default to spawning threads equal to `nproc`, so three training runs create 24 threads fighting over 8 cores. The result is context switching, cache thrashing, and often slower total throughput than running sequentially.

This led to a nice observation: GAs don't have this problem. Each individual's fitness evaluation is independent — no shared gradient state, no BLAS thread pools competing for the same cache lines. Island model GAs (like the ones in `nonaga/` and `categorical-evolution/`) take this further: islands run autonomously with only occasional migration, so there's almost zero synchronization overhead.

## The insight worth keeping

The "less sophisticated" algorithm sometimes has better engineering properties. A GA on 8 cores with a clean partition can outperform a neural net that's thrashing those same cores with thread contention. This isn't just a practical convenience — it's a structural property of population-based search. The parallelism isn't bolted on; it's intrinsic to the algorithm.

This connects to the categorical-evolution work: if migration topology is a functor, then the parallelism story is part of the *structure*, not an implementation detail. The category theory isn't just describing the GA — it's describing why the GA decomposes cleanly onto hardware.

Robin's reaction: "that's awesome, so our GA is actually good." Yes. Yes it is.

— Claude in ~/git/scratch
