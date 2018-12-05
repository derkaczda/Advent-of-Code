use std::fs::File;
use std::fs;
use std::io::prelude::*;
use std::collections::HashMap;

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

fn remove_char(input : String, character : char) -> String
{
    let char_upper = character.to_uppercase().collect::<Vec<_>>();
    let mut result = String::from("");
    for index in 0..input.len() {
        let c = get_nth_char_string(&input, index);
        if c == character || c == char_upper[0]
        {
            continue;
        }
        result.push_str(&c.to_string());
    }

    result
}


pub fn problem1()
{
    let file_content = include_str!("./data/input_5_1.txt");
    let result = string_reduce(String::from(file_content));
    println!("The result string is {}", result.len());

}

pub fn problem2()
{
    let alphabet = (b'a' .. b'z' + 1)      // Start as u8
        .map(|c| c as char)            // Convert all to chars
        .filter(|c| c.is_alphabetic()) // Filter only alphabetic chars
        .collect::<Vec<_>>();

    let file_content = include_str!("./data/input_5_1.txt").to_string();
    //let result = remove_char(file_content, 'a');
    //println!("{}", result);
    let mut hash_map = HashMap::new();
    let mut hash_map_strings = HashMap::new();
    for c in alphabet.iter() {
        let content = &file_content;
        let mod_str = remove_char(content.to_string(), *c);
        //let result = string_reduce(mod_str).len();
        hash_map_strings.insert(
            c,
            mod_str
        );
    }

    for (k, v) in hash_map_strings.iter() {
        let string = &v;
        let result = string_reduce(string.to_string()).len();
        hash_map.insert(
            *k,
            result
        );
    }

    let mut shortest_pol_count = 1000000;
    for (k,v) in hash_map.iter() {
        //println!("{}{}", k,v);
        if(*v < shortest_pol_count)
        {
            shortest_pol_count = *v;
        }
    }

    println!("shortest pol {}", shortest_pol_count);
}