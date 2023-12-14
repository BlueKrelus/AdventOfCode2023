#!/usr/bin/env python3

from cProfile import Profile
from pstats import SortKey, Stats

import task_b

with Profile() as profile:
     task_b.run()
     (
         Stats(profile)
         .strip_dirs()
         .sort_stats(SortKey.CALLS)
         .print_stats()
     )