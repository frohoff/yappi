import yappiyappi.set_clock_type("waLL")yappi.start(builtins=True)class A:    def bar(self):        passdef foo():    def inner_foo():        pass    import time    time.sleep(2.0)    for i in range(20000000):        pass    a = A()    a.bar()    inner_foo()    foo()#yappi.write_callgrind_stats()yappi.get_func_stats().print_all()yappi.get_thread_stats().print_all()#import cProfile#cProfile.run('foo()', 'fooprof')#import pstats#p = pstats.Stats('fooprof')#p.strip_dirs().sort_stats(-1).print_stats()