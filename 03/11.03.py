data = "string"
print(hasattr(data, "reverse"))
print(hasattr(data, "index"))

print(getattr(data, "startswith"))ё
data.startswith("st")
print(f"!!! {data.startswith("st")} !!!" )

starts = getattr(data, "startswith", "st")

print(type(starts))



