def satr_uzunligi(satr):
    return sum(1 for simvol in satr)
```

```python
print(satr_uzunligi("Hello, World!"))  # 13
print(satr_uzunligi("Python"))  # 6
