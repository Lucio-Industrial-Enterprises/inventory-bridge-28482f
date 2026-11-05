# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a shipping quote
in dollars. Zones are `local` and `regional`; weights must be positive.
Supported services:

| Service    | Description                              |
|------------|------------------------------------------|
| `standard` | Base rate (default)                      |
| `express`  | Standard rate plus a flat $7 surcharge   |

Passing an unknown zone or service raises `ValueError`.

### CLI

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```bash
# Standard quote – 2 kg, local zone
python -m warehouse.cli 2 local
# $8.00

# Express quote – 2 kg, local zone
python -m warehouse.cli 2 local --service express
# $15.00
```
