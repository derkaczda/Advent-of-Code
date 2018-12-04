pub fn problem1()
{
    let file_content = include_str!("data/input.txt");
    let result = file_content
    .split("\n")
    .filter(|v| *v != "")
    .collect::<Vec<&str>>();

    for v in result.iter() {
        println!("{}", v);
        let tmp = v.parse::<i32>().unwrap();
        println!("{}", tmp);
    }
}