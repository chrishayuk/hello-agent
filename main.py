from wasmtime import Store, Module, Instance

store=Store()
module=Module.from_file(store.engine, './tools/math.wat')
instance=Instance(store,module,[])
square = instance.exports(store)['square']
print("square(3) = %d" % square(store,3))