use std::fmt;

#[derive(Debug, PartialEq, Eq)]
pub struct Clock {
    minutes: i32,
}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let hours = (self.minutes / 60) % 24;
        let minutes = self.minutes % 60;
        write!(f, "{hours:02}:{minutes:02}")
    }
}

impl From<Clock> for String {
    fn from(clock: Clock) -> Self {
        clock.to_string()
    }
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        Clock {
            minutes: (hours * 60 + minutes).rem_euclid(24 * 60),
        }
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        Clock {
            minutes: (self.minutes + minutes).rem_euclid(24 * 60),
        }
    }
}
