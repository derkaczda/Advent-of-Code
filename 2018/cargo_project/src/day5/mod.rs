use std::fs::File;
use std::fs;
use std::io::prelude::*;

fn get_nth_char(string: &str, n: usize) -> char
{
    let result = string.chars().nth(n).unwrap();
    result
}

fn get_nth_char_string(string: &String, n: usize) -> char
{
    let result = string.chars().nth(n).unwrap();
    result
}

fn string_reduce(input : String) -> String
{
    let mut result = String::from("");
    let mut skip_next : bool = false;
    let mut reduce_happend : bool = false;
    for index in 0..input.len()
    {
        if(skip_next)
        {
            skip_next = false;
            continue;
        }
        if(index + 1 >= input.len())
        {
            let c_0 = get_nth_char_string(&input, index);
            result.push_str(&c_0.to_string());
            continue;
        }

        let c_0 = get_nth_char_string(&input, index);
        let c_1 = get_nth_char_string(&input, index + 1);

        let c_0_l = c_0.to_lowercase().collect::<Vec<_>>();
        let c_1_l = c_1.to_lowercase().collect::<Vec<_>>();

        if (c_0_l == c_1_l &&
            c_0 != c_1)
        {
            skip_next = true;
            reduce_happend = true;
            continue;
        }

        result.push_str(&c_0.to_string());
    }

    if( result.len() == input.len())
    {
        return result
    }
    else
    {
        let new_result = string_reduce(result);
        new_result
    }
}


pub fn problem1()
{
    let file_content = include_str!("./data/input_5_1.txt");
    let result = string_reduce(String::from(file_content));
    println!("The result string is {}", result.len());

}