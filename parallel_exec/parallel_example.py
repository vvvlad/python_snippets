from concurrent.futures import ThreadPoolExecutor


from time import sleep

def perf_test():
    with ThreadPoolExecutor() as executor:
        async_thread = executor.submit(test_async)
        try:
            fn_thread = executor.submit(my_analysis_function)
            result = fn_thread.result()
        finally:
            print(f"Result from thread: {result}")
            
        
def test_async():
    for x in range (30):
        sleep(1)
        print(f"async {x}")

def my_analysis_function():
    for x in range (3):
        sleep(9)
        print(f"analysis {x}")
    return "hi"


if __name__ == "__main__":
    perf_test()