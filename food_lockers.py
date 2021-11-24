def foodlockers():
    hoods = set(["PTA", "LGA", "PT", "EP", "PSM", "LM", "PM", "ET", "EPR", "NP", "LA", "L", "CJ", "LG", "CA", "LR", "NH"])

    lockers = {}
    lockers["one"] = set(["PTA", "LGA", "PT", "EP"])
    lockers["two"] = set(["PT", "PSM", "LM", "LGA" ])
    lockers["three"] = set(["PT", "EP", "LM", "PM", "ET"])
    lockers["four"] = set(["EPR", "ET", "EP", "LA", "NP"])
    lockers["five"] = set(["PSM", "LG", "CJ" ])
    lockers["six"] = set(["PM", "LM", "L", "CJ", "LR"])
    lockers["seven"] = set(["L", "LA", "ET", "PM"])
    lockers["eight"] = set(["EPR", "NP", "LA", "L"])
    lockers["nine"] = set(["CA", "LG", "LR"])
    lockers["ten"] = set(["NH", "LR", "L"])

    hoods_needed = set(["PTA", "LGA", "PT", "EP", "PSM", "LM", "PM", "ET", "EPR", "NP", "LA", "L", "CJ", "LG", "CA", "LR", "NH"])
    final_lockers = set()
    while hoods_needed:
        best_locker = None
        hoods_covered = set()
        for lock, hoods_for_lockers in lockers.items():
            covered = hoods_needed & hoods_for_lockers
            if len(covered) > len(hoods_covered):
                best_locker = lock
                hoods_covered = covered
                hoods_needed -= hoods_covered
                final_lockers.add(best_locker)

    print("you only need to install: ", final_lockers)

foodlockers()