pub fn problem1()
{
    let file_content = include_str!("data/input.txt");
    let result: i32 = file_content
    .split("\r\n")
    .filter(|v| *v != "")
    .map(|v| v.parse::<i32>().unwrap())
    .sum();

    println!("Result of 1-1: {}", result);
}