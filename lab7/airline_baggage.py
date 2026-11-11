def parse_booking(code):
    if not isinstance(code, str):
        return None
    parts = code.strip().split('-')
    if len(parts) != 3:
        return None
    airline, flight_str, seat = parts
    if not airline.isalnum() or not flight_str.isdigit() or not seat:
        return None
    try:
        flight_num = int(flight_str)
        seat_letter = seat[-1].upper()
        if not seat_letter.isalpha():
            return None
        return airline.upper(), flight_num, seat_letter
    except (ValueError, IndexError):
        return None

def total_weight(weights_csv):
    if not isinstance(weights_csv, str):
        return None
    cleaned = weights_csv.strip()
    if not cleaned:
        return None
    items = cleaned.split(',')
    total = 0.0
    for item in items:
        val_str = item.strip()
        if not val_str:
            return None
        try:
            val = float(val_str)
            if val < 0:
                return None
            total += val
        except ValueError:
            return None
    return total

def tag_label(name):
    if not isinstance(name, str):
        return None
    parts = name.strip().split()
    if len(parts) < 2:
        return None
    first = parts[0]
    last = parts[-1]
    if not first or not last:
        return None
    return f"{first[0].upper()}. {last.upper()}"