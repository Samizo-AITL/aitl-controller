# 第3章：OpenLane による ASIC 実装

## ディレクトリ構成
```
designs/aitl_fsm/
 ├── src/aitl_fsm.v
 ├── config.tcl
 └── constraints.sdc（任意）
```

## config.tcl（最小例）
```
set ::env(DESIGN_NAME) aitl_fsm
set ::env(VERILOG_FILES) "src/aitl_fsm.v"
set ::env(CLOCK_PORT) "clk"
set ::env(CLOCK_PERIOD) "10"
```

## コマンド実行
```
./flow.tcl -design aitl_fsm
```

## 生成される成果物
- `results/synthesis/*.v`
- `results/floorplan/*.def`
- `results/placement/*.def`
- `results/routing/*.def`
- `results/gds/aitl_fsm.gds`
