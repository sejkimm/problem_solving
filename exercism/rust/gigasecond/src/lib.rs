use time::PrimitiveDateTime as DateTime;

// Returns a DateTime one billion seconds after start.
pub fn after(start: DateTime) -> DateTime {
    let end = start + time::Duration::seconds(1_000_000_000);

    return end;
}
