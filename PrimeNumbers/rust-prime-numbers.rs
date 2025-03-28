fn is_prime(number: u32) -> bool {
    if number <= 1 { return false; } 

    let max = number.isqrt();

    for i in 1..max {
        if number % i == 0 { return false; }
    }
    return true;
}

fn main() {
    let max = 9000000;

    for i in 1..max { is_prime(i); }
}
