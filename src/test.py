
# def fun1():
#     l=3
#     fun2(l)
#     print(l) # 3
#
# def fun2(a):
#     a=5

# def fun1():
#     l=[]
#     fun2(l)
#     print(l) # [1]
#
# def fun2(a):
#     a.append(1)


# def fun1():
#     l=[3]
#     fun2(l)
#     print(l) # [3, 1]
#
# def fun2(a):
#     a.append(1)

# def fun1():
#     l=[]
#     fun2(l)
#     print(l) # []
#
# def fun2(a):
#     a=[3]

#
# def fun1():
#     l=[3]
#     fun2(l)
#     print(l) # [3]
#
# def fun2(a):
#     a=[7,1]

# def fun():
#     l = [1,2,3]
#     #print(hex(id(l)))
#     fun2(l)
#     print(l)
#
#
# def fun2(m):
#     ret = []
#     for i in m:
#         ret.append((i))
#     m=ret
#     # m = list(m)
#     #print(hex(id(m)))
#     m.append(4)
#     print('m is {}'.format(m))


# def fun():
#     return [i for i in range(5)]
import ctypes
import gc


def fun(res):
    for i in range(5):
        res.append(i)
        
# We use ctypes moule  to access our unreachable objects by memory address.
class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]


gc.disable()  # Disable generational gc

lst = []
lst.append(lst)

# Store address of the list
lst_address = id(lst)

# Destroy the lst reference
del lst

object_1 = {}
object_2 = {}
object_1['obj2'] = object_2
object_2['obj1'] = object_1

obj_address = id(object_1)

# Destroy references
del object_1, object_2

# Uncomment if you want to manually run garbage collection process
# gc.collect()

# Check the reference count
print(PyObject.from_address(obj_address).refcnt)
print(PyObject.from_address(lst_address).refcnt)
if __name__=='__main__':
    import ctypes
    import gc


    def fun(res):
        for i in range(5):
            res.append(i)


    # We use ctypes moule  to access our unreachable objects by memory address.
    class PyObject(ctypes.Structure):
        _fields_ = [("refcnt", ctypes.c_long)]


    gc.disable()  # Disable generational gc

    lst = []
    lst.append(lst)

    # Store address of the list
    lst_address = id(lst)

    # Destroy the lst reference
    del lst

    object_1 = {}
    object_2 = {}
    object_1['obj2'] = object_2
    object_2['obj1'] = object_1

    obj_address = id(object_1)

    # Destroy references
    del object_1, object_2

    # Uncomment if you want to manually run garbage collection process
    # gc.collect()

    # Check the reference count
    print(PyObject.from_address(obj_address).refcnt)
    print(PyObject.from_address(lst_address).refcnt)