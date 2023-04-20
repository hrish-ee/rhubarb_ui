def gen_id(name: str, dunder_name: str) -> str:
    if "." in dunder_name:
        module_name = dunder_name.split(".")[-2].upper()
    else:
        module_name = dunder_name.upper()
    name = name.replace("_", "-").replace(" ", "-").replace(".", "-")
    return f"{module_name}-{name}"


STORE_TIMER_1H = gen_id("1h timer", __name__)
STORE_TIMER_6H = gen_id("6h timer", __name__)
DEPT_STORE = gen_id("dept all store", __name__)
ROOM_STORE = gen_id("rooms all store", __name__)
BEDS_STORE = gen_id("beds all store", __name__)
ELECTIVES_STORE = gen_id("electives all store", __name__)
SITREP_STORE = gen_id("sitrep all store", __name__)
