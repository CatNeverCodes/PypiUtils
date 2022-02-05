from . import time


def load_config():
    from . cfg import config
    return config


def timer(fn):
    __call_from__ = "/".join(fn.__code__.co_filename.split("\\")[-2:])
    def wrapper(*args, **kwargs):
        result = {}

        time_start = time.time()
        result_fn = fn(*args, **kwargs)
        time_end = time.time()

        time_cost = round(time_end - time_start, 2)
        time_created = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_start))
        time_finished = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_end))

        result["Created"] = time_created
        result["Finished"] = time_finished
        result["CostTime"] = time_cost
        result["File"] = __call_from__
        result["Function"] = fn.__qualname__
        result["Result"] = result_fn
        return result
    return wrapper
