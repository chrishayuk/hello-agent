(module
 (type $0 (func (param i32 i32) (result i32)))
 (memory $0 0)
 (export "add" (func $assembly/index/add))
 (export "multiply" (func $assembly/index/multiply))
 (export "square" (func $assembly/index/square))
 (export "memory" (memory $0))
 (func $assembly/index/add (param $0 i32) (param $1 i32) (result i32)
  local.get $0
  local.get $1
  i32.add
 )
 (func $assembly/index/multiply (param $0 i32) (param $1 i32) (result i32)
  local.get $0
  local.get $1
  i32.mul
 )
 (func $assembly/index/square (param $0 i32) (result i32)
  local.get $0
  local.get $0
  i32.mul
 )
)
