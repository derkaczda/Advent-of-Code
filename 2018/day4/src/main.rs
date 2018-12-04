extern crate chrono;
use chrono::{NaiveDate, NaiveDateTime};
use std::collections::HashMap;
use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::io::BufRead;


fn read_file_into_hashmap(file_path: &str) -> HashMap<i32, String>
{
    let mut dictionary = HashMap::new();
    let f = File::open(file_path).expect("File not found!");
    let mut file = BufReader::new(&f);

    for(num, line) in file.lines().enumerate() {
        let lu = String::from(line.unwrap());
        let mut date_time_str = String::from("");
        let mut action_str = String::from("");
        let mut switch : bool  = false;

        for i in 0..lu.len() {
            if(switch == false)
            {
                if(lu.chars().nth(i).unwrap() != '[' &&
                    lu.chars().nth(i).unwrap() != ']')
                {
                    date_time_str.push(
                        lu.chars().nth(i).unwrap()
                        );
                }

                if(lu.chars().nth(i).unwrap() == ']')
                {
                    switch = true;
                }
            }
            else {
                action_str.push(
                    lu.chars().nth(i).unwrap()
                );
            }
        }
        let mut realString = String::from("");
        let splitDate = date_time_str.split(" ");
        let mut i : i8 = 0;
        for l in splitDate {
            if( i == 0)
            {
                let date = l.split('-');
                let mut y : i8 = 0;
                for s in date {
                    if ( y == 1 || y == 2)
                    {
                        realString.push_str(s);
                    }
                    y = y+1;
                }
            }
            else
            {
                let time = l.split(':');
                for s in time {
                    realString.push_str(s);
                }
            }

            i = i+1;
        }

        dictionary.insert(
            realString.parse::<i32>().unwrap(),
            action_str
        );
    }

    dictionary
}

fn main() 
{

    let input_file_path = "./puzzleinput.txt";
    let dictionary = read_file_into_hashmap(&input_file_path);
    for(k, v) in dictionary.iter(){
        println!("{}, {}", k,v);
    }
}