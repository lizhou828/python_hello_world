import types

# 普通函数
def function():
    return 1


# 生成器函数
def generator():
    yield 1


# 异步函数（协程）
async def async_function():
    return 1


# 异步生成器
async def async_generator():
    yield 1


print(type(function) is types.FunctionType)
print(type(generator()) is types.GeneratorType)
print(type(async_function()) is types.CoroutineType)
print(type(async_generator()) is types.AsyncGeneratorType)
# 直接调用异步函数不会返回结果，而是返回一个coroutine对象：

print(async_function())
# <coroutine object async_function at 0x102ff67d8>